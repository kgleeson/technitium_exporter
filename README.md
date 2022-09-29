# technitium_exporter

A Prometheus exporter for Technitium written in Python 3 inspired by https://github.com/dr1s/pihole_exporter.py/

# Usage
	Technitium Prometheus Exporter [-h] [-a ADDRESS] [-p PORT] [-U USER] [-P PASSWORD] [-t TOKEN] [-w WEBSERVER_PORT]

	optional arguments:
	  -h, --help            show this help message and exit
	  -a ADDRESS, --address ADDRESS
	                        Technitium server address. e.g http://10.0.0.253
	  -p PORT, --port PORT  Technitium webui port
	  -U USER, --user USER  UI Username
	  -P PASSWORD, --password PASSWORD
	                        UI Password
	  -t TOKEN, --token TOKEN
	                        API Token
	  -w WEBSERVER_PORT, --webserver-port WEBSERVER_PORT
	                        Port used by the webserver


## Usage Examples

    technitium-exporter.py -a http://192.168.1.253 -p 5380 -U admin -P password -w 8888
or

    technitium-exporter.py -a http://192.168.1.253 -p 5380 -t 18e7c60cbccf4aca93d2778d313d2e6718e7c60cbccf4aca93d2778d313d2e67


# Available Metrics

* Top blocked domains
* Top allowed domains
* Top clients total requests
* Number of domain names listed in blocked zones
* Allowed zones allows to add exception to unblock domain names listed in blocked zones
* Number of blocked zones
* The total number of queries that were resolved using data available in the server's cache.
* The total number of queries that were resolved from the zones hosted locally on the DNS server.
* The total number of queries this DNS server blocked by responding with "0.0.0.0" (or "::" for AAAA) for A record request.
* The total number of queries that were resolved using data available in the server's cache.
* The total number of unique clients based on IP address of the queries.
* The total number of queries that were responded positively by the server.
* The server will try to resolve a domain name in the query and if the domain name does not exists, it will receive a NX Domain response code
* These are the total number of queries the DNS server has received from all clients.
* The total number of queries that were resolved partially or fully resolved by recursive resolution.
* The total number of queries this DNS server refused to resolve.
* The total number of queries that the server failed to respond positively.
* The total number of zones on the Technitium server

