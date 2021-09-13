from mdutils.mdutils import MdUtils
import json, copy

# parsing json
items = json.load(open("data.json"))["items"]

for item in items:
    for method in item["methods"]:
        preset = json.load(open("preset.json"))
        if method["response"] == "default":
            method["response"] = preset["response"][method["method"]]
            if method["method"] == "get":
                method["response"][0]["example"]["result"] = item["example"]
        if method["request"] == "default":

            preset = copy.deepcopy(preset["request"][method["method"]])
            if method["method"] in ["post", "patch"]:
                example = copy.deepcopy(item["example"])
                del example["_id"]
                for el in example:
                    if method["method"] == "post":
                        preset.append(
                            {
                                "name": el,
                                "type": "number"
                                if el in ["launch_time_utc"]
                                else "bool"
                                if el in ["insight"]
                                else "list"
                                if el in ["tags"]
                                else "string",
                                "in": "body",
                                "required": True,
                            },
                        )
                    else:
                        preset.append(
                            {
                                "name": el,
                                "type": "string",
                                "in": "body",
                                "required": False,
                            },
                        )
            method["request"] = preset

status_codes = json.load(open("preset.json"))["status"]

for el in items:
    mdFile = MdUtils(file_name=f"endpoints/{el['name']}")
    mdFile.new_header(level=1, title=f"**{el['name'].capitalize()}**\n")

    mdFile.write(el["description"] + "\n")

    for method in el["methods"]:
        mdFile.new_header(
            level=2,
            title=f"""<span class="{method['method']} method">{method['method']}</span> **{method['title']}**\n""",
        )
        if "description" in method:
            mdFile.write(method["description"] + "\n\n")

        if "endpoint" in method:
            mdFile.write(f"`https://api.solarnews.ga/v1/{method['endpoint']}`\n")
        else:
            if method["method"] in ["patch", "delete"]:
                mdFile.write(f"`https://api.solarnews.ga/v1/{el['name']}/:id`\n")
            else:
                mdFile.write(f"`https://api.solarnews.ga/v1/{el['name']}`\n")

        if len(method["request"]) > 0:
            table = ["name", "type", "in", "required"]
            for request in method["request"]:
                table.extend(
                    [
                        request["name"],
                        "`" + request["type"] + "`",
                        request["in"],
                        str(request["required"]),
                    ]
                )
            mdFile.new_table(
                columns=4,
                rows=len(method["request"]) + 1,
                text=table,
                text_align="center",
            )

        mdFile.write(f"\n<details>\n<summary>Response</summary>\n\n")
        for response in method["response"]:
            status = status_codes[str(response["status"])]
            mdFile.write(f'<span class="{status[0]} round"></span> **{status[1]}**')
            mdFile.insert_code(
                json.dumps(response["example"], indent=4, sort_keys=True), "json"
            )
            mdFile.write("\n")
        mdFile.write("\n\n</details>\n")

    mdFile.create_md_file()
