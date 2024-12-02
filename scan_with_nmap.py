import nmap3
import json

host_for_scan = '127.0.0.1'
# host_for_scan = '192.168.100.1'
# host_for_scan = '86.57.251.89'

nmap_obj = nmap3.Nmap()
print("[*] Scanning...\n")
results = nmap_obj.nmap_list_scan(host_for_scan)
# print(results)

# with open('data.txt', 'w') as file_txt:
#     json.dump(results, file_txt)

print(f"{results['runtime']['summary']} \n"
      f"equivalent command: {results['stats']['args']} \n")

print(f"name_host: {results[list(results.keys())[0]]['hostname'][0]['name']} \n"
      f"ipv4: {next(iter(results))}, mac: {results[list(results.keys())[0]]['macaddress']} \n")

print("=" * 100)

print("[*] Scanning ports...\n")
results2 = nmap_obj.nmap_subnet_scan(host_for_scan)
results2_json = (json.dumps(results2, indent=4)) # Serializing json
# print(results2_json)

print(f"{results2['runtime']['summary']} \n"
      f"equivalent command: {results2['stats']['args']} \n")

# with open('data.json', 'w') as file_json: # Writing to .json
#     file_json.write(results2_json)

ports_open = results2[list(results.keys())[0]]['ports']


for port in ports_open:
      print(f"port: {port['portid']:{8}} state: {port['state']:{8}} reason: {port['reason']}")

print(f"\n{results2['task_results'][0]['extrainfo']} scanning complete \n")