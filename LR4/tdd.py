import unittest
import FabricMethod, AdapterPattern

class TestStringMethods(unittest.TestCase):

    def testFabric1(self):
        returned = FabricMethod.clientCode1(FabricMethod.AutoManufacturer())[1][1]
        self.assertEqual(returned, "ездиет")

    def testFabric2(self):
        returned = FabricMethod.clientCode1(FabricMethod.PlaneManufacturer())[1][0]
        self.assertEqual(returned, "Dreamweawer770")

    def testAdapter1(self):
        adapter = AdapterPattern.BinPresenter(127)
        returned = AdapterPattern.clientCode2(adapter)
        self.assertEqual(returned, "1111111")

    def testAdapter2(self):
        adapter = AdapterPattern.BinPresenter(1024)
        returned = AdapterPattern.clientCode2(adapter)
        self.assertEqual(returned, "10000000000")

if __name__ == '__main__':
    unittest.main()
