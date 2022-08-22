def jsonify(state={}, headers={}, metadata={}, status=200):
    resource = {}
    resource.update(state)
    resource.update(metadata)
    return resource, status, headers

