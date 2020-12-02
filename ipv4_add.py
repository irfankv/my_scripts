# from dateutil import tz
# from datetime import datetime
# a = 0
# b = 0
# c = 0
# # 10.a.b.c
# for i in range(0, 1021):
#     if i <= 255:
#         c = i
#     elif i > 255 and i <= 510:
#         b = 1
#         c = int(i) % 255
#         c = i - 255
#     elif i > 510 and i <= 765:
#         b = 2
#         c = int(i) % 510
#         # c = i - 255
#     elif i > 764 and i <= 1020:
#         b = 3
#         c = int(i) % 765
#         # c = i - 255

#     # print(f"10.{a}.{b}.{c}")

#     # print(f"20.{b}.{c}.0/24")
"ACL V4"
j = 0
c = 0
k = 0
for i in range(1, 2):
    c = 41 + (int(i % 255) - 1)
    for j in range(0, 256):

        h = hex(k).split("x")[1]
        l = 0 + j
        as_num1 = 100 + int(k)
        bunde = f"""
interface Bundle-Ether100.{k}
 ipv4 address 10.{c}.{j}.1 255.255.255.0
 ipv6 address 2001:4141:4141:{h}::1/124
 encapsulation dot1q {k}
!
"""

        # print(bunde)
        interface = f"""
interface HundredGigE0/3/0/29.{k}
 ipv4 address 10.{c}.{j}.1 255.255.255.0
 ipv6 address 2001:1717:1717:{h}::1/124
 encapsulation dot1q {k}
!
router bgp 100
 neighbor 10.{c}.{j}.2
  remote-as {as_num1}
  address-family ipv4 unicast
   route-policy pass in
   route-policy pass out
  !

"""
        k += 1
        # print(interface)
        config = f"""
interface HundredGigE0/3/0/29.{k}
 vrf abf-v4
 ipv4 address 117.{c}.{j}.1 255.255.255.0
 ipv6 address 2a04:3542:1000:910:a8aa:aaff:7{h}:1/112
 encapsulation dot1q {k}
 ipv4 access-group v4-sub-scale-1 ingress
!
1 permit udp host 117.117.1.2 eq 65000 host 10.37.2.2 eq rip dscp 9 nexthop1 vrf abf-v4 ipv4 10.131.0.2
"""
        # config2 = f"{k} permit udp host host 117.{c}.{j}.2 eq 65000 host 10.37.2.2 eq rip dscp 9 nexthop1 vrf abf-v4 ipv4 10.131.0.2"
        # config3 = f"interface HundredGigE0/0/0/29.{k} ipv4 access-group vrf-sub-scale ingress"
        config_fs = f"""class-map type traffic match-all bgpfs_ipv4_{k}
match destination-address ipv4 10.17.0.0 255.255.255.0
match source-address ipv4 47.{c}.{j}.0 255.255.255.0
match protocol tcp 
match destination-port 20000 
match source-port 20000 
end-class-map
! 
policy-map type pbr bgpfs_ipv4
class type traffic bgpfs_ipv4_{k} 
drop
end-policy-map
!
"""
        as_num = 100 + k
        v6 = hex(k).split("x")[1]
        config_lpts = f"""
interface  HundredGigE0/0/0/29.{k}
 ipv4 address 10.{c}.{j}.1 255.255.255.0
 ipv6 address 2001:4747:4747:{v6}::1/124
 encapsulation dot1q {k}
!
router bgp 100
 neighbor 10.{c}.{j}.2
  remote-as {as_num}
  address-family ipv4 unicast
   route-policy pass in
   route-policy pass out
  !
 !
"""
        bgp_conf = f"""
router bgp 100
 neighbor 10.{c}.{j}.2
  remote-as {as_num}
  address-family ipv4 unicast
   route-policy pass in
   route-policy pass out
  !
 !
"""
        # print(bgp_conf)
        # print(config2)

