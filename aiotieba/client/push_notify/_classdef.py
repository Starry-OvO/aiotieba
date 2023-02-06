from .._classdef import TypeMessage


class WsNotify(object):
    """
    websocket主动推送消息提醒
    """

    __slots__ = [
        '_note_type',
        '_group_type',
        '_group_id',
        '_last_msg_id',
        '_create_time',
    ]

    def _init(self, data_proto: TypeMessage) -> "WsNotify":
        data_proto = data_proto.data
        self._note_type = data_proto.type
        self._group_type = data_proto.groupType
        self._group_id = data_proto.groupId
        self._last_msg_id = data_proto.msgId
        self._create_time = str(create_time) if (create_time := data_proto.et) else 0
        return self

    def __repr__(self) -> str:
        return str(
            {
                'note_type': self._note_type,
                'group_type': self._group_type,
                'group_id': self._group_id,
                'last_msg_id': self._last_msg_id,
            }
        )

    @property
    def note_type(self) -> int:
        """
        消息类别
        """

        return self._note_type

    @property
    def group_type(self) -> int:
        """
        消息组类别
        """

        return self._group_type

    @property
    def group_id(self) -> int:
        """
        消息组id
        """

        return self._group_id

    @property
    def last_msg_id(self) -> int:
        """
        最后一条消息的id
        """

        return self._last_msg_id

    @property
    def create_time(self) -> int:
        """
        推送时间

        Note:
            10位时间戳 以秒为单位
        """

        return self._create_time
