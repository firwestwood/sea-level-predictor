import unittest
import sea_level_predictor
import matplotlib.pyplot as plt

class SeaLevelPredictorTestCase(unittest.TestCase):
    def test_plot(self):
        fig = sea_level_predictor.draw_plot()
        self.assertTrue(isinstance(fig, plt.Figure))

if __name__ == "__main__":
    unittest.main()
