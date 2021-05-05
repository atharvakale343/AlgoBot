from StockDataExtraction.StockData import SingleStockData
from IndicatorClasses.AccumulationDistribution import AccumulationDistribution
from IndicatorClasses.Aroon import Aroon
from IndicatorClasses.AverageTrueRange import AverageTrueRange
from IndicatorClasses.BalanceOfPower import BalanceOfPower
from IndicatorClasses.BollingerEMA import BollingerEMA
from IndicatorClasses.BollingerSMA import BollingerSMA
from IndicatorClasses.ChakinOscillator import ChaikinOscillator
from IndicatorClasses.ChoppinessIndex import ChoppinessIndex
from IndicatorClasses.CommodityChannelIndex import CommodityChannelIndex
from IndicatorClasses.ConnorsRSI import ConnorsRSI
from IndicatorClasses.CoppockCurve import CoppockCurve
from IndicatorClasses.CumulativeVolume import CumulativeVolume
from IndicatorClasses.DetrendedPriceOscillator import DetrendedPriceOscillator
from IndicatorClasses.DirectionalMovement import DirectionalMovement
from IndicatorClasses.DonchianChannels import DonchianChannels
from IndicatorClasses.EaseOfMovement import EaseOfMovement
from IndicatorClasses.EldersForce import EldersForce
from IndicatorClasses.EnvelopeEMA import EnvelopeEMA
from IndicatorClasses.EnvelopeSMA import EnvelopeSMA
from IndicatorClasses.ExponentialMovingAverage import ExponentialMovingAverage
from IndicatorClasses.SimpleMovingAverage import SimpleMovingAverage
from IndicatorClasses.FisherTransform import FisherTransform
from IndicatorClasses.FisherTransformReversal import FisherTransformReversal
from IndicatorClasses.McGinleyDynamic import McGinleyDynamic
from IndicatorClasses.HistoricalVolatility import HistoricalVolatility
from IndicatorClasses.KeltnerChannel import KeltnerChannel
from IndicatorClasses.LinearRegression import LinearRegression
from IndicatorClasses.LocalVolatility import LocalVolatility
from IndicatorClasses.MassIndex import MassIndex
from IndicatorClasses.MomentumOscillator import MomentumOscillator
from IndicatorClasses.MomentumOscillatorReversal import MomentumOscillatorReversal
from IndicatorClasses.MoneyFlowReversal import MoneyFlowReversal
from IndicatorClasses.MovingAverageConvergenceDivergence import MovingAverageConvergenceDivergence
from IndicatorClasses.OnBalanceVolume import OnBalanceVolume
from IndicatorClasses.PivotPoint import PivotPoint
from IndicatorClasses.PriceVolumeTrend import PriceVolumeTrend
from IndicatorClasses.PriceVolumeTrendReversal import PriceVolumeTrendReversal
from IndicatorClasses.RateOfChange import RateOfChange
from IndicatorClasses.RelativeStrengthIndex import RelativeStrengthIndex
from IndicatorClasses.SimpleMovingAverageOscillator import SimpleMovingAverageOscillator
from IndicatorClasses.SMIErgodic import SMIErgodic
from IndicatorClasses.StochasticOscillator import StochasticOscillator
from IndicatorClasses.WeightedMovingAverage import WeightedMovingAverage
from IndicatorClasses.StochasticOscillatorReversal import StochasticOscillatorReversal
from IndicatorClasses.TRIX import TRIX
from IndicatorClasses.TrueStrengthIndicator import TrueStrengthIndicator

stock_data = SingleStockData(4,True, 200)
stock_data.generate_dataframe()

obj = TrueStrengthIndicator(dataframe_input = stock_data.df, lookback_period = 5)
x,y = obj.run(3)
print(x)
print(y)

