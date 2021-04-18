
####################################Get Command ####################################
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

####################################push Command ####################################


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

#################################### Napalam Command ####################################

#
# from nornir import InitNornir
# from nornir_napalm.plugins.tasks import napalm_get, napalm_cli
# from nornir_utils.plugins.functions import print_result
#
# nornir = InitNornir('config.yaml')
#
# result = nornir.run(task=napalm_get, getters=["facts"])
# print_result(result)


#################################### Scrapli Command ####################################

# from nornir import InitNornir
# from nornir_scrapli.tasks import send_command
# from nornir_utils.plugins.functions import print_result
#
#
# nr = InitNornir(config_file="config.yaml")
# command_results = nr.run(task=send_command, command="show version")
#
# print_result(command_results)



#################################### Structured Data  ####################################
"""nornir_scrapli.examples.structured_data.demo"""
from nornir_utils.plugins.functions import print_result

from nornir import InitNornir
from nornir_scrapli.functions import print_structured_result
from nornir_scrapli.tasks import send_command


def main() -> None:
    """Simple demo for printing structured data"""
    nr = InitNornir(config_file="config.yaml")
    r2 = nr.filter(name="P1")
    show_result = r2.run(task=send_command, command="show version")

    # we can print results w/ the "normal" print_result function, however with this method we have
    # no means to print the *structured* result (as parsed by textfsm/genie)
    # print_result(show_result)

    # if we wanted to print this result data out parsed with genie we can do so as follows:
    print_structured_result(result=show_result, parser="genie")

    # or if we preferred textfsm - note that `textfsm` is the default parser argument so we don't
    # actually need to pass that here):
#    print_structured_result(result=show_result, parser="textfsm")

    # if we had some kind of output that could *not* be parsed by the parser of our choice, the
    # printed output would be an empty list; if you would prefer to fallback to having the "raw"
    # string data printed if parsing fails, you can pass the `fail_to_string` argument:
#    print_structured_result(result=show_result, parser="textfsm", fail_to_string=True)

    # if you prefer to fetch/store/manipulate the structured data instead of simply printing it, you
    # can do so by accessing the underlying scrapli `Response` object... first to keep this easy to
    # read we can snag the specific host results out of the nornir `AggregateResult` object:
    # host_result = show_result["iosxe1"][0]

    # now we can see we've gotten the `Result` object -- or rather the `ScrapliResult` object from
    # the `AggregateResult`, and we can inspect that object to see what methods/attributes are
    # available to us
#    print(type(host_result))
#    print(dir(host_result))

    # in this case we can see there is a `scrapli_response` object which is the original/unmodified
    # response object from the underlying scrapli connection
#    print(type(host_result.scrapli_response))
#    print(dir(host_result.scrapli_response))

    # At this point we can simply work with that `scrapli_response` like we would a "normal" scrapli
    # response object:
    textfsm_results = show_result.scrapli_response.textfsm_parse_output()
    genie_results = show_result.scrapli_response.genie_parse_output()

    print("TEXTFSM RESULTS: \n", textfsm_results)
    print("GENIE RESULTS: \n", genie_results)


if __name__ == "__main__":
    main()