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


class UDPPacket:
    def __init__(self,
                 src_port:  int,
                 dst_port:  int,):       
        self.src_port = src_port
        self.dst_port = dst_port


    def build(self,msg: int) -> bytes:
        packet = struct.pack(
            '!HHHH',
            self.src_port,  # Source Port
            self.dst_port,  # Destination Port
            0,              # Length
            msg,              # Checksum (initial value)
        )

        return packet


if __name__ == '__main__':
    dst = '192.168.1.1'

    pak = UDPPacket(
        9999,
        9990,
    )

    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)

    s.sendto(pak.build(int.from_bytes(bytes("hi",encoding="utf-8"),'big')), (dst, 0))