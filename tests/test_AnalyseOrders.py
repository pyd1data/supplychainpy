import os
import unittest
from decimal import Decimal
from unittest import TestCase

from supplychainpy import model_inventory
from supplychainpy.demand import analyse_uncertain_demand
from supplychainpy.demand.analyse_uncertain_demand import UncertainDemand


class TestAnalyseOrders(TestCase):
    def setUp(self):
        self._data_set = {'jan': 25, 'feb': 25, 'mar': 25, 'apr': 25, 'may': 25, 'jun': 25, 'jul': 75,
                          'aug': 75, 'sep': 75, 'oct': 75, 'nov': 75, 'dec': 75}

        app_dir = os.path.dirname(__file__, )
        rel_path = 'supplychainpy/data2.csv'
        abs_file_path = os.path.abspath(os.path.join(app_dir, '..', rel_path))

        self._orders_analysis = model_inventory.analyse_orders_abcxyz_from_file(file_path=abs_file_path,
                                                                                z_value=Decimal(1.28),
                                                                                reorder_cost=Decimal(5000),
                                                                                file_type="csv",
                                                                                length=12)

        self._uncertain_demand = analyse_uncertain_demand.UncertainDemand(self._data_set, sku='Rx493-90',
                                                                          lead_time=Decimal(4),
                                                                          reorder_cost=Decimal(450),
                                                                          z_value=Decimal(1.28),
                                                                          holding_cost=Decimal(0.25),
                                                                          retail_price=Decimal(400.58),
                                                                          unit_cost=Decimal(55))

    def test_orders_type(self):
        self.assertIsInstance(self._orders_analysis.orders, list)

    def test_order_list_type(self):
        for order in self._orders_analysis.orders:
            self.assertIsInstance(order, UncertainDemand)

    def test_safety_stock(self):
        print(self.







              _uncertain_demand.safety_stock)



    def test_is_average(self):
        # act

        d = analyse_uncertain_demand.UncertainDemand(self._data_set, sku='Rx493-90', lead_time=Decimal(4),
                                                     reorder_cost=Decimal(450), z_value=Decimal(1.28),
                                                     holding_cost=Decimal(0.25), retail_price=Decimal(4.58),
                                                     unit_cost=Decimal(55))
        a = Decimal(d.average_orders)
        # assert
        self.assertEqual(a, 50)

    def test_order_constraint(self):
        # arrange
        orders_placed = [25, 25, 25]  # less than five demand are specified
        # act
        # assert
        with self.assertRaises(AttributeError):
            analyse_uncertain_demand.UncertainDemand(orders=orders_placed, sku='Rx493-90', lead_time=Decimal(4),
                                                     unit_cost=Decimal(40), reorder_cost=Decimal(400),
                                                     retail_price=Decimal(600))

    def test_standard_deviation(self):
        # arrange
        # act
        d = analyse_uncertain_demand.UncertainDemand(self._data_set, sku='Rx493-90', lead_time=Decimal(4),
                                                     reorder_cost=Decimal(450), z_value=Decimal(1.28),
                                                     holding_cost=Decimal(0.25), retail_price=Decimal(4.58),
                                                     unit_cost=Decimal(55))
        a = d.standard_deviation
        # assert
        self.assertEqual(a, 25)


if __name__ == '__main__':
    unittest.main()
