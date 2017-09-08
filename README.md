# cqrs-python-demo
For research purposes only. Learn from our experiments :) but, it is generally an attempt to do the following:

# working CQRS system
# event sourced
# view model
# commands
# single REST api (for convenience)

## The Stack

Since we're considering event-sourcing and CQRS for our own techstack, I wanted to try it out first hand, using some pre-made event-source offering.
The focus was to get a practical feel of a CQRS implementation, and the possible issues with event-sourcing.

# Event Sourcing https://geteventstore.com
# Event Store Client https://github.com/madedotcom/atomicpuppy
# REST API http://flask.pocoo.org
# View Models https://www.postgresql.org

### Event-Store Options

* https://geteventstore.com (C#, .NET, and plenty of community adapterS)
* http://eventuate.io (java)
* https://github.com/johnbywater/eventsourcing (Python)

### What is CQRS?

CQRS stands for Command Query Responsibility Segregation

https://martinfowler.com/bliki/CQRS.html

*Learn more about CQRS*

If you're new to microservices or command-query-responsibility-segregation checkout some of these resources which I found particularily useful.

* "When Microservices Meet Event Sourcing" https://www.youtube.com/watch?v=cISNDnwlSgw
* "Developing microservices with aggregates - Chris Richardson" https://www.youtube.com/watch?v=7kX3fs0pWwc
* "Event Sourcing in practice" https://ookami86.github.io/event-sourcing-in-practice/
* Eventually Consistent Distributed Systems with Node.js for Finance - Stefan Kutko of Electronifie https://www.youtube.com/watch?v=X_VHWQa1k0k
* Dealing with CQRS issues http://danielwhittaker.me/2015/02/02/upgrade-cqrs-events-without-busting/
* Principles Of Microservices by Sam Newman https://www.youtube.com/watch?v=PFQnNFe27kU