## Example
	  # HELP python_gc_objects_collected_total Objects collected during gc
	  # TYPE python_gc_objects_collected_total counter
	  python_gc_objects_collected_total{generation="0"} 795.0
	  python_gc_objects_collected_total{generation="1"} 247.0
	  python_gc_objects_collected_total{generation="2"} 0.0
	  # HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
	  # TYPE python_gc_objects_uncollectable_total counter
	  python_gc_objects_uncollectable_total{generation="0"} 0.0
	  python_gc_objects_uncollectable_total{generation="1"} 0.0
	  python_gc_objects_uncollectable_total{generation="2"} 0.0
	  # HELP python_gc_collections_total Number of times this generation was collected
	  # TYPE python_gc_collections_total counter
	  python_gc_collections_total{generation="0"} 96.0
	  python_gc_collections_total{generation="1"} 8.0
	  python_gc_collections_total{generation="2"} 0.0
	  # HELP python_info Python platform information
	  # TYPE python_info gauge
	  python_info{implementation="CPython",major="3",minor="9",patchlevel="2",version="3.9.2"} 1.0
	  # HELP technitium_top_blocked_domains Top blocked domains
	  # TYPE technitium_top_blocked_domains gauge
	  technitium_top_blocked_domains{domain="stats.grafana.org"} 2577.0
	  technitium_top_blocked_domains{domain="app-measurement.com"} 146.0
	  technitium_top_blocked_domains{domain="metrics.icloud.com"} 91.0
	  technitium_top_blocked_domains{domain="dit.whatsapp.net"} 41.0
	  technitium_top_blocked_domains{domain="googleads.g.doubleclick.net"} 40.0
	  technitium_top_blocked_domains{domain="region1.app-measurement.com"} 30.0
	  technitium_top_blocked_domains{domain="outcome-ssp.supersonicads.com"} 24.0
	  technitium_top_blocked_domains{domain="ads.api.vungle.com"} 20.0
	  technitium_top_blocked_domains{domain="api2.amplitude.com"} 19.0
	  technitium_top_blocked_domains{domain="rt.applovin.com"} 18.0
	  # HELP technitium_top_domains Top allowed domains
	  # TYPE technitium_top_domains gauge
	  technitium_top_domains{domain="discovery-v6.syncthing.net"} 4141.0
	  technitium_top_domains{domain="discovery-v4.syncthing.net"} 2636.0
	  technitium_top_domains{domain="log.tailscale.io"} 1500.0
	  technitium_top_domains{domain="discovery.syncthing.net"} 954.0
	  technitium_top_domains{domain="controlplane.tailscale.com"} 839.0
	  technitium_top_domains{domain="relays.syncthing.net"} 782.0
	  technitium_top_domains{domain="init-cdn.itunes-apple.com.akadns.net"} 769.0
	  technitium_top_domains{domain="iot.meross.com"} 611.0
	  # HELP technitium_top_clients Top clients total requests
	  # TYPE technitium_top_clients gauge
	  technitium_top_clients{host="192.168.1.111"} 512847.0
	  technitium_top_clients{host="192.168.1.200"} 42257.0
	  technitium_top_clients{host="192.168.1.107"} 13230.0
	  technitium_top_clients{host="192.168.1.201"} 9505.0
	  technitium_top_clients{host="192.168.1.130"} 6407.0
	  technitium_top_clients{host="192.168.1.119"} 5212.0
	  # HELP technitium_block_list_zones Number of domain names listed in blocked zones
	  # TYPE technitium_block_list_zones gauge
	  technitium_block_list_zones 1.265788e+06
	  # HELP technitium_allowed_zones Allowed zones allows to add exception to unblock domain names listed in blocked zones
	  # TYPE technitium_allowed_zones gauge
	  technitium_allowed_zones 0.0
	  # HELP technitium_blocked_zones Number of blocked zones
	  # TYPE technitium_blocked_zones gauge
	  technitium_blocked_zones 0.0
	  # HELP technitium_cached_entries The total number of queries that were resolved using data available in the server's cache.
	  # TYPE technitium_cached_entries gauge
	  technitium_cached_entries 10023.0
	  # HELP technitium_total_authoritative The total number of queries that were resolved from the zones hosted locally on the DNS server.
	  # TYPE technitium_total_authoritative gauge
	  technitium_total_authoritative 35077.0
	  # HELP technitium_total_blocked The total number of queries this DNS server blocked by responding with "0.0.0.0" (or "::" for AAAA) for A record 	  request.
	  # TYPE technitium_total_blocked gauge
	  technitium_total_blocked 3189.0
	  # HELP technitium_total_cached The total number of queries that were resolved using data available in the server's cache.
	  # TYPE technitium_total_cached gauge
	  technitium_total_cached 536147.0
	  # HELP technitium_total_clients The total number of unique clients based on IP address of the queries.
	  # TYPE technitium_total_clients gauge
	  technitium_total_clients 6.0
	  # HELP technitium_total_no_error The total number of queries that were responded positively by the server.
	  # TYPE technitium_total_no_error gauge
	  technitium_total_no_error 98499.0
	  # HELP technitium_total_nx_domain The server will try to resolve a domain name in the query and if the domain name does not exists, it will 	  receive a NX Domain response code which is also relayed as a response to the original query.
	  # TYPE technitium_total_nx_domain gauge
	  technitium_total_nx_domain 3987.0
	  # HELP technitium_total_queries These are the total number of queries the DNS server has received from all clients.
	  # TYPE technitium_total_queries gauge
	  technitium_total_queries 589458.0
	  # HELP technitium_total_recursive The total number of queries that were resolved partially or fully resolved by recursive resolution.
	  # TYPE technitium_total_recursive gauge
	  technitium_total_recursive 15045.0
	  # HELP technitium_total_refused The total number of queries this DNS server refused to resolve.
	  # TYPE technitium_total_refused gauge
	  technitium_total_refused 0.0
	  # HELP technitium_total_server_failure The total number of queries that the server failed to respond positively.
	  # TYPE technitium_total_server_failure gauge
	  technitium_total_server_failure 486821.0
	  # HELP technitium_zones The total number of zones on the Technitium server
	  # TYPE technitium_zones gauge
	  technitium_zones 7.0


# Licence
![GitHub](https://img.shields.io/github/license/kgleeson/technitium_exporter)
