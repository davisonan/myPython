#! /usr/bin/env python

#if __name__ != '__lib__':
#    def outputSchema(dont_care):
#        def wrapper(func):
#            def inner(*args, **kwargs):
#                return func(*args, **kwargs)
#            return inner
#        return wrapper

@outputSchema("record:{(qtype:int,ts:int,srchid:chararray,ddb:chararray,query:chararray,fr2:chararray,nextquery:chararray,nextfr2:chararray,same:int)}")
def get_next(events):
	reform = None
	reform_fr2 = None
	same = 0
	result = []
	for event in events:
		(bcookie,tsid,qtype,timestamp,srchid,ddb,query,fr2) = event
		if reform is not None and reform == query:
			same=1
		else:
			same=0
		result.append((qtype,timestamp,srchid,ddb,query,fr2,reform,reform_fr2,same))
		reform=query
		reform_fr2=fr2
	return result
