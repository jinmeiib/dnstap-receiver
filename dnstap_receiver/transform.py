import json
import yaml

def convert_dnstap(fmt, tapmsg):
    """convert dnstap message"""
    if fmt == "text":
        msg_list = []
        msg_list.append("%s" % tapmsg["timestamp"])
        msg_list.append("%s" % tapmsg["identity"])
        msg_list.append("%s" % tapmsg["message"])
        msg_list.append("%s" % tapmsg["code"]) 
        msg_list.append("%s" % tapmsg["source-ip"])
        msg_list.append("%s" % tapmsg["source-port"])
        msg_list.append("%s" % tapmsg["protocol"])
        msg_list.append("%s" % tapmsg["transport"])
        msg_list.append("%sb" % tapmsg["length"])
        msg_list.append("%s" % tapmsg["query-name"])
        msg_list.append("%s" % tapmsg["query-type"])
        
        msg = " ".join(msg_list)
        del msg_list
        return msg.encode()
        
    elif fmt == "json":
        msg = json.dumps(tapmsg)
        return msg.encode()
        
    elif fmt == "yaml":
        msg = yaml.dump(tapmsg)
        return msg.encode()
        
    else:
        return tapmsg
    