for i in range(1, 1501):
    j = 60000 + int(i)
    v6 = hex(i).split("x")[1]
    # config = f"{i} deny tcp host 10.47.0.2 eq {j} host 10.17.0.2 eq {j}"
    egree_acl_v4 = (
        f"{i} permit tcp host 19.1.1.2 eq {j} host 29.1.1.2 eq 60001 dscp af12"
    )
    egree_acl_v6 = f"{i} deny icmpv6 host 2001:4747:4747:4747::{v6} host 2001:1717:1717:1717::2 time-exceeded dscp af41"
    # print(egree_acl_v4)

    port = 64000 + i
    v6 = hex(i).split("x")[1]
    p = 63000 + int(i)
    acl = f"{i} permit udp host 2001:2727:2727:2727::2 eq {p} host 2001:5757:5757:5757::2 eq {i} dscp af31 nexthop1 ipv6 2002:1414:1414:1414::2 nexthop2 ipv6 2004:4:1:1::"
    no_acl = f"no {i}"
    po = 63000 + int(i)
    # print(acl)
    v6_abf = f"{i} permit tcp host 2001:2727:2727:2727::2 eq {po} host 2001:5757:5757:5757::2 eq {i} dscp af31"
    # print(v6_abf)
    v6_egress = f"{i} deny tcp host 2001:1717:1717:1717::2 eq {po} host 2001:4747:4747:4747::2 eq {po}"
    # print(v6_egress)
    config_v6 = f"{i} deny tcp host 2001:4747:4747:4747::2 eq {p} host 2001:1717:1717:1717::2 eq {p}"
    # print(config_v6)
    config = f"""class-map type traffic match-all bgpfs_ipv6_{i}
 match destination-address ipv6 2047:47:47:{v6}::/64
 match source-address ipv6 2001:1717:1717:1717::/124
 match protocol udp 
 match destination-port 15000-20000
 match source-port 15001 
 end-class-map
! 
policy-map type pbr bgpfs_ipv6
 class type traffic bgpfs_ipv6_{i}
  drop
 ! 
 class type traffic class-default 
 ! 
 end-policy-map
! 

"""

    acl_abf = f"{i} permit tcp host 10.47.0.2 eq {j} host 10.17.0.2 eq {j} dscp af41 nexthop1 ipv4 10.114.0.1 nexthop2 ipv4 114.114.0.1 nexthop3 ipv4 1.1.1.1"
    # print(acl_abf)
    no_flow = f"no class-map type traffic bgpfs_ipv6_{i}"
    # print(config)
    # print(config_v6)
    conf_v4 = f"""{i} deny udp 10.17.0.0/24 eq 60000 47.47.{i}.0/24 range 50000 60000 dscp af11"""
    o = int(i) + 48
    acl_qos = f"""
ipv4 access-list ipv4_qos_acl_{i}
 1 permit udp 10.17.0.0/24 eq 50000 47.{o}.1.0/24 gt 60000
 2 permit udp 10.17.0.0/24 eq 50000 47.{o}.2.0/24 gt 60000
 3 permit udp 10.17.0.0/24 eq 50000 47.{o}.3.0/24 gt 60000
 4 permit udp 10.17.0.0/24 eq 50000 47.{o}.4.0/24 gt 60000
 5 permit udp 10.17.0.0/24 eq 50000 47.{o}.5.0/24 gt 60000
 6 permit udp 10.17.0.0/24 eq 50000 47.{o}.6.0/24 gt 60000
 7 permit udp 10.17.0.0/24 eq 50000 47.{o}.1.0/24 gt 60000
 8 permit udp 10.17.0.0/24 eq 50000 47.{o}.2.0/24 gt 60000
 9 permit udp 10.17.0.0/24 eq 50000 47.{o}.3.0/24 gt 60000
 10 permit udp 10.17.0.0/24 eq 50000 47.{o}.4.0/24 gt 60000
 11 permit udp 10.17.0.0/24 eq 50000 47.{o}.5.0/24 gt 60000
 12 permit udp 10.17.0.0/24 eq 50000 47.{o}.6.0/24 gt 60000
 13 permit udp 10.17.0.0/24 eq 50000 47.{o}.4.0/24 gt 60000
 14 permit udp 10.17.0.0/24 eq 50000 47.{o}.5.0/24 gt 60000
 15 permit udp 10.17.0.0/24 eq 50000 47.{o}.6.0/24 gt 60000
 16 permit udp 10.17.0.0/24 eq 50000 47.{o}.4.0/24 gt 60000
!
class-map match-any ipv4_qos_cm_{i}
 match access-group ipv4 ipv4_qos_acl_{i} 
 end-class-map
! 
policy-map qos_policy
 class ipv4_qos_cm_{i}
  set precedence flash
 ! 
 class class-default
 ! 
 end-policy-map
! 
"""
    # print(config)

# j = 0
# k = 0
# l = 1
# for i in range(1, 38):
#     c = int(i % 255)-1
#     for j in range(0, 256, 4):
#         print(f"{l} permit ipv4 17.17.{c}.{j}/30 any dscp 9 nexthop1 ipv4 10.31.0.2 nexthop2 ipv4 10.131.0.2")
#         l += 1

