Events
######

``unchaind`` notifiers support various types of events. Each event type has its
own set of filters.

kill
====
One of the most common events. When any notifiers that subscribe to the kill
event are configured ``unchaind`` will keep track of the live feed of
zkillboard_ kills and try to match them with your filter configuration. If a
killmail is matched it will be posted to the notifiers' output.

example
-------
Kill supports a slew of filters. Let's start with an example configuration for
a kill notifier:::

  [[notifier]]
      type = "discord"
      webhook = "hook_url"
      subscribes_to = "kill"
  
      [notifier.filter]
          [notifier.filter.require_all_of]
              alliance = [99999999]
              minimum_value = [500000000]
              location = ["chain"]
          [notifier.filter.exclude_if_any]
              alliance_loss = [99999998]

filters
-------
The following filters are supported by the kill event type:

location
^^^^^^^^
The ``location`` filter uses the system id where the kill took place to filter
results.

alliance
^^^^^^^^
The ``alliance`` filter looks if the supplied alliance id is on either the
attacker or loss side of the killmail.

alliance_kill
^^^^^^^^^^^^^
The ``alliance_kill`` filter looks if the supplied alliance id is on the 
attacker side of the killmail.

alliance_loss
^^^^^^^^^^^^^
The ``alliance_loss`` filter looks if the supplied alliance id is on the 
losing side of the lossmail.

corporation
^^^^^^^^^^^
The ``corporation`` filter looks if the supplied corporation id is on either the
attacker or loss side of the killmail.

corporation_kill
^^^^^^^^^^^^^^^^
The ``corporation_kill`` filter looks if the supplied corporation id is on the 
attacker side of the killmail.

corporation_loss
^^^^^^^^^^^^^^^^
The ``corporation_loss`` filter looks if the supplied corporation id is on the 
losing side of the lossmail.

character
^^^^^^^^^
The ``character`` filter looks if the supplied character id is on either the
attacker or loss side of the killmail.

character_kill
^^^^^^^^^^^^^^
The ``character_kill`` filter looks if the supplied character id is on the 
attacker side of the killmail.

character_loss
^^^^^^^^^^^^^^
The ``character_loss`` filter looks if the supplied character id is on the 
losing side of the lossmail.

minimum_value
^^^^^^^^^^^^^
The ``minimum_value`` filter uses the minimum value of the killmail to filter
on.

security
^^^^^^^^
The ``security`` filter uses the security status of the system to include or
exclude killmails.

system_class
^^^^^^^^
The ``system_class`` filter uses class of the system to include or
exclude killmails.

System classes are defined as follows:
- 1-6: C1-C6 (Wormholes)
- 7: low/high
- 9: null
- 10-11: part of Jove space
- 12: Thera
- 13: C13s (Wormholes)
- 14-18: weird drifter storyline holes, one per region
- 19-23: abyssal space
- 24: idk some weird P-001 space

system_name
^^^^^^^^
The ``system_name`` filter uses the name of the system to include or
exclude killmails.

Ex: Jita

ship_class
^^^^^^^^
The ``ship_class`` filter uses class of the ship killed to include or
exclude killmails.

Ex: Frigate

ship_name
^^^^^^^^
The ``ship_name`` filter uses the name of the ship killed to include or
exclude killmails.

Ex: Bantam

system
======
The system filter runs for new systems being added to the map, for example
a system that was added to one of the mappers that you have configured.

filters
-------
There are no filters yet for the system event. If you configure it a message
will be sent to the configured webhook for every new system found.::

  [[notifier]]
      type = "system"
      webhook = "hook_url"
      subscribes_to = "system"


.. _zkillboard: https://www.zkillboard.com
