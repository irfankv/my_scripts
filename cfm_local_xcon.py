for i in range(1002, 1101):
    j = 2000+i
    config_r1 = f"""
ethernet cfm
 domain irf1 level 6 id null
  service up-mep-{i} xconnect group xcon p2p {i} id number {i}
  mip auto-create all ccm-learning
  continuity-check interval 10s  loss-threshold 3
   continuity-check archive hold-time 100
   mep crosscheck
    mep-id {i}
   !
   ais transmission interval 1m cos 6
   log ais
   log continuity-check errors
   log crosscheck errors
   log continuity-check mep changes
  !
 
interface TenGigE0/4/0/7.{i} l2transport
encapsulation dot1q {i} second-dot1q 2501
ethernet cfm
  mep domain irf1 service up-mep-{i} mep-id {j}
  !
!
!
 
interface Te0/5/0/2.{i} l2transport
encapsulation dot1q {i} second-dot1q 2501
l2vpn
xconnect group xcon
  p2p {i}
   interface TenGigE0/4/0/7.{i}
   interface TenGigE0/5/0/2.{i}
  !
    """
    # print(config_r1)

    config_r2 = f"""
ethernet cfm
 domain irf1 level 6 id null
  service up-mep-{i} xconnect group xcon p2p {i} id number {i}
  mip auto-create all ccm-learning
  continuity-check interval 10s  loss-threshold 3
   continuity-check archive hold-time 100
   mep crosscheck
    mep-id {j}
   !
   ais transmission interval 1m cos 6
   log ais
   log continuity-check errors
   log crosscheck errors
   log continuity-check mep changes
  !
 
interface TenGigE0/6/0/2/2.{i} l2transport
encapsulation dot1q {i} second-dot1q 2501
ethernet cfm
  mep domain irf1 service up-mep-{i} mep-id {i}
  !
!
!
 
interface TenGigE0/7/0/8/1.{i} l2transport
encapsulation dot1q {i} second-dot1q 2501
l2vpn
xconnect group xcon
  p2p {i}
   interface TenGigE0/6/0/2/2.{i}
   interface TenGigE0/7/0/8/1.{i}
  !
    """
    print(config_r2)
