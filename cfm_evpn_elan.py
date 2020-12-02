for i in range(1001, 1002):  # make it from 1 to 1000
    #print("======= Frett Fretta========")
    mep_id1 = 1000+int(i)
    mep_id2 = 2000+int(i)
    mep_id3 = 4000+int(i)
    id_num = 3000+int(i)
    cfm_fretta = """
ethernet cfm
domain irf_evpn_up level 4 id null
  service up_mep_evpn_%s bridge group evpn_%s bridge-domain evpn_bd_%s id icc-based LE XXX-08%s
   continuity-check interval  10s loss-threshold 3
   continuity-check archive hold-time 10
   mep crosscheck
               mep-id %s
               mep-id %s
   !
   ais transmission interval 1m cos 6
   log ais
   log continuity-check errors
   log crosscheck errors
   log continuity-check mep changes
  !
root
interface Te0/6/0/2/2.%s l2transport
encapsulation dot1q %s second-dot1q 2000
ethernet cfm
  mep domain irf_evpn_up service up_mep_evpn_%s mep-id %s
  cos 3
  !
!
!
l2vpn
bridge group evpn_%s
  bridge-domain evpn_bd_%s
   interface Te0/6/0/2/2.%s
   !
   evi %s
 
evpn
evi %s
  bgp
   route-target import 200:%s
   route-target export 100:%s
   route-target import 400:%s
  !
  advertise-mac
  !
!
!
    """ % (i, i, i, id_num, mep_id2, mep_id3, i, i, i, mep_id1, i, i, i, i, i, i, i, i)
    #print("======= PE1========")
    print(cfm_fretta)  # comment here
    #print("======= PE2========")
    cfm_PE2 = """
ethernet cfm
domain irf_evpn_up level 4 id null
  service up_mep_evpn_%s bridge group evpn_%s bridge-domain evpn_bd_%s id icc-based LE XXX-08%s
   continuity-check interval  10s loss-threshold 3
   continuity-check archive hold-time 10
   mep crosscheck
               mep-id %s
               mep-id %s
   !
   ais transmission interval 1m cos 6
   log ais
   log continuity-check errors
   log crosscheck errors
  log continuity-check mep changes
  !
root
interface TenGigE0/4/0/7.%s l2transport
encapsulation dot1q %s second-dot1q 2000
ethernet cfm
  mep domain irf_evpn_up service up_mep_evpn_%s mep-id %s
  cos 3
  !
!
!
l2vpn
bridge group evpn_%s
  bridge-domain evpn_bd_%s
   interface TenGigE0/4/0/7.%s
   !
   evi %s
 
evpn
evi %s
  bgp
   route-target import 100:%s
   route-target export 200:%s
   route-target import 400:%s
  !
  advertise-mac
  !
!
!
    """ % (i, i, i, id_num, mep_id1, mep_id3, i, i, i, mep_id2, i, i, i, i, i, i, i, i)
    print(cfm_PE2)
    #print("======= Frett Fretta========")
    mep_id = 3000+int(i)
    id_num = 3000+int(i)
    cfm_PE3 = """
ethernet cfm
domain irf_evpn_up level 4 id null
  service up_mep_evpn_%s bridge group evpn_%s bridge-domain evpn_bd_%s id icc-based LE XXX-08%s
   continuity-check interval  10s loss-threshold 3
   continuity-check archive hold-time 10
   mep crosscheck
               mep-id %s
               mep-id %s
   !
   ais transmission interval 1m cos 6
   log ais
   log continuity-check errors
   log crosscheck errors
   log continuity-check mep changes
  !
root
interface TenGigE0/0/0/4.%s l2transport
encapsulation dot1q %s second-dot1q 2000
ethernet cfm
  mep domain irf_evpn_up service up_mep_evpn_%s mep-id %s
  cos 3
  !
!
!
l2vpn
bridge group evpn_%s
  bridge-domain evpn_bd_%s
   interface TenGigE0/0/0/4.%s
   !
   evi %s
 
evpn
evi %s
  bgp
   route-target import 100:%s
   route-target export 400:%s
   route-target import 200:%s
  !
  advertise-mac
  !
!
!
    """ % (i, i, i, id_num, mep_id1, mep_id2, i, i, i, mep_id3, i, i, i, i, i, i, i, i)
    #print("======= PE3========")
    # print(cfm_PE3)
