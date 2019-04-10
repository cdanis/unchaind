SELECT
it.typeID,
it.typeName,
ig.groupName
FROM invTypes it
LEFT JOIN invGroups ig ON it.groupID = ig.groupID
