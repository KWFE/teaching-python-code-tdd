class WeightCheck:

    @staticmethod
    def check_invalid_add(container, thing):
        return (container.total_weight() + thing.get_weight() > container.max_weight())
