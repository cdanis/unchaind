SELECT
md.itemId,
md.itemName,
md.security,
mlr.wormholeClassID
FROM mapDenormalize md
LEFT JOIN mapLocationWormholeClasses mlr ON mlr.locationID = md.regionID
WHERE typeID=5 AND groupID=5;
