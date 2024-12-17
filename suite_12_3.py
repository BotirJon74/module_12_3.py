import unittest
import tests_12_3 as t

rt = unittest.TestSuite()
rt.addTest((unittest.TestLoader().loadTestsFromTestCase(t.RunnerTest)))
rt.addTest((unittest.TestLoader().loadTestsFromTestCase(t.TournamentTest)))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(rt)
