#pragma once

#include "base32/base32.h"

#define TBH_UUID_SIZE 36
#define TBH_ANDROID_ID_SIZE 16

#define TBH_MD5_HASH_SIZE 16
#define TBH_MD5_STR_SIZE (TBH_MD5_HASH_SIZE * 2)

#define TBH_SHA1_HASH_SIZE 20
#define TBH_SHA1_HEX_SIZE (TBH_SHA1_HASH_SIZE * 2)
#define TBH_SHA1_BASE32_SIZE (BASE32_LEN(TBH_SHA1_HASH_SIZE))

#define TBH_HELIOS_HASH_SIZE 5
#define TBH_HELIOS_BASE32_SIZE (BASE32_LEN(TBH_HELIOS_HASH_SIZE))

#define TBH_CUID_GALAXY2_SIZE (TBH_MD5_STR_SIZE + 2 + TBH_HELIOS_BASE32_SIZE)

#define TBH_C3_AID_SIZE (4 + TBH_SHA1_BASE32_SIZE + 1 + TBH_HELIOS_BASE32_SIZE)

static const char HEX_UPCASE_TABLE[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};
static const char HEX_LOWCASE_TABLE[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};