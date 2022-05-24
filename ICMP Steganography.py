import array
import socket
import struct


def chksum(packet: bytes) -> int:
    if len(packet) % 2 != 0:
        packet += b'\0'

    res = sum(array.array("H", packet))
    res = (res >> 16) + (res & 0xffff)
    res += res >> 16

    return (~res) & 0xffff


class ICMPPacket:


    def build(self,msg: int) -> bytes:
        packet = struct.pack(
            '!BBHHHI',
            17,            # Type
            0,              #Code
            0,              #Checksum
            0,              # Identifier
            msg,             #sequence number
            0               #Address mask
        )

        return packet


if __name__ == '__main__':
    dst = '192.168.1.1'

    pak = ICMPPacket(
    )

    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    s.sendto(pak.build(int.from_bytes(bytes("hi",encoding="utf-8"),'big')), (dst, 0))