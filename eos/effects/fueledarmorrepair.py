# fueledArmorRepair
#
# Used by:
# Modules from group: Ancillary Armor Repairer (7 of 7)
runTime = "late"
type = "active"


def handler(fit, module, context):
    if module.charge and module.charge.name == "Nanite Repair Paste":
        multiplier = 3
    else:
        multiplier = 1

    amount = module.getModifiedItemAttr("armorDamageAmount") * multiplier
    speed = module.getModifiedItemAttr("duration") / 1000.0
    rps = amount / speed
    fit.extraAttributes.increase("armorRepair", rps)
    fit.extraAttributes.increase("armorRepairPreSpool", rps)
    fit.extraAttributes.increase("armorRepairFullSpool", rps)
