#include "_sign.h"

static const char SIGN_SUFFIX[] = {'t', 'i', 'e', 'b', 'a', 'c', 'l', 'i', 'e', 'n', 't', '!', '!', '!'};

static inline void __pyStr2UTF8(const uint8_t **dst, size_t *dstSize, PyObject *pyoStr)
{
    if (PyUnicode_1BYTE_KIND == PyUnicode_KIND(pyoStr))
    {
        (*dst) = PyUnicode_DATA(pyoStr);
        (*dstSize) = PyUnicode_GET_LENGTH(pyoStr);
    }
    else
    {
        (*dst) = PyUnicode_AsUTF8(pyoStr);
        (*dstSize) = strlen(*dst);
    }
}

PyObject *sign(PyObject *self, PyObject *args)
{
    PyObject *items;
    if (!PyArg_ParseTuple(args, "O", &items))
    {
        PyErr_SetString(PyExc_ValueError, "failed to parse args");
        return NULL;
    }
    Py_ssize_t listSize = PyList_GET_SIZE(items);

    mbedtls_md5_context md5Ctx;
    mbedtls_md5_init(&md5Ctx);
    mbedtls_md5_starts(&md5Ctx);
    char itoaBuffer[20];
    char equal = '=';
    for (Py_ssize_t iList = 0; iList < listSize; iList++)
    {
        PyObject *item = PyList_GET_ITEM(items, iList);

        uint8_t *key;
        size_t keySize;
        PyObject *pyoKey = PyTuple_GET_ITEM(item, 0);
        __pyStr2UTF8(&key, &keySize, pyoKey);
        mbedtls_md5_update(&md5Ctx, key, keySize);

        mbedtls_md5_update(&md5Ctx, &equal, sizeof(equal));

        uint8_t *val;
        size_t valSize;
        PyObject *pyoVal = PyTuple_GET_ITEM(item, 1);
        if (PyUnicode_Check(pyoVal))
        {
            __pyStr2UTF8(&val, &valSize, pyoVal);
        }
        else
        {
            int64_t ival = PyLong_AsLongLong(pyoVal);
            val = itoaBuffer;
            uint8_t *valEnd = i64toa(ival, val);
            valSize = valEnd - val;
        }
        mbedtls_md5_update(&md5Ctx, val, valSize);
    }

    mbedtls_md5_update(&md5Ctx, SIGN_SUFFIX, sizeof(SIGN_SUFFIX));

    uint8_t md5[TBH_MD5_HASH_SIZE];
    mbedtls_md5_finish(&md5Ctx, md5);

    char dst[TBH_MD5_STR_SIZE];
    size_t dstOffset = 0;
    for (size_t imd5 = 0; imd5 < TBH_MD5_HASH_SIZE; imd5++)
    {
        dst[dstOffset] = HEX_LOWCASE_TABLE[md5[imd5] >> 4];
        dstOffset++;
        dst[dstOffset] = HEX_LOWCASE_TABLE[md5[imd5] & 0x0F];
        dstOffset++;
    }

    return PyUnicode_FromKindAndData(PyUnicode_1BYTE_KIND, dst, TBH_MD5_STR_SIZE);
}