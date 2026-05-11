from panos.firewall import Firewall
ike_profile.create()

# IPSEC PROFILE
ipsec_profile = IpsecCryptoProfile(
    name="IPSEC-PROFILE",
    esp_encryption=["3des"],
    esp_authentication=["sha1"],
    dh_group="group14"
)

fw.add(ipsec_profile)
ipsec_profile.create()

# TUNNEL INTERFACE
tunnel = TunnelInterface(
    name="tunnel.1",
    ip="169.255.1.2/30"
)

fw.add(tunnel)
tunnel.create()

# IKE GATEWAY
ike_gateway = IkeGateway(
    name="VPN-FORTIGATE",
    peer_ip_value="192.168.1.100",
    interface="ethernet1/1",
    psk="SenhaVPN@2026",
    version="ikev2",
    ikev2_crypto_profile="IKE-PROFILE"
)

fw.add(ike_gateway)
ike_gateway.create()

# IPSEC TUNNEL
ipsec_tunnel = IpsecTunnel(
    name="VPN-FORTIGATE",
    tunnel_interface="tunnel.1",
    ak_ike_gateway="VPN-FORTIGATE",
    ak_ipsec_crypto_profile="IPSEC-PROFILE"
)

fw.add(ipsec_tunnel)
ipsec_tunnel.create()

# STATIC ROUTE
vr = VirtualRouter("default")
fw.add(vr)

route = StaticRoute(
    name="TO-FORTIGATE",
    destination="192.168.10.0/24",
    interface="tunnel.1"
)

vr.add(route)
route.create()

print("Configuração enviada ao Palo Alto")