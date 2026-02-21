def vehicle_roi(vehicle):
    revenue = 100000
    maintenance_cost = vehicle.servicelog_set.aggregate(models.Sum('cost'))['cost__sum'] or 0
    fuel_cost = vehicle.fuellog_set.aggregate(models.Sum('cost'))['cost__sum'] or 0

    acquisition_cost = 500000

    roi = (revenue - (maintenance_cost + fuel_cost)) / acquisition_cost
    return roi