# j = 140
# for i in range(1, 20):
#     j = 140+int(i)
#     k = 4 + int(i)
#     conf = f"""
#     class-map type traffic match-all bgpfs_ipv4_udp_{i}
#     match destination-address ipv4 10.17.{j}.0/30
#     match source-address      ipv4 37.37.{k}.0/30
#     match protocol udp
#     match destination-port         10000-20000
#     match source-port              10000-20000
#     end-class-map
#     !
#     class-map type traffic match-all bgpfs_ipv4_tcp_{i}
#     match destination-address ipv4 10.17.{j}.0/30
#     match source-address      ipv4 37.37.{k}.0/30
#     match protocol tcp
#     match destination-port         10000-20000
#     match source-port              10000-20000
#     end-class-map
#     !
#     policy-map type pbr bgpfs_ipv4
#     class type traffic bgpfs_ipv4_tcp_{i}
#     drop
#     class type traffic bgpfs_ipv4_udp_{i}
#     drop
#     """
#     print(conf)


# for i in range(0, 255, 4):
# print(i)
# if i >= 256:
#     k = 1
#     i = i - 256
# if 512 <= i >= 768:
#     k = 2
#     i = i - 512
# if 768 <= i >= 1024:
#     k = 3
#     i = i - 768
# if 1024 <= i >= 1280:
#     k = 4
#     i = i - 1024

# print(f"{j} permit tcp 17.17.{k}.{i}/30 eq 65000 any eq 65001 dscp 9 nexthop1 ipv4 10.131.0.2 nexthop1 ipv4 10.31.0.2")
# j += 1
# for i in range(1, 50):
#     k = 1130+i
#     config = f"""
# interface HundredGigE0/3/0/17.{i}
#  vrf abf-v4
#  encapsulation dot1q {i}
#  ipv4 address 10.113.{i}.1 255.255.255.0
#  ipv4 address 113.113.{i}.1 255.255.255.0 secondary
#  ipv6 address 2001:abcd:dead:cafe:{k}::1/96
# !
# """
#     print(config)

# for i in range(3, 1001):
#     j = hex(i).split("x")[1]
#     k = i
#     print(f"{i} deny icmpv6 host 2001: 20: 1: 1: : {j} host 2001: 10: 1: 1: : 2 time-exceeded")
# print(f"{i} deny icmpv6 host 2001:20:1:1::{j} host 2001:10:1:1::2 time-exceeded")
# print(f"{i} permit tcp any eq {i} any eq {i} dscp af22")
# print(f"2001:12:1:{j}::/64")
# print(f"{k} deny tcp host 2001:20:0:1::2 gt 1023 host 2001:10:0:1::{j} gt 1023")
# print(f"{i} deny tcp host 2001:20:0:1::2 gt 1023 host 2001:10:0:1::2 gt 1023")
# print(f"{i} deny ipv6 host 2001:10:1:1::{j} host 2001:20:1:1::2 dscp af22")
# print(
#     f"{i} permit tcp host 2001:11:11::{j} gt 1 host 2001:21:21::2 lt 9000 nexthop1 ipv6 2001:192:168::2 nexthop2 ipv6 2001:192:168:3::2 nexthop3 ipv6 2001:192:168:1::2"
# )
# for i in range(2, 51):
# print(f"{i} deny tcp any eq {i} net-group bgl-r1-routes-v4 eq {i} dscp af33")

# def func(meass):
#     meass_func = "Variable Inside func"
#     print(f"{meass_func}")

# # print(f"{meass_func}")

# func("Irfan")

# for i in range(2, 216):
#     j = 10+i
#     k = hex(i).split("x")[1]
#     conf = f"""
# interface Bundle-Ether100.{i}
#  ipv4 address 10.{j}.1.2 255.255.0.0
#  ipv6 address 2001:10:{j}:1::2/64
#  encapsulation dot1q {i}
#     """
#     # print(conf)

#     conf_static = f"""
# 2001:100:11::{i}/128 Bundle-Ether100.{i} 2001:10:{j}:1::1
#      """
#     print(conf_static)

# # METHOD 1: Hardcode zones:
# from_zone = tz.gettz('GMT')
# to_zone = tz.gettz('IST')

# # METHOD 2: Auto-detect zones:
# from_zone = tz.tzutc()
# to_zone = tz.tzlocal()

# # utc = datetime.utcnow()
# utc = datetime.strptime('2020-03-4 17:37:21', '%Y-%m-%d %H:%M:%S')

# # Tell the datetime object that it's in UTC time zone since
# # datetime objects are 'naive' by default
# utc = utc.replace(tzinfo=from_zone)

# # Convert time zone
# central = utc.astimezone(to_zone)

# print(str(central).split('+')[0])

# # 2020-03-04 23:07:21+05:30
# for i in range(1, 1001):
#     print(f"{i} deny tcp host 20.1.0.2 eq {i} host 10.1.0.2 eq {i}")

