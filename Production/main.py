from StockDataExtraction.StockData import SingleStockData
from IndicatorClasses.TradingRange import TradingRange
import yfinance as yf
from StockDataExtraction.StockData import BasketStockData
from Engines.Engine1 import Engine1
from Engines.Engine2 import Engine2
from StockDataExtraction.yfinanceDataPull import extract
import time
import sys


def main():
    #list_stok = ['AAPL', 'MSFT', 'ETSY', 'AMZN', 'FB', 'GOOGL', 'GOOG', 'TSLA', 'JPM', 'JNJ', 'V', 'UNH', 'HD', 'NVDA', 'PG', 'DIS', 'MA', 'BAC', 'PYPL', 'XOM', 'CMCSA', 'VZ', 'INTC', 'ADBE', 'T', 'CSCO', 'NFLX', 'PFE', 'KO', 'ABT', 'CVX', 'ABBV', 'PEP', 'CRM', 'MRK', 'WMT', 'WFC', 'TMO', 'ACN', 'AVGO', 'MCD', 'MDT', 'NKE', 'TXN', 'COST', 'DHR', 'HON', 'C', 'LIN', 'QCOM', 'UPS', 'LLY', 'UNP', 'PM', 'LOW', 'ORCL', 'AMGN', 'NEE', 'BMY', 'SBUX', 'IBM', 'MS', 'CAT', 'RTX', 'BA', 'GS', 'BLK', 'DE', 'AMAT', 'MMM', 'GE', 'CVS', 'AMT', 'INTU', 'SCHW', 'TGT', 'AXP', 'ISRG', 'CHTR', 'LMT', 'NOW', 'ANTM', 'MU', 'FIS', 'AMD', 'SPGI', 'BKNG', 'MO', 'CI', 'LRCX', 'MDLZ', 'TJX', 'PLD', 'PNC', 'USB', 'GILD', 'ADP', 'SYK', 'TFC', 'TMUS', 'ZTS', 'CSX', 'CCI', 'CB', 'DUK', 'FDX', 'COP', 'GM', 'CME', 'NSC', 'ATVI', 'COF', 'FISV', 'MMC', 'BDX', 'CL', 'SO', 'SHW', 'ITW', 'EL', 'APD', 'ICE', 'D', 'ADSK', 'EQIX', 'FCX', 'PGR', 'BSX', 'HUM', 'GPN', 'ETN', 'AON', 'NOC', 'ADI', 'EW', 'ECL', 'EMR', 'HCA', 'VRTX', 'WM', 'ILMN', 'NEM', 'DG', 'NXPI', 'MCO', 'REGN', 'DOW', 'MET', 'KLAC', 'ROP', 'JCI', 'KMB', 'ROST', 'F', 'IDXX', 'EOG', 'TEL', 'GD', 'LHX', 'IQV', 'BAX', 'DD', 'HPQ', 'AEP', 'SYY', 'EXC', 'AIG', 'TT', 'SLB', 'TWTR', 'TROW', 'PPG', 'ALGN', 'DLR', 'PRU', 'PSA', 'BK', 'BIIB', 'SRE', 'STZ', 'PH', 'EA', 'TRV', 'SPG', 'A', 'ALL', 'APH', 'INFO', 'CTSH', 'CMG', 'MCHP', 'ORLY', 'CMI', 'MSCI', 'WBA', 'GIS', 'MPC', 'APTV', 'EBAY', 'MAR', 'CNC', 'XEL', 'PSX', 'ALXN', 'ADM', 'IFF', 'YUM', 'SNPS', 'DFS', 'CARR', 'CTVA', 'ZBH', 'AFL', 'LUV', 'CDNS', 'MNST', 'GLW', 'SWK', 'WLTW', 'DXCM', 'KMI', 'DHI', 'PXD', 'HLT', 'AZO', 'VLO', 'TDG', 'FRC', 'PAYX', 'PCAR', 'OTIS', 'SBAC', 'MSI', 'PEG', 'AME', 'ROK', 'CTAS', 'WEC', 'AMP', 'STT', 'WELL', 'MTD', 'FAST', 'WMB', 'SIVB', 'XLNX', 'FITB', 'BLL', 'MCK', 'LYB', 'WY', 'LEN', 'SWKS', 'ES', 'EFX', 'AJG', 'ANSS', 'VFC', 'KR', 'DAL', 'CBRE', 'NUE', 'VRSK', 'RMD', 'FTNT', 'KHC', 'AWK', 'BBY', 'DTE', 'DLTR', 'LH', 'AVB', 'KSU', 'ED', 'KEYS', 'MXIM', 'CPRT', 'ODFL', 'VMC', 'EQR', 'O', 'ZBRA', 'NTRS', 'URI', 'HSY', 'FTV', 'WST', 'SYF', 'CDW', 'IP', 'HIG', 'FLT', 'OKE', 'RSG', 'CLX', 'MLM', 'TSN', 'CERN', 'TSCO', 'EXPE', 'MKC', 'ARE', 'VIAC', 'EIX', 'OXY', 'VRSN', 'HES', 'PPL', 'KEY', 'DOV', 'RF', 'CHD', 'ETR', 'XYL', 'WDC', 'CZR', 'HPE', 'AEE', 'KMX', 'GRMN', 'TER', 'QRVO', 'MTB', 'CFG', 'CCL', 'IT', 'FE', 'VTR', 'GWW', 'GNRC', 'COO', 'HAL', 'ETSY', 'EXPD', 'AMCR', 'TTWO', 'CE', 'WAT', 'GPC', 'BR', 'TRMB', 'TFX', 'EXR', 'NDAQ', 'LVS', 'CAG', 'CMS', 'ESS', 'DRI', 'DGX', 'IR', 'AVY', 'OMC', 'STX', 'PEAK', 'J', 'AKAM', 'STE', 'CINF', 'ANET', 'ULTA', 'MAA', 'ALB', 'NVR', 'RCL', 'CTLT', 'POOL', 'ABC', 'NTAP', 'K', 'IEX', 'DRE', 'AES', 'MAS', 'UAL', 'PFG', 'EMN', 'BKR', 'VTRS', 'HOLX', 'RJF', 'DPZ', 'MKTX', 'CAH', 'TYL', 'PHM', 'TDY', 'PAYC', 'HBAN', 'MGM', 'WRK', 'WHR', 'INCY', 'PKI', 'LB', 'ENPH', 'TXT', 'BXP', 'FBHS', 'FMC', 'SJM', 'DVN', 'CTXS', 'FANG', 'XRAY', 'JBHT', 'PKG', 'WAB', 'EVRG', 'MPWR', 'LNT', 'LDOS', 'PTC', 'LKQ', 'PWR', 'UDR', 'SNA', 'AAP', 'ABMD', 'CNP', 'HRL', 'MHK', 'LUMN', 'L', 'AAL', 'CHRW', 'ATO', 'TPR', 'BIO', 'WYNN', 'IPG', 'ALLE', 'HAS', 'HWM', 'FOXA', 'BWA', 'PENN', 'LNC', 'MOS', 'NLOK', 'HST', 'JKHY', 'UHS', 'IRM', 'CBOE', 'DISH', 'LW', 'HSIC', 'WRB', 'FFIV', 'TAP', 'PNR', 'CF', 'NWL', 'RE', 'CMA', 'LYV', 'IVZ', 'WU', 'NWSA', 'CPB', 'RHI', 'REG', 'NCLH', 'GL', 'NI', 'ZION', 'AOS', 'PNW', 'NLSN', 'AIZ', 'BEN', 'DISCK', 'MRO', 'KIM', 'DVA', 'JNPR', 'SEE', 'HII', 'DXC', 'NRG', 'ALK', 'ROL', 'PVH', 'APA', 'PBCT', 'FRT', 'FLIR', 'HBI', 'LEG', 'VNO', 'GPS', 'IPGP', 'COG', 'RL', 'NOV', 'UNM', 'DISCA']
    list_stok = ['ADANIPORTS.NS', 'APEX.NS', 'SRF.NS', 'JMFINANCIL.NS', 'SBICARD.NS', 'VIDHIING.NS', 'ASTRAL.NS', 'PGHH.NS', 'FIEMIND.NS', 'BATAINDIA.NS', 'SUNCLAYLTD.NS', 'NETWORK18.NS', 'CGCL.NS', 'BFUTILITIE.NS', 'CENTURYTEX.NS', 'INDIACEM.NS', 'MMP.NS', 'SOMANYCERA.NS', 'HATSUN.NS', 'MAYURUNIQ.NS', 'KRBL.NS', 'KINGFA.NS', 'NRAIL.NS', 'NAVINFLUOR.NS', 'DCBBANK.NS', 'KOKUYOCMLN.NS', 'ZUARI.NS', 'GALAXYSURF.NS', 'KICL.NS', 'IOB.NS', 'ASTRAZEN.NS', 'ITDC.NS', 'CHEMFAB.NS', 'HMT.NS', 'TCS.NS', 'DIVISLAB.NS', 'MAJESCO.NS', 'QUESS.NS', 'DWARKESH.NS', 'BHEL.NS', 'PRAJIND.NS', 'GKWLIMITED.NS', 'MPHASIS.NS', 'KUANTUM.NS', 'FSL.NS', 'POLYCAB.NS', 'GRSE.NS', 'WHEELS.NS', 'TVTODAY.NS', 'INDIAGLYCO.NS', 'IGARASHI.NS', 'PNBGILTS.NS', 'AHLWEST.NS', 'DRREDDY.NS', 'SOLARA.NS', 'KSL.NS', 'RELAXO.NS', 'PETRONET.NS', 'HINDALCO.NS', 'ITDCEM.NS', 'MAHSCOOTER.NS', 'GMBREW.NS', 'RBL.NS', 'MSPL.NS', 'CAPLIPOINT.NS', 'NRBBEARING.NS', 'EIHAHOTELS.NS', 'SWARAJENG.NS', 'MEGH.NS', 'COLPAL.NS', 'NIPPOBATRY.NS', 'ASTRAMICRO.NS', 'AMBIKCO.NS', 'OLECTRA.NS', 'LTI.NS', 'SANGHIIND.NS', 'SPIC.NS', 'RANEHOLDIN.NS', 'WSTCSTPAPR.NS', 'BRIGADE.NS', 'HDFCBANK.NS', 'HCG.NS', 'BEPL.NS', 'ENGINERSIN.NS', 'NBIFIN.NS', 'GREAVESCOT.NS', 'BORORENEW.NS', 'JAICORPLTD.NS', 'PRABHAT.NS', 'MAITHANALL.NS', 'RALLIS.NS', 'POWERGRID.NS', 'COCHINSHIP.NS', 'KIRLOSENG.NS', 'SHARDAMOTR.NS', 'SUPRAJIT.NS', 'MCL.NS', 'DFMFOODS.NS', 'FLFL.NS', 'MPSLTD.NS', 'TIRUMALCHM.NS', 'JBCHEPHARM.NS', 'ANUP.NS', 'DICIND.NS', 'BINDALAGRO.NS', 'PFS.NS', 'DECCANCE.NS', 'TRIVENI.NS', 'GODREJAGRO.NS', 'HAVELLS.NS', 'SMLISUZU.NS', 'SHRIRAMEPC.NS', 'JBMA.NS', 'NESCO.NS', 'INTELLECT.NS', 'UNIONBANK.NS', 'CENTRALBK.NS', 'UNIENTER.NS', 'TATAMETALI.NS', 'RTNPOWER.NS', 'EMAMILTD.NS', 'SUBROS.NS', 'GRINDWELL.NS', 'LAURUSLABS.NS', 'POLYPLEX.NS', 'POWERINDIA.NS', 'SDBL.NS', 'ADANITRANS.NS', 'MEP.NS', 'FINCABLES.NS', 'GEPIL.NS', 'GANECOS.NS', 'VESUVIUS.NS', 'NAUKRI.NS', 'ARMANFIN.NS', 'TCI.NS', 'RAMCOCEM.NS', 'GHCL.NS', 'ASHOKLEY.NS', 'NATIONALUM.NS', 'HEIDELBERG.NS', 'CENTURYPLY.NS', 'CENTENKA.NS', 'TATAINVEST.NS', 'HINDCOPPER.NS', 'GLOBUSSPR.NS', 'INDUSINDBK.NS', 'VENKEYS.NS', 'KSCL.NS', 'UPL.NS', 'BLUESTARCO.NS', 'NATHBIOGEN.NS', 'NDTV.NS', 'HGINFRA.NS', 'ADORWELD.NS', 'QUICKHEAL.NS', 'PRAKASH.NS', 'KSB.NS', 'CHALET.NS', 'SHRIPISTON.NS', 'FRETAIL.NS', 'TATASTLLP.NS', 'CENTUM.NS', 'DEEPAKNTR.NS', 'JAYAGROGN.NS', 'GVKPIL.NS', 'ATFL.NS', 'REPRO.NS', 'TATACOMM.NS', 'BHARTIARTL.NS', 'TITAN.NS', 'ZYDUSWELL.NS', 'JSWSTEEL.NS', 'NMDC.NS', 'NHPC.NS', 'VGUARD.NS', 'SOBHA.NS', 'ALKEM.NS', 'TVSSRICHAK.NS', 'JAYBARMARU.NS', 'EQUITAS.NS', 'VIPULLTD.NS', 'VMART.NS', 'MANINFRA.NS', 'GMRINFRA.NS', 'NTPC.NS', 'INDOCO.NS', 'ALICON.NS', 'ZOTA.NS', 'KIRIINDUS.NS', 'ALEMBICLTD.NS', 'SAIL.NS', 'SYMPHONY.NS', 'JINDWORLD.NS', 'WABCOINDIA.NS', 'EIDPARRY.NS', 'KEI.NS', 'NILKAMAL.NS', 'OCCL.NS', 'SHRIRAMCIT.NS', 'THEINVEST.NS', 'NAGAFERT.NS', 'DCW.NS', 'RAMCOSYS.NS', 'DREDGECORP.NS', 'BAJAJ-AUTO.NS', 'VINDHYATEL.NS', 'LGBBROSLTD.NS', 'VARDHACRLC.NS', 'TRENT.NS', 'HINDNATGLS.NS', 'ATULAUTO.NS', 'NOCIL.NS', 'RTNINFRA.NS', 'L&TFH.NS', 'DLF.NS', 'BDL.NS', 'DELTACORP.NS', 'CEATLTD.NS', 'EICHERMOT.NS', 'GSFC.NS', 'BPCL.NS', 'ARVINDFASN.NS', 'APARINDS.NS', 'KAJARIACER.NS', 'MANGCHEFER.NS', 'ELGIEQUIP.NS', 'RGL.NS', 'TTKPRESTIG.NS', 'AMARAJABAT.NS', 'JSL.NS', 'DYNAMATECH.NS', 'BEL.NS', 'TNPL.NS', 'SHREECEM.NS', 'BAJAJCON.NS', 'CROMPTON.NS', 'SARDAEN.NS', 'LIBERTSHOE.NS', 'KOLTEPATIL.NS', 'DHAMPURSUG.NS', 'CANFINHOME.NS', 'IDEA.NS', 'HINDCOMPOS.NS', 'TEXRAIL.NS', 'HITECHGEAR.NS', 'MAHINDCIE.NS', 'UNICHEMLAB.NS', 'KPITTECH.NS', 'EVERESTIND.NS', 'ADANIENT.NS', 'VAKRANGEE.NS', 'RUPA.NS', 'PFOCUS.NS', 'HSCL.NS', 'RSYSTEMS.NS', 'GABRIEL.NS', 'LAKSHVILAS.NS', 'SOLARINDS.NS', 'UFO.NS', 'LUXIND.NS', 'KNRCON.NS', 'BLISSGVS.NS', 'AARTIDRUGS.NS', 'JTEKTINDIA.NS', 'HSIL.NS', 'UNIVCABLES.NS', 'BRNL.NS', 'KITEX.NS', 'MINDAIND.NS', 'GILLETTE.NS', 'RUBYMILLS.NS', 'GUJALKALI.NS', 'MUTHOOTCAP.NS', 'BHARATFORG.NS', 'JYOTHYLAB.NS', 'METROPOLIS.NS', 'HONDAPOWER.NS', 'FDC.NS', 'PENIND.NS', 'BEML.NS', 'PHILIPCARB.NS', 'CIGNITITEC.NS', 'PGIL.NS', 'TV18BRDCST.NS', 'DPSCLTD.NS', 'INSECTICID.NS', 'BAJFINANCE.NS', 'SADBHIN.NS', 'IFGLEXPOR.NS', 'AVTNPL.NS', 'PCJEWELLER.NS', 'ECLERX.NS', 'SUZLON.NS', 'ESABINDIA.NS', 'SPARC.NS', 'AEGISCHEM.NS', 'KIRLOSBROS.NS', 'LTTS.NS', 'SCHAEFFLER.NS', 'CONCOR.NS', 'SCI.NS', 'BOMDYEING.NS', 'PRESTIGE.NS', 'GDL.NS', 'ASHAPURMIN.NS', 'CONFIPET.NS', 'EXPLEOSOL.NS', 'TVSMOTOR.NS', 'IOC.NS', 'ATUL.NS', 'MINDACORP.NS', 'HINDOILEXP.NS', 'BIOCON.NS', 'PARAGMILK.NS', 'VADILALIND.NS', 'ERIS.NS', 'PRSMJOHNSN.NS', 'ELECTCAST.NS', 'UNITECH.NS', 'RIIL.NS', 'SATIA.NS', 'PTL.NS', 'WONDERLA.NS', 'CREST.NS', 'BLS.NS', 'MARICO.NS', 'NFL.NS', 'RSWM.NS', 'FEDERALBNK.NS', 'ABB.NS', 'DAAWAT.NS', 'ALANKIT.NS', 'SADBHAV.NS', 'IIFLSEC.NS', 'RELIANCE.NS', 'VAIBHAVGBL.NS', 'DATAMATICS.NS', 'MSTCLTD.NS', 'TECHNOE.NS', 'CLNINDIA.NS', 'VTL.NS', 
    'DEN.NS', 'JINDALSAW.NS', 'DIAMONDYD.NS', 'SBIN.NS', 'ABFRL.NS', 'JSLHISAR.NS', 'BHARATRAS.NS', 'PTC.NS', 'CANTABIL.NS', 'JETAIRWAYS.NS', 'GPIL.NS', 'JUSTDIAL.NS', 'LINCOLN.NS', 'EXCELINDUS.NS', 'GFLLIMITED.NS', 'JPASSOCIAT.NS', 'EIFFL.NS', 'AAVAS.NS', 'BHAGERIA.NS', 'ASHOKA.NS', 'BOSCHLTD.NS', 'GOLDIAM.NS', 'ASIANTILES.NS', 'HEG.NS', 'IBREALEST.NS', 'GEOJITFSL.NS', 'NAVKARCORP.NS', 'RPGLIFE.NS', 'SHAKTIPUMP.NS', 'RKFORGE.NS', 'PGHL.NS', 'YESBANK.NS', 'GREENLAM.NS', 'FSC.NS', 'OAL.NS', 'ASTEC.NS', 'SANGHVIMOV.NS', 'EIHOTEL.NS', 'DEEPAKFERT.NS', 'JMCPROJECT.NS', 'DHFL.NS', 'FCL.NS', 'MFSL.NS', 'CERA.NS', 'JKLAKSHMI.NS', 'SAGCEM.NS', 'BRITANNIA.NS', 'BANARISUG.NS', 'EMAMIPAP.NS', 'VOLTAS.NS', 'PLASTIBLEN.NS', 'GET&D.NS', 'SHREEPUSHK.NS', 'BASF.NS', 'MAHSEAMLES.NS', 'NIACL.NS', 'HGS.NS', 'SUTLEJTEX.NS', 'MANAKSIA.NS', 'ENIL.NS', 'TATAPOWER.NS', 'VSSL.NS', 'KALPATPOWR.NS', 'INOXWIND.NS', 'BAJAJFINSV.NS', 'IMPAL.NS', 'CGPOWER.NS', 'IDFCFIRSTB.NS', 'AMBUJACEM.NS', 'SUNTECK.NS', 'WELSPUNIND.NS', 'SUVENPHAR.NS', 'TEJASNET.NS', 'NITINSPIN.NS', 'BCG.NS', 'MTNL.NS', 'SUMMITSEC.NS', 'SANGAMIND.NS', 'APLAPOLLO.NS', 'NAVNETEDUL.NS', 'POLYMED.NS', 'STARCEMENT.NS', 'PUNJABCHEM.NS', 'IFCI.NS', 'ICICIGI.NS', 'HUDCO.NS', 'SASKEN.NS', 'REPCOHOME.NS', 'DHANBANK.NS', 'SUNPHARMA.NS', 'GUJGASLTD.NS', 'RAMCOIND.NS', 'PANAMAPET.NS', 'NLCINDIA.NS', 'HTMEDIA.NS', 'GULFPETRO.NS', 'HDFC.NS', 'KARURVYSYA.NS', 'TI.NS', 'ALBERTDAVD.NS', 'GSKCONS.NS', 'OIL.NS', 'SHILPAMED.NS', 'AMBER.NS', 'FACT.NS', 'STERTOOLS.NS', 'AUBANK.NS', 'MRF.NS', 'BODALCHEM.NS', 'ORIENTPPR.NS', 'AVADHSUGAR.NS', 'DLINKINDIA.NS', '3IINFOTECH.NS', 'ACC.NS', 'BGRENERGY.NS', 'RVNL.NS', 'ARSHIYA.NS', 'DIXON.NS', '63MOONS.NS', 'GAEL.NS', 'APOLLOTYRE.NS', 'GNFC.NS', 'ZEEL.NS', 'VINATIORGA.NS', 'BIRLACORPN.NS', 'HEXAWARE.NS', 'KARDA.NS', 'AUROPHARMA.NS', 'AMRUTANJAN.NS', 'ULTRACEMCO.NS', 'UJJIVAN.NS', 'MINDTREE.NS', 'TATAMOTORS.NS', 'FORTIS.NS', 'SUNTV.NS', 'INDIANHUME.NS', 'WABAG.NS', 'GRAVITA.NS', 'ESTER.NS', 'TAJGVK.NS', 'ICIL.NS', 'LALPATHLAB.NS', 'GATI.NS', 'HIRECT.NS', 'ARTEMISMED.NS', 'ASTERDM.NS', 'RAIN.NS', 'SBILIFE.NS', 'SPAL.NS', 'MARUTI.NS', 'HATHWAY.NS', 'ADANIPOWER.NS', 'GREENPANEL.NS', 'JSWHL.NS', 'BFINVEST.NS', 'TDPOWERSYS.NS', 'MENONBE.NS', 'MAHESHWARI.NS', 'DALBHARAT.NS', 'TATASTEEL.NS', 'TNPETRO.NS', 'GAYAPROJ.NS', 'ALOKINDS.NS', 'KEC.NS', 'SMSPHARMA.NS', 'PAISALO.NS', 'TCIEXP.NS', 'PIDILITIND.NS', 'GMMPFAUDLR.NS', 'PSPPROJECT.NS', 'ICICIBANK.NS', 'ANANTRAJ.NS', 'RITES.NS', 'BALAMINES.NS', 'WELENT.NS', 'MAHABANK.NS', 'ICICIPRULI.NS', 'HIMATSEIDE.NS', 'SRIPIPES.NS', 'ELECON.NS', 'STAR.NS', 'IRCON.NS', 'OBEROIRLTY.NS', 'KANSAINER.NS', 'GALLISPAT.NS', 'HLVLTD.NS', 'AXISBANK.NS', 'M&M.NS', 'MARKSANS.NS', 'ADVANIHOTR.NS', 'VIPIND.NS', 'HDFCAMC.NS', 'VSTIND.NS', 'INDOSTAR.NS', 'AIAENG.NS', 'SUVEN.NS', 'SIYSIL.NS', 'TANLA.NS', 'TWL.NS', 'MUNJALAU.NS', 'GMDCLTD.NS', 'IOLCP.NS', 'HDFCLIFE.NS', 'IEX.NS', 'GODREJCP.NS', 'MASFIN.NS', 'INFY.NS', 'IIFL.NS', 'LUMAXTECH.NS', 'TORNTPHARM.NS', 'VBL.NS', 'GSPL.NS', 'RADIOCITY.NS', 'SAFARI.NS', 'BBTC.NS', 'BAJAJHIND.NS', 'UJJIVANSFB.NS', 'ALLSEC.NS', 'TEAMLEASE.NS', 'IFBIND.NS', 'ONMOBILE.NS', 'GRASIM.NS', '5PAISA.NS', 'RENUKA.NS', 'INEOSSTYRO.NS', 'AARTIIND.NS', 'NEOGEN.NS', 'INDIGO.NS', 'CASTROLIND.NS', 'CAMLINFINE.NS', 'SPANDANA.NS', 'HARITASEAT.NS', 'ENDURANCE.NS', 'CHAMBLFERT.NS', 'NBCC.NS', 'THEJO.NS', 'GALLANTT.NS', 'CONTROLPR.NS', 'SANDHAR.NS', 'SESHAPAPER.NS', 'INDIAMART.NS', 'AKASH.NS', 'MIDHANI.NS', 'WELCORP.NS', 'MUKANDLTD.NS', 'NH.NS', 'FOSECOIND.NS', 'CRISIL.NS', 'LUPIN.NS', 'ONGC.NS', 'LAOPALA.NS', 'SHK.NS', 'LUMAXIND.NS', 'AVANTIFEED.NS', 'J&KBANK.NS', 'CAPACITE.NS', 'LINCPEN.NS', 'ARVSMART.NS', 'APOLLOHOSP.NS', 'IPCALAB.NS', 'NEWGEN.NS', 'JKPAPER.NS', 'GICRE.NS', 'SJVN.NS', 'CARERATING.NS', 'NUCLEUS.NS', 'RAMANEWS.NS', 'KOTAKBANK.NS', 'KTKBANK.NS', 'UBL.NS', 'CUB.NS', 'CIPLA.NS', 'TATASTLBSL.NS', 'SHANKARA.NS', 'BUTTERFLY.NS', 'CUMMINSIND.NS', 'JSWENERGY.NS', 'OMAXE.NS', 'DBCORP.NS', 'PILANIINVS.NS', 'WHIRLPOOL.NS', 'ASALCBR.NS', 'ACE.NS', 'ABCAPITAL.NS', 'PEL.NS', 'APCOTEXIND.NS', 'ORISSAMINE.NS', 'BANKINDIA.NS', 'FMGOETZE.NS', 'DISHTV.NS', 'WIPRO.NS', 'AKZOINDIA.NS', 'TIMKEN.NS', 'RADICO.NS', 'BALMLAWRIE.NS', 'JINDALPOLY.NS', 'CHOLAFIN.NS', 'SANOFI.NS', 'BANCOINDIA.NS', 'TATAELXSI.NS', 'BALKRISIND.NS', 'THANGAMAYL.NS', 'NSIL.NS', 'TAKE.NS', 'CADILAHC.NS', 'ADVENZYMES.NS', 'AGCNET.NS', 'IGPL.NS', 'ICRA.NS', 'CHOLAHLDNG.NS', 'PNBHOUSING.NS', 'MAGMA.NS', 'NELCO.NS', 'MBAPL.NS', 'CHENNPETRO.NS', 'GLAXO.NS', 'TIDEWATER.NS', 'DOLLAR.NS', 'DABUR.NS', 'MUNJALSHOW.NS', 'COALINDIA.NS', 'ZENTEC.NS', 'CANBK.NS', 'APCL.NS', 'TTML.NS', 'CEREBRAINT.NS', 'NACLIND.NS', 'TCNSBRANDS.NS', 'SEAMECLTD.NS', 'LAXMIMACH.NS', 'TCPLPACK.NS', 'GOCLCORP.NS', 'COSMOFILMS.NS', 'GLENMARK.NS', 'XCHANGING.NS', 'MARATHON.NS', 'JKTYRE.NS', 'KCP.NS', 'MAXVIL.NS', 'KIOCL.NS', 'HONAUT.NS', 'MANGLMCEM.NS', 'INDRAMEDCO.NS', 'GTLINFRA.NS', 'GIRRESORTS.NS', 
    'NATCOPHARM.NS', 'IBULHSGFIN.NS', 'VISHWARAJ.NS', 'MRPL.NS', 'NIITLTD.NS', 'AHLUCONT.NS', 'POKARNA.NS', 'SCHNEIDER.NS', 'ZEELEARN.NS', 'SHALBY.NS', 'TORNTPOWER.NS', 'SASTASUNDR.NS', 'RATNAMANI.NS', 'KKCL.NS', 'SWANENERGY.NS', 'CDSL.NS', 'POWERMECH.NS', 'RECLTD.NS', 'PDSMFL.NS', 'BALRAMCHIN.NS', 'SKIPPER.NS', 'MANAPPURAM.NS', 'WOCKPHARMA.NS', 'GANDHITUBE.NS', 'HFCL.NS', 'JCHAC.NS', 'RCF.NS', 'GUFICBIO.NS', 'GPPL.NS', 'MARINE.NS', 'PNCINFRA.NS', 'ORICONENT.NS', 'VSTTILLERS.NS', 'CAREERP.NS', 'JKIL.NS', 'ANDHRAPAP.NS', 'SUNDARMFIN.NS', 'SANDESH.NS', 'SUPREMEIND.NS', 'PHOENIXLTD.NS', 'BANKBARODA.NS', 'SUNDRMFAST.NS', 'PSB.NS', '3RDROCK.NS', 'IIFLWAM.NS', 'SUDARSCHEM.NS', 'INOXLEISUR.NS', 'HIL.NS', 'APLLTD.NS', 'THYROCARE.NS', 'GRANULES.NS', 'DMART.NS', 'SIEMENS.NS', 'ISEC.NS', 'ZENSARTECH.NS', 'INGERRAND.NS', 'UCALFUEL.NS', 'RBLBANK.NS', 'SOUTHBANK.NS', 'HESTERBIO.NS', 'SNOWMAN.NS', 'HAL.NS', 'RESPONIND.NS', 'CENTRUM.NS', 'SONATSOFTW.NS', 'EXIDEIND.NS', 'PATELENG.NS', 'FCONSUMER.NS', 'IRCTC.NS', 'MOREPENLAB.NS', 'HINDUNILVR.NS', 'SOTL.NS', 'NBVENTURES.NS', 'JINDALSTEL.NS', 'FEL.NS', 'HMVL.NS', 'SREINFRA.NS', 'VARROC.NS', 'ACCELYA.NS', 'KPRMILL.NS', 'BANDHANBNK.NS', 'SUMICHEM.NS', 'GODREJIND.NS', 'MOTILALOFS.NS', 'DVL.NS', 'ADFFOODS.NS', 'CSBBANK.NS', 'MHRIL.NS', 'JAIBALAJI.NS', 'IRB.NS', 'HINDPETRO.NS', 'RELIGARE.NS', 'CREDITACC.NS', 'EVEREADY.NS', 'SHALPAINTS.NS', 'KESORAMIND.NS', 'SHANTIGEAR.NS', 'INFIBEAM.NS', 'MUTHOOTFIN.NS', 'SATIN.NS', 'SURYAROSNI.NS', 'BAJAJELEC.NS', 'MANALIPETC.NS', 'TASTYBITE.NS', 'SIS.NS', 'SFL.NS', 'CARBORUNIV.NS', 'ORIENTHOT.NS', 'HERITGFOOD.NS', 'RAJESHEXPO.NS', 'UCOBANK.NS', 'GULFOILLUB.NS', 'THERMAX.NS', 'IGL.NS', 'FINEORG.NS', 'RAYMOND.NS', 'ALLCARGO.NS', 'GODREJPROP.NS', 'GODFRYPHLP.NS', 'GUJAPOLLO.NS', 'VEDL.NS', 'GOKEX.NS', 'ITI.NS', 'PRINCEPIPE.NS', 'TIMETECHNO.NS', 'RML.NS', 'NCLIND.NS', 'SIRCA.NS', 'RPOWER.NS', 'PFIZER.NS', 'INDIANB.NS', 'MOLDTKPAC.NS', 'SPENCERS.NS', 'HCC.NS', 'FLUOROCHEM.NS', 'BBL.NS', 'MMTC.NS', 'GICHSGFIN.NS', 'NECLIFE.NS', 'SYNGENE.NS', 'CUPID.NS', 'CCL.NS', 'WENDT.NS', 'SHARDACROP.NS', 'HBLPOWER.NS', 'TTKHLTCARE.NS', 'MAHEPC.NS', 'KAYA.NS', 'PNB.NS', 'FINPIPE.NS', 'THOMASCOOK.NS', 'ARVIND.NS', 'PVR.NS', 'TATACHEM.NS', 'BALAJITELE.NS', 'VHL.NS', 'MONTECARLO.NS', 'JISLJALEQS.NS', 'DHANUKA.NS', 'GENUSPOWER.NS', 'GARFIBRES.NS', 'SAREGAMA.NS', 'SUPPETRO.NS', 'ALKYLAMINE.NS', 'PIIND.NS', 'TATACONSUM.NS', 'ESCORTS.NS', 'LEMONTREE.NS', 'ORIENTCEM.NS', 'TINPLATE.NS', 'ASAHIINDIA.NS', 'NAM-INDIA.NS', 'UTTAMSUGAR.NS', 'AHLEAST.NS', 'IFBAGRO.NS', 'JKCEMENT.NS', 'ADANIGREEN.NS', 'IMFA.NS', 'KCPSUGIND.NS', 'MIRZAINT.NS', 'USHAMART.NS', 'RICOAUTO.NS', 'LICHSGFIN.NS', 'RCOM.NS', 'JAGRAN.NS', 'AUTOAXLES.NS', 'KIRLOSIND.NS', 'ORIENTREF.NS', 'SWSOLAR.NS', 'PFC.NS', 'EDELWEISS.NS', 'JAMNAAUTO.NS', 'JPPOWER.NS', 'ORIENTELEC.NS', 'AJMERA.NS', 'GRAPHITE.NS', 'STCINDIA.NS', 'ASIANPAINT.NS', 'HEROMOTOCO.NS', 'TRITURBINE.NS', 'VRLLOG.NS', 'MAHLIFE.NS', 'LT.NS', 'MADRASFERT.NS', 'AJANTPHARM.NS', 'SEQUENT.NS', 'MGL.NS', 'NELCAST.NS', 'VISAKAIND.NS', 'PURVA.NS', 'CHEMBOND.NS', 'GESHIP.NS', 'DCMSHRIRAM.NS', 'SSWL.NS', 'DCAL.NS', 'FILATEX.NS', 'UFLEX.NS', 'SHIL.NS', 'BSE.NS', 'OFSS.NS', 'MASTEK.NS', 'PANACEABIO.NS', 'SREEL.NS', 'SRTRANSFIN.NS', 'MMFL.NS', 'JUBLFOOD.NS', 'SHOPERSTOP.NS', 'COROMANDEL.NS', 'APOLLOPIPE.NS', 'ZEEMEDIA.NS', 'INDNIPPON.NS', 'M&MFIN.NS', 'PAGEIND.NS', 'RAJTV.NS', 'NEULANDLAB.NS', 'SUNDARMHLD.NS', 'PERSISTENT.NS', 'TIINDIA.NS', 'PRICOLLTD.NS', 'LINDEINDIA.NS', 'ORBTEXP.NS', 'ITC.NS', 'APTECHT.NS', 'VOLTAMP.NS', 'BSOFT.NS', 'MOTHERSUMI.NS', 'NXTDIGITAL.NS', 'GIPCL.NS', 'THEMISMED.NS', 'INFOBEAN.NS', 'INDHOTEL.NS', 'ASHIANA.NS', 'RELINFRA.NS', 'BLUEDART.NS', 'GTPL.NS', 'IDBI.NS', 'MATRIMONY.NS', 'SHREDIGCEM.NS', 'PPAP.NS', 'GNA.NS', 'MCDOWELL-N.NS', 'BERGEPAINT.NS', 'TIIL.NS', 'SUNFLAG.NS', 'ZODIACLOTH.NS', 'CYIENT.NS', 'PRECWIRE.NS', 'TFCILTD.NS', 'RAMKY.NS', '3MINDIA.NS', 'HCLTECH.NS', 'HIKAL.NS', 'TATACOFFEE.NS', 'SKFINDIA.NS', 'IDFC.NS', 'GREENPLY.NS', 'AFFLE.NS', 'PRECAM.NS', 'TECHM.NS', 'MOIL.NS', 'GAIL.NS', 'TRIDENT.NS', 'INDORAMA.NS', 'HINDZINC.NS', 'NCC.NS', 'HERCULES.NS', 'REDINGTON.NS', 'DBL.NS', 'TEXINFRA.NS', 'V2RETAIL.NS', 'EBIXFOREX.NS', 'DALMIASUG.NS', 'ANDHRSUGAR.NS', 'MANINDS.NS', 'BAJAJHLDNG.NS', 'MAHLOG.NS', 'CESC.NS']    

    # list_stok = ['GODREJIND.NS', 'HGINFRA.NS', 'KITEX.NS', 'WELSPUNIND.NS', 'ENIL.NS', 'THOMASCOOK.NS', 'VADILALIND.NS', 'BATAINDIA.NS', 'TEAMLEASE.NS', 'ANUP.NS', 'GODREJAGRO.NS', 'GODFRYPHLP.NS', 'SRIPIPES.NS', 'APLLTD.NS', 'ERIS.NS', 'CANTABIL.NS', 'HDFCAMC.NS', 'NILKAMAL.NS', 'BODALCHEM.NS', 'GMDCLTD.NS', 'MEP.NS', 'UCALFUEL.NS', 'BOSCHLTD.NS', 'VARROC.NS', 'GMRINFRA.NS', 'SHILPAMED.NS', 'JINDALSAW.NS', 'MINDAIND.NS', 'NLCINDIA.NS', 'ADANIGAS.NS', 'CRISIL.NS', 'MONTECARLO.NS', 'MUNJALAU.NS', 'OMAXE.NS', 'ACC.NS', 'SUBROS.NS', 'MANALIPETC.NS', 'UTTAMSUGAR.NS', 'SARDAEN.NS', 'HDFCLIFE.NS', 'CIGNITITEC.NS', 'OLECTRA.NS', 'BHEL.NS', 'BAJAJ-AUTO.NS', 'APCL.NS', 'MUKANDLTD.NS', 'INFY.NS', 'TATASTLBSL.NS', 'TVSSRICHAK.NS', 'DAAWAT.NS', 'TRIDENT.NS', 'REPRO.NS', 'NEOGEN.NS', 'ASTERDM.NS', 'GODREJCP.NS', 'GULFPETRO.NS', 'BAJAJCON.NS', 'DCAL.NS', 'PURVA.NS', 'JAYAGROGN.NS', 'DALBHARAT.NS', 'WOCKPHARMA.NS', 'CAPACITE.NS', '3RDROCK.NS', 'JAICORPLTD.NS', 'DALMIASUG.NS', 'ARVSMART.NS', 'KCPSUGIND.NS', 'GET&D.NS', 'INDOCO.NS', 'ASHOKA.NS', 'PTC.NS', 'SHAKTIPUMP.NS', 'GREAVESCOT.NS', 'DEEPAKNTR.NS', 'GATI.NS', 'AGCNET.NS', 'PANACEABIO.NS', 'SRTRANSFIN.NS', 'HINDCOPPER.NS', 'COSMOFILMS.NS', 'KIOCL.NS', 'GARFIBRES.NS', 'GLENMARK.NS', 'JSL.NS', 'NESCO.NS', 'TANLA.NS', 'HARITASEAT.NS', 'BASF.NS', 'UFO.NS', 'SJVN.NS', 'SHOPERSTOP.NS', 'PRSMJOHNSN.NS', 'PARAGMILK.NS', 'HERCULES.NS', 'NAVKARCORP.NS', 'MUNJALSHOW.NS', 'GICHSGFIN.NS', 'BLISSGVS.NS', 'SUVEN.NS', 'DHFL.NS', 'HDFCBANK.NS', 'APOLLOTYRE.NS', 'ORIENTCEM.NS', 'BIRLACORPN.NS', 'ZEELEARN.NS', 'COLPAL.NS', 'CERA.NS', 'RAMCOCEM.NS', 'AUBANK.NS', 'JAMNAAUTO.NS', 'USHAMART.NS', 'MENONBE.NS', 'SKFINDIA.NS', 'INDOSTAR.NS', 'MOTILALOFS.NS', 'KSL.NS', 'ENDURANCE.NS', 'BHARATRAS.NS', 'CADILAHC.NS', 'COCHINSHIP.NS', 'MANGLMCEM.NS', 'JKIL.NS', 'INDNIPPON.NS', 'MAITHANALL.NS', 'GNFC.NS', 'VISAKAIND.NS', 'SHANTIGEAR.NS', 'RELINFRA.NS', 'SIEMENS.NS', 'YESBANK.NS', 'HINDCOMPOS.NS', 'SAIL.NS', 'WHEELS.NS', 'NBCC.NS', 'POWERINDIA.NS', 'GOCLCORP.NS', 'TAKE.NS', 'QUICKHEAL.NS', 'MANAPPURAM.NS', 'OIL.NS', 'PNBHOUSING.NS', 'AMBIKCO.NS', 'GRAVITA.NS', 'THYROCARE.NS', 'KKCL.NS', 'KARURVYSYA.NS', 'AHLWEST.NS', 'GVKPIL.NS', 'SOTL.NS', 'INDIAMART.NS', 'TCS.NS', 'ELECTCAST.NS', 'LALPATHLAB.NS', 'IOB.NS', 'KIRLOSENG.NS', 'GTLINFRA.NS', 'CREST.NS', 'TRENT.NS', 'ASIANTILES.NS', 'RESPONIND.NS', 'ASTRAL.NS', 'CENTUM.NS', 'GRANULES.NS', 'SUDARSCHEM.NS', 'SEQUENT.NS', 'SATIN.NS', 'LIBERTSHOE.NS', 'UFLEX.NS', 'RPGLIFE.NS', 'NXTDIGITAL.NS', 'SAGCEM.NS', 'WABAG.NS', 'FCONSUMER.NS', 'GREENPANEL.NS', 'ORIENTHOT.NS', 'POLYCAB.NS', 'ADANIPOWER.NS', 'VBL.NS', 'SUPRAJIT.NS', 'NH.NS', 'EVERESTIND.NS', 'SOMANYCERA.NS', 'JUSTDIAL.NS', 'HATSUN.NS', 'EMAMIPAP.NS', 'TECHM.NS', 'KNRCON.NS', 'RBL.NS', 'PPAP.NS', 'TCI.NS', 'ATFL.NS', 'GNA.NS', 'GICRE.NS', 'PRESTIGE.NS', 'PIIND.NS', 'VRLLOG.NS', 'ASTEC.NS', 'HBLPOWER.NS', 'FCL.NS']
    #list_stok = ['UNIONBANK.NS', 'IIFLWAM.NS', 'NBCC.NS', 'ITDCEM.NS', 'PENIND.NS', 'PATELENG.NS', 'VEDL.NS', 'FEDERALBNK.NS', 'SCHAEFFLER.NS', 'GRINDWELL.NS', 'KKCL.NS', 'PFOCUS.NS', 'NEULANDLAB.NS', 'GOLDIAM.NS', 'GIPCL.NS', 'BAJAJELEC.NS', 'UPL.NS', 'ALICON.NS', 'SKIPPER.NS', 'ACCELYA.NS', 'BALMLAWRIE.NS', 'BEPL.NS', 'SOMANYCERA.NS', 'RAYMOND.NS', 'IFCI.NS', 'ELECTCAST.NS', 'ESTER.NS', 'NATCOPHARM.NS', 'MARKSANS.NS', 'JUSTDIAL.NS', 'MPHASIS.NS', 'CSBBANK.NS', 'MRF.NS', 'MARATHON.NS', 'EVERESTIND.NS', 'AHLWEST.NS', 'PARAGMILK.NS', 'PIIND.NS', 'EQUITAS.NS', 'MAHESHWARI.NS', 'SHRIPISTON.NS', '5PAISA.NS', 'EIHOTEL.NS', 'SUVEN.NS', 'GALLANTT.NS', 'BFINVEST.NS', 'VIPULLTD.NS', 'TANLA.NS', 'RSWM.NS', 'UJJIVAN.NS', 'IFBIND.NS', 'CHEMFAB.NS', 'HFCL.NS', 'SOUTHBANK.NS', 'KICL.NS', 'CADILAHC.NS', 'BEL.NS', 'INDIAMART.NS', 'RAJESHEXPO.NS', 'SSWL.NS', 'OBEROIRLTY.NS', 'CEATLTD.NS', 'J&KBANK.NS', 'CARERATING.NS', 'BLS.NS', 'VGUARD.NS', 'AVANTIFEED.NS', 'GMRINFRA.NS', 'LICHSGFIN.NS', 'SUDARSCHEM.NS', 'IDEA.NS', 'MARINE.NS', 'KUANTUM.NS', 'SANOFI.NS', 'ARVSMART.NS', 'LEMONTREE.NS', 'SMLISUZU.NS', 'VIPIND.NS', 'INFOBEAN.NS', 'HONDAPOWER.NS', 'MAXVIL.NS', 'GREENPANEL.NS', 'SUMMITSEC.NS', 'JKLAKSHMI.NS', 'GATI.NS', 'MIRZAINT.NS', 'KEI.NS', 'MUNJALSHOW.NS', 'PNBHOUSING.NS', 'BLISSGVS.NS', 'MATRIMONY.NS', 'TATAINVEST.NS', 'MUTHOOTCAP.NS', 'ARMANFIN.NS', 'INGERRAND.NS', 'LTTS.NS', 'OLECTRA.NS', 'IGL.NS', 'FINCABLES.NS', 'AVADHSUGAR.NS', 'HAL.NS', 'PFS.NS', 'BHARATFORG.NS', 'SATIN.NS', 'DLINKINDIA.NS', 'MANINFRA.NS', 'ZENSARTECH.NS', 'BUTTERFLY.NS', 'MOIL.NS', 'GDL.NS', 'ATFL.NS', 'MAHSCOOTER.NS', 'SUMICHEM.NS', 'RTNPOWER.NS', 'PNBGILTS.NS', 'BATAINDIA.NS', 'GODREJPROP.NS', 'INDUSINDBK.NS', 'RECLTD.NS', 'SADBHAV.NS', 'THEINVEST.NS', 'CENTUM.NS', 'VENKEYS.NS', 'KSL.NS', 'NBVENTURES.NS', 'SWARAJENG.NS', 'CHENNPETRO.NS', 'ULTRACEMCO.NS', 'VESUVIUS.NS', 'MANINDS.NS', 'JINDWORLD.NS', 'COALINDIA.NS', 'LINDEINDIA.NS', 'SUNCLAYLTD.NS', 'COSMOFILMS.NS', 'BANKINDIA.NS', 'TRITURBINE.NS', 'FORTIS.NS', 'SRIPIPES.NS', '3IINFOTECH.NS', 'VADILALIND.NS', 'WELSPUNIND.NS', 'PRSMJOHNSN.NS', 'SBICARD.NS', 'JBCHEPHARM.NS', 'HAVELLS.NS', 'IOB.NS', 'ICRA.NS', 'BLUEDART.NS', 'APEX.NS', 'SANGAMIND.NS', 'KPRMILL.NS', 'GULFPETRO.NS', 'BHAGERIA.NS', 'MANGCHEFER.NS', 'ACC.NS', 'ABCAPITAL.NS', 'HINDCOMPOS.NS', 'GENUSPOWER.NS', 'TASTYBITE.NS', 'SMSPHARMA.NS', 'UTTAMSUGAR.NS', 'BLUESTARCO.NS', 'ANUP.NS', 'UFO.NS', 'AEGISCHEM.NS', 'CENTRALBK.NS', 'JCHAC.NS', 'MARICO.NS', 'NTPC.NS', 'ATUL.NS', 'UNIVCABLES.NS', 'VOLTAS.NS', 'TATACOFFEE.NS', 'DCAL.NS', 'ORBTEXP.NS', 'PURVA.NS', 'THEMISMED.NS', 'NXTDIGITAL.NS', 'TCNSBRANDS.NS', 'KAYA.NS', 'JBMA.NS', 'HINDOILEXP.NS', 'INTELLECT.NS', 'JAYBARMARU.NS', 'STERTOOLS.NS', 'ABFRL.NS', 'BANDHANBNK.NS', 'HINDNATGLS.NS', 'CUPID.NS', 'GOKEX.NS', 'ORIENTELEC.NS', 'FLFL.NS', 'GANDHITUBE.NS', 'RAMCOSYS.NS', 'GET&D.NS', 'CENTURYPLY.NS', 'AFFLE.NS', 'JYOTHYLAB.NS', 'INFY.NS']
    begin = time.time()
    stock_data = BasketStockData(True, 70)
    if len(sys.argv)>1:
        if sys.argv[1]=='--update':
            update_data = True
    else:
        update_data = False
    x = stock_data.generate_dict(list_stok,update_data=update_data)
    end = time.time()
    print(f'Time taken to extract data: {end - begin}')

    begin1 = time.time()
    dict_of_dataframes = x
    base_lookback = 7
    number_of_readings = 200

    eng_obj = Engine2(dict_of_dataframes = dict_of_dataframes, base_lookback = base_lookback, number_of_readings = number_of_readings)
    longs, shorts = eng_obj.generate(absolute_list = False)
    print ("Metrics " + '\n' + "Base Lookback: " + str(base_lookback) + '\n' + "Number of Readings: " + str(number_of_readings))
    print("Readings: ")
    print(longs)
    print()
    print("Shorts: ")
    print(shorts)
    print()

    end1 = time.time()

    print(f"Time taken to compute data: {end1 - begin1}")

if __name__ == '__main__':
    main()
# ['FB'])
# print(dict1)
