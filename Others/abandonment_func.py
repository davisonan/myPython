#! /usr/bin/env python

if __name__ != '__lib__':
    def outputSchema(dont_care):
        def wrapper(func):
            def inner(*args, **kwargs):
                return func(*args, **kwargs)
            return inner
        return wrapper

@outputSchema("record:{(query:chararray,type:chararray)}")
def get_abandonment(input):
    """This UDF marks every query session in a single timeout session as three types:
       a: abandonment
       r: retried
       c: clicked
       Abandonment rate should be (total number of type a) / (all uniq query sessions)"""

    if len(input) == 0:
        return [0,0,0,0];
    last_query = None
    query_tag_map = {}
    for line in input:
        if len(line)<5:
            continue
        (bcookie, session_id, query, noclick, event_type, ts) = line
        noclick = int(noclick)
        query = unicode(query)
        if query not in query_tag_map:
            if last_query is not None and query != last_query and query_tag_map[last_query] == 'a':
                query_tag_map[last_query]='r'
        if noclick != 1:
            query_tag_map[query]='c'
        else:
            if query not in query_tag_map:
                query_tag_map[query]='a'
        last_query = query

    return query_tag_map.items()

if __name__ == '__main__':
    # input schema is bcookie, session_id, query, noclick, event_type, ts
    in_data = [
        ['bcookie', '1', 'query a', 1, 'p', '12345'],
        ['bcookie', '1', 'query b', 0, 'p', '12345'],
        ['bcookie', '1', 'query c', 1, 'p', '12345'],
        ['bcookie', '1', 'query a', 1, 'p', '12345']
    ]

    print in_data
    print get_abandonment(in_data)
    # print abandonment_cnt(in_data)