# for i in range(2, 201):
#     a = 10000+i
#     j = hex(+i).split("x")[1]
#     config = f"""
# interface HundredGigE0/7/0/33.{i}
#  encapsulation dot1q {i}
#  ipv4 address 10.17.{i}.1 255.255.255.0
#  ipv4 address 10.117.{i}.1 255.255.255.0 secondary
#  ipv6 address 2a04:3542:1000:910:a8aa:aaff:17{j}:1/112
# !
# router bgp 100
# neighbor 10.17.{i}.2
#   remote-as {a}
#   address-family ipv4 unicast
#    route-policy pass in
#    route-policy pass out
#   !
#  !
# !
# """
#     print(config)
step = 1
for i in range(1, 200):

    step = step
    if step >= 255:
        c = int(step % 255)
        d = 12
    else:
        c = int(step % 255)
        d = 11
    conf = """
interface HundredGigE0/0/0/31.%s
 ipv4 address 99.19.%d.%s 255.255.255.252
 """ % (
        i,
        d,
        c,
    )
    # print(conf)
    step += 4

for i in range(101, 102):
    config_bvi = """
interface Bundle-Ether1201.{} l2transport
 encapsulation dot1q {}
 rewrite ingress tag pop 1 symmetric
!
interface HundredGigE0/2/0/29.{} l2transport
 encapsulation dot1q {}
 rewrite ingress tag pop 1 symmetric
!
l2vpn
 bridge group aclObvi
  bridge-domain {}
   interface Bundle-Ether1201.{}
   !
   interface HundredGigE0/2/0/29.{}
   !
   routed interface BVI{}
   !
  !
 !
!
interface BVI{}
 ipv4 address 19.1.{}.1 255.255.255.0
 ipv6 address 19:1:{}::1/64
 mac-address cafe.dead.{}
!
router ospf bvi
 area 0
  interface BVI{}
   passive enable
  !
 !
!
router ospfv3 bvi
 area 0
  interface BVI{}
   passive
  !
 !
!
""".format(
        i, i, i, i, i, i, i, i, i, i, i, i, i, i
    )
    # print(config_bvi)


for i in range(4, 301):
    ace = "{} permit tcp host 19.1.1.2 eq 1024 host 39.1.1.2 eq {} dscp cs4".format(
        i, i
    )
    # ace = "no {}".format(i)
    # ace = "{} deny tcp net-group scale eq 1024 net-group scale eq {} dscp cs4".format(
    #     i, i
    # )
    # ace = "{} deny tcp net-group scale port-group port-eq net-group scale eq {} dscp cs4".format(
    #     i, i
    # )
    j = 60000 + int(i)
    # ace = "{} deny udp net-group bvi_host port-group bvi_port net-group bvi_host eq {}".format(
    #     i, j
    # )
    j = 13 + int(i)
    ace = "{} permit udp host 19.2.3.2 eq 14 host 49.4.1.2 eq {} dscp cs3 nexthop1 ipv4 192.1.4.2 nexthop2 ipv4 192.1.3.2 nexthop3 ipv4 192.1.2.2".format(
        i, j
    )
    print(ace)

for i in range(1, 11):
    config = """
class-map type traffic match-all bgp_fs_v4_{}
    match protocol udp 
    match source-port 10000-20000
    match destination-port 10000-20000
    match dscp cs4 
    match source-address ipv4 219.1.{}.0 255.255.255.0
    match destination-address ipv4 149.1.{}.0 255.255.255.0
    end-class-map
!
policy-map type pbr bgp_fs_v4
 class type traffic bgp_fs_v4_{}
  drop
 ! 
 class type traffic class-default 
 ! 
 end-policy-map
!
""".format(
        i, i, i, i
    )
    # print(config)

for i in range(2, 16):
    config_gre = """
interface Loopback{}
 ipv4 address 4.{}.1.1 255.255.255.255
 ipv6 address 2001:4::{}:1:1/128
!
interface tunnel-ip{}
 ipv4 address 192.1.{}.2 255.255.255.252
 ipv6 address 192:1:{}::2/64
 tunnel ttl 64
 tunnel mode gre ipv4 encap
 tunnel source 4.{}.1.1
 tunnel destination 1.2.1.1
!

""".format(
        i, i, i, i, i, i, i
    )
    # print(config_gre)

st = "biden is elected president"
vowels = []
st = st.split(" ")
su = 0
for i in st:
    for j in i:
        if j in vowels:
            c = c + 1

    if c % 2 == 0:
        su = su + 2
    else:
        su = su + 1


def count_vowels(words):
    b = 0
    for i in words:
        a = (
            i.count("a")
            + i.count("e")
            + i.count("i")
            + i.count("o")
            + i.count("u")
            + i.count("y")
        )
        if a % 2 == 0:
            b = b + 2
        else:
            b = b + 1
    return b
