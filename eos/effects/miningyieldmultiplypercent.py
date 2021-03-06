# miningYieldMultiplyPercent
#
# Used by:
# Variations of module: Mining Laser Upgrade I (5 of 5)
# Module: Frostline 'Omnivore' Harvester Upgrade
type = "passive"


def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Mining"),
                                  "miningAmount", module.getModifiedItemAttr("miningAmountBonus"))
