#!/usr/bin/env python3

# Script name: Challenge: 401 Challenge 35
# Author: Christen Reinhart
# Date of Latest Revision: 02/23/2024
# Sources: https://chat.openai.com/share/6e1b9f2a-7a84-48c9-b383-7868058e48c9 
# Purpose: In Kali Linux, write your own .nse script

description = [[
    Gathers basic information about the target.
]]

author = "Your Name"

license = "Same as Nmap--See https://nmap.org/book/man-legal.html"

categories = {"discovery", "safe"}

require("stdnse")

-- Function to gather information
function gather_info(host)
    local target_ip = "192.168.2.109"  -- Set the target IP address

    local open_ports = {}

    for port = 1, 1025 do
        local socket = nmap.new_socket()
        socket:set_timeout(100)
        local status, err = socket:connect(host, port, "tcp")
        if status then
            table.insert(open_ports, port)
        end
        socket:close()
    end

    return {
        ['Target IP Address'] = target_ip,
        ['Open Ports'] = open_ports
    }
end

-- Register the script with Nmap
action = function(host)
    local info = gather_info(host)
    if type(info) == "table" then
        stdnse.print_output("Information about the target:")
        for key, value in pairs(info) do
            stdnse.print_output("%s: %s", key, value)
        end
    else
        return stdnse.format_output(false, info)
    end
end
