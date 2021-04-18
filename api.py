
#################################### {Netmiko} Get Command ####################################
# from nornir import InitNornir
# from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
# from nornir_utils.plugins.functions import print_result
#
# nornir = InitNornir('config.yaml')
# r2 = nornir.filter(name="P1")
#
#
# result = r2.run(netmiko_send_command, command_string="show ip int br")#
# print_result(result)

#################################### {Netmiko} push Command ####################################


# from nornir import InitNornir
# from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
# from nornir_utils.plugins.functions import print_result
#
# nornir = InitNornir('config.yaml')
#
# description = 'Description set with Nornir Netmiko'
#
# description_config = [
#     "interface loopback 0 ",
#     f"description {description}",
#     "commit",
# ]
#
# result = nornir.run(netmiko_send_config, config_commands=description_config)
# print_result(result)

#################################### {Napalam} Command ####################################

#
# from nornir import InitNornir
# from nornir_napalm.plugins.tasks import napalm_get, napalm_cli
# from nornir_utils.plugins.functions import print_result
#
# nornir = InitNornir('config.yaml')
#
# result = nornir.run(task=napalm_get, getters=["facts"])
# print_result(result)


#################################### {Scrapli} Command ####################################

# from nornir import InitNornir
# from nornir_scrapli.tasks import send_command
# from nornir_utils.plugins.functions import print_result
#
#
# nr = InitNornir(config_file="config.yaml")
# command_results = nr.run(task=send_command, command="show version")
#
# print_result(command_results)
