nan = None;  NAN = None
nan = 0
reports = []
class ValErr:
    def __init__(self, value, error, antisym):
        self.value, self.error, self.antisym = value, error, antisym

    def __repr__(self):
        if self.antisym == 0.:
            return "%g +- %g" % (self.value, self.error)
        else:
            return "%g +- %g ~ %g" % (self.value, self.error, self.antisym)

class Report:
    def __init__(self, chamberId, postal_address, name):
        self.chamberId, self.postal_address, self.name = chamberId, postal_address, name
        self.status = "NOFIT"
        self.fittype = None
        self.CovMatrix = None

    def add_parameters(self, deltax, deltay, deltaz, deltaphix, deltaphiy, deltaphiz, loglikelihood, numsegments, sumofweights, redchi2):
        self.status = "PASS"
        self.deltax, self.deltay, self.deltaz, self.deltaphix, self.deltaphiy, self.deltaphiz = deltax, deltay, deltaz, deltaphix, deltaphiy, deltaphiz
        self.loglikelihood, self.numsegments, self.sumofweights, self.redchi2 = loglikelihood, numsegments, sumofweights, redchi2

    def add_stats(self, median_x, median_y, median_dxdz, median_dydz, mean30_x, mean30_y, mean20_dxdz, mean50_dydz, mean15_x, mean15_y, mean10_dxdz, mean25_dydz, wmean30_x, wmean30_y, wmean20_dxdz, wmean50_dydz, wmean15_x, wmean15_y, wmean10_dxdz, wmean25_dydz, stdev30_x, stdev30_y, stdev20_dxdz, stdev50_dydz, stdev15_x, stdev15_y, stdev10_dxdz, stdev25_dydz):
        self.median_x, self.median_y, self.median_dxdz, self.median_dydz, self.mean30_x, self.mean30_y, self.mean20_dxdz, self.mean50_dydz, self.mean15_x, self.mean15_y, self.mean10_dxdz, self.mean25_dydz, self.wmean30_x, self.wmean30_y, self.wmean20_dxdz, self.wmean50_dydz, self.wmean15_x, self.wmean15_y, self.wmean10_dxdz, self.wmean25_dydz, self.stdev30_x, self.stdev30_y, self.stdev20_dxdz, self.stdev50_dydz, self.stdev15_x, self.stdev15_y, self.stdev10_dxdz, self.stdev25_dydz = median_x, median_y, median_dxdz, median_dydz, mean30_x, mean30_y, mean20_dxdz, mean50_dydz, mean15_x, mean15_y, mean10_dxdz, mean25_dydz, wmean30_x, wmean30_y, wmean20_dxdz, wmean50_dydz, wmean15_x, wmean15_y, wmean10_dxdz, wmean25_dydz, stdev30_x, stdev30_y, stdev20_dxdz, stdev50_dydz, stdev15_x, stdev15_y, stdev10_dxdz, stdev25_dydz

    def __repr__(self):
        return "<Report %s %s %s>" % (self.postal_address[0], " ".join(map(str, self.postal_address[1:])), self.status)

reports.append(Report(574914560, ("DT", -2, 1, 1), "MBwhAst1sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575176704, ("DT", -2, 1, 2), "MBwhAst1sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575438848, ("DT", -2, 1, 3), "MBwhAst1sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575700992, ("DT", -2, 1, 4), "MBwhAst1sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575963136, ("DT", -2, 1, 5), "MBwhAst1sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576225280, ("DT", -2, 1, 6), "MBwhAst1sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576487424, ("DT", -2, 1, 7), "MBwhAst1sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576749568, ("DT", -2, 1, 8), "MBwhAst1sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577011712, ("DT", -2, 1, 9), "MBwhAst1sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577273856, ("DT", -2, 1, 10), "MBwhAst1sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577536000, ("DT", -2, 1, 11), "MBwhAst1sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577798144, ("DT", -2, 1, 12), "MBwhAst1sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579108864, ("DT", -2, 2, 1), "MBwhAst2sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579371008, ("DT", -2, 2, 2), "MBwhAst2sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579633152, ("DT", -2, 2, 3), "MBwhAst2sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579895296, ("DT", -2, 2, 4), "MBwhAst2sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580157440, ("DT", -2, 2, 5), "MBwhAst2sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580419584, ("DT", -2, 2, 6), "MBwhAst2sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580681728, ("DT", -2, 2, 7), "MBwhAst2sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580943872, ("DT", -2, 2, 8), "MBwhAst2sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581206016, ("DT", -2, 2, 9), "MBwhAst2sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581468160, ("DT", -2, 2, 10), "MBwhAst2sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581730304, ("DT", -2, 2, 11), "MBwhAst2sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581992448, ("DT", -2, 2, 12), "MBwhAst2sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583303168, ("DT", -2, 3, 1), "MBwhAst3sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583565312, ("DT", -2, 3, 2), "MBwhAst3sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583827456, ("DT", -2, 3, 3), "MBwhAst3sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584089600, ("DT", -2, 3, 4), "MBwhAst3sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584351744, ("DT", -2, 3, 5), "MBwhAst3sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584613888, ("DT", -2, 3, 6), "MBwhAst3sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584876032, ("DT", -2, 3, 7), "MBwhAst3sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585138176, ("DT", -2, 3, 8), "MBwhAst3sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585400320, ("DT", -2, 3, 9), "MBwhAst3sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585662464, ("DT", -2, 3, 10), "MBwhAst3sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585924608, ("DT", -2, 3, 11), "MBwhAst3sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586186752, ("DT", -2, 3, 12), "MBwhAst3sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(574947328, ("DT", -1, 1, 1), "MBwhBst1sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575209472, ("DT", -1, 1, 2), "MBwhBst1sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575471616, ("DT", -1, 1, 3), "MBwhBst1sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575733760, ("DT", -1, 1, 4), "MBwhBst1sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575995904, ("DT", -1, 1, 5), "MBwhBst1sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576258048, ("DT", -1, 1, 6), "MBwhBst1sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576520192, ("DT", -1, 1, 7), "MBwhBst1sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576782336, ("DT", -1, 1, 8), "MBwhBst1sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577044480, ("DT", -1, 1, 9), "MBwhBst1sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577306624, ("DT", -1, 1, 10), "MBwhBst1sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577568768, ("DT", -1, 1, 11), "MBwhBst1sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577830912, ("DT", -1, 1, 12), "MBwhBst1sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579141632, ("DT", -1, 2, 1), "MBwhBst2sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579403776, ("DT", -1, 2, 2), "MBwhBst2sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579665920, ("DT", -1, 2, 3), "MBwhBst2sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579928064, ("DT", -1, 2, 4), "MBwhBst2sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580190208, ("DT", -1, 2, 5), "MBwhBst2sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580452352, ("DT", -1, 2, 6), "MBwhBst2sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580714496, ("DT", -1, 2, 7), "MBwhBst2sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580976640, ("DT", -1, 2, 8), "MBwhBst2sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581238784, ("DT", -1, 2, 9), "MBwhBst2sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581500928, ("DT", -1, 2, 10), "MBwhBst2sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581763072, ("DT", -1, 2, 11), "MBwhBst2sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(582025216, ("DT", -1, 2, 12), "MBwhBst2sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583335936, ("DT", -1, 3, 1), "MBwhBst3sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583598080, ("DT", -1, 3, 2), "MBwhBst3sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583860224, ("DT", -1, 3, 3), "MBwhBst3sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584122368, ("DT", -1, 3, 4), "MBwhBst3sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584384512, ("DT", -1, 3, 5), "MBwhBst3sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584646656, ("DT", -1, 3, 6), "MBwhBst3sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584908800, ("DT", -1, 3, 7), "MBwhBst3sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585170944, ("DT", -1, 3, 8), "MBwhBst3sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585433088, ("DT", -1, 3, 9), "MBwhBst3sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585695232, ("DT", -1, 3, 10), "MBwhBst3sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585957376, ("DT", -1, 3, 11), "MBwhBst3sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586219520, ("DT", -1, 3, 12), "MBwhBst3sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(574980096, ("DT", 0, 1, 1), "MBwhCst1sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576028672, ("DT", 0, 1, 5), "MBwhCst1sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577077248, ("DT", 0, 1, 9), "MBwhCst1sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575242240, ("DT", 0, 1, 2), "MBwhCst1sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576290816, ("DT", 0, 1, 6), "MBwhCst1sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577339392, ("DT", 0, 1, 10), "MBwhCst1sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575504384, ("DT", 0, 1, 3), "MBwhCst1sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576552960, ("DT", 0, 1, 7), "MBwhCst1sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577601536, ("DT", 0, 1, 11), "MBwhCst1sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575766528, ("DT", 0, 1, 4), "MBwhCst1sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576815104, ("DT", 0, 1, 8), "MBwhCst1sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577863680, ("DT", 0, 1, 12), "MBwhCst1sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579174400, ("DT", 0, 2, 1), "MBwhCst2sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580222976, ("DT", 0, 2, 5), "MBwhCst2sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581271552, ("DT", 0, 2, 9), "MBwhCst2sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579436544, ("DT", 0, 2, 2), "MBwhCst2sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580485120, ("DT", 0, 2, 6), "MBwhCst2sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581533696, ("DT", 0, 2, 10), "MBwhCst2sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579698688, ("DT", 0, 2, 3), "MBwhCst2sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580747264, ("DT", 0, 2, 7), "MBwhCst2sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581795840, ("DT", 0, 2, 11), "MBwhCst2sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579960832, ("DT", 0, 2, 4), "MBwhCst2sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581009408, ("DT", 0, 2, 8), "MBwhCst2sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(582057984, ("DT", 0, 2, 12), "MBwhCst2sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583368704, ("DT", 0, 3, 1), "MBwhCst3sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584417280, ("DT", 0, 3, 5), "MBwhCst3sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585465856, ("DT", 0, 3, 9), "MBwhCst3sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583630848, ("DT", 0, 3, 2), "MBwhCst3sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584679424, ("DT", 0, 3, 6), "MBwhCst3sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585728000, ("DT", 0, 3, 10), "MBwhCst3sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583892992, ("DT", 0, 3, 3), "MBwhCst3sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584941568, ("DT", 0, 3, 7), "MBwhCst3sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585990144, ("DT", 0, 3, 11), "MBwhCst3sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584155136, ("DT", 0, 3, 4), "MBwhCst3sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585203712, ("DT", 0, 3, 8), "MBwhCst3sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586252288, ("DT", 0, 3, 12), "MBwhCst3sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575012864, ("DT", 1, 1, 1), "MBwhDst1sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575275008, ("DT", 1, 1, 2), "MBwhDst1sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575537152, ("DT", 1, 1, 3), "MBwhDst1sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575799296, ("DT", 1, 1, 4), "MBwhDst1sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576061440, ("DT", 1, 1, 5), "MBwhDst1sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576323584, ("DT", 1, 1, 6), "MBwhDst1sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576585728, ("DT", 1, 1, 7), "MBwhDst1sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576847872, ("DT", 1, 1, 8), "MBwhDst1sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577110016, ("DT", 1, 1, 9), "MBwhDst1sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577372160, ("DT", 1, 1, 10), "MBwhDst1sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577634304, ("DT", 1, 1, 11), "MBwhDst1sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577896448, ("DT", 1, 1, 12), "MBwhDst1sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579207168, ("DT", 1, 2, 1), "MBwhDst2sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579469312, ("DT", 1, 2, 2), "MBwhDst2sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579731456, ("DT", 1, 2, 3), "MBwhDst2sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579993600, ("DT", 1, 2, 4), "MBwhDst2sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580255744, ("DT", 1, 2, 5), "MBwhDst2sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580517888, ("DT", 1, 2, 6), "MBwhDst2sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580780032, ("DT", 1, 2, 7), "MBwhDst2sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581042176, ("DT", 1, 2, 8), "MBwhDst2sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581304320, ("DT", 1, 2, 9), "MBwhDst2sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581566464, ("DT", 1, 2, 10), "MBwhDst2sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581828608, ("DT", 1, 2, 11), "MBwhDst2sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(582090752, ("DT", 1, 2, 12), "MBwhDst2sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583401472, ("DT", 1, 3, 1), "MBwhDst3sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583663616, ("DT", 1, 3, 2), "MBwhDst3sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583925760, ("DT", 1, 3, 3), "MBwhDst3sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584187904, ("DT", 1, 3, 4), "MBwhDst3sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584450048, ("DT", 1, 3, 5), "MBwhDst3sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584712192, ("DT", 1, 3, 6), "MBwhDst3sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584974336, ("DT", 1, 3, 7), "MBwhDst3sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585236480, ("DT", 1, 3, 8), "MBwhDst3sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585498624, ("DT", 1, 3, 9), "MBwhDst3sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585760768, ("DT", 1, 3, 10), "MBwhDst3sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586022912, ("DT", 1, 3, 11), "MBwhDst3sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586285056, ("DT", 1, 3, 12), "MBwhDst3sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575045632, ("DT", 2, 1, 1), "MBwhEst1sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575307776, ("DT", 2, 1, 2), "MBwhEst1sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575569920, ("DT", 2, 1, 3), "MBwhEst1sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575832064, ("DT", 2, 1, 4), "MBwhEst1sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576094208, ("DT", 2, 1, 5), "MBwhEst1sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576356352, ("DT", 2, 1, 6), "MBwhEst1sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576618496, ("DT", 2, 1, 7), "MBwhEst1sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576880640, ("DT", 2, 1, 8), "MBwhEst1sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577142784, ("DT", 2, 1, 9), "MBwhEst1sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577404928, ("DT", 2, 1, 10), "MBwhEst1sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577667072, ("DT", 2, 1, 11), "MBwhEst1sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577929216, ("DT", 2, 1, 12), "MBwhEst1sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579239936, ("DT", 2, 2, 1), "MBwhEst2sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579502080, ("DT", 2, 2, 2), "MBwhEst2sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579764224, ("DT", 2, 2, 3), "MBwhEst2sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580026368, ("DT", 2, 2, 4), "MBwhEst2sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580288512, ("DT", 2, 2, 5), "MBwhEst2sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580550656, ("DT", 2, 2, 6), "MBwhEst2sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580812800, ("DT", 2, 2, 7), "MBwhEst2sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581074944, ("DT", 2, 2, 8), "MBwhEst2sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581337088, ("DT", 2, 2, 9), "MBwhEst2sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581599232, ("DT", 2, 2, 10), "MBwhEst2sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581861376, ("DT", 2, 2, 11), "MBwhEst2sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(582123520, ("DT", 2, 2, 12), "MBwhEst2sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583434240, ("DT", 2, 3, 1), "MBwhEst3sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583696384, ("DT", 2, 3, 2), "MBwhEst3sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583958528, ("DT", 2, 3, 3), "MBwhEst3sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584220672, ("DT", 2, 3, 4), "MBwhEst3sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584482816, ("DT", 2, 3, 5), "MBwhEst3sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584744960, ("DT", 2, 3, 6), "MBwhEst3sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585007104, ("DT", 2, 3, 7), "MBwhEst3sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585269248, ("DT", 2, 3, 8), "MBwhEst3sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585531392, ("DT", 2, 3, 9), "MBwhEst3sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585793536, ("DT", 2, 3, 10), "MBwhEst3sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586055680, ("DT", 2, 3, 11), "MBwhEst3sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586317824, ("DT", 2, 3, 12), "MBwhEst3sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587497472, ("DT", -2, 4, 1), "MBwhAst4sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587759616, ("DT", -2, 4, 2), "MBwhAst4sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588021760, ("DT", -2, 4, 3), "MBwhAst4sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588283904, ("DT", -2, 4, 4), "MBwhAst4sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590643200, ("DT", -2, 4, 13), "MBwhAst4sec13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588546048, ("DT", -2, 4, 5), "MBwhAst4sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588808192, ("DT", -2, 4, 6), "MBwhAst4sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589070336, ("DT", -2, 4, 7), "MBwhAst4sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589332480, ("DT", -2, 4, 8), "MBwhAst4sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589594624, ("DT", -2, 4, 9), "MBwhAst4sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589856768, ("DT", -2, 4, 10), "MBwhAst4sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590905344, ("DT", -2, 4, 14), "MBwhAst4sec14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590118912, ("DT", -2, 4, 11), "MBwhAst4sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590381056, ("DT", -2, 4, 12), "MBwhAst4sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587530240, ("DT", -1, 4, 1), "MBwhBst4sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587792384, ("DT", -1, 4, 2), "MBwhBst4sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588054528, ("DT", -1, 4, 3), "MBwhBst4sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588316672, ("DT", -1, 4, 4), "MBwhBst4sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590675968, ("DT", -1, 4, 13), "MBwhBst4sec13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588578816, ("DT", -1, 4, 5), "MBwhBst4sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588840960, ("DT", -1, 4, 6), "MBwhBst4sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589103104, ("DT", -1, 4, 7), "MBwhBst4sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589365248, ("DT", -1, 4, 8), "MBwhBst4sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589627392, ("DT", -1, 4, 9), "MBwhBst4sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589889536, ("DT", -1, 4, 10), "MBwhBst4sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590938112, ("DT", -1, 4, 14), "MBwhBst4sec14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590151680, ("DT", -1, 4, 11), "MBwhBst4sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590413824, ("DT", -1, 4, 12), "MBwhBst4sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587563008, ("DT", 0, 4, 1), "MBwhCst4sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587825152, ("DT", 0, 4, 2), "MBwhCst4sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588087296, ("DT", 0, 4, 3), "MBwhCst4sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588349440, ("DT", 0, 4, 4), "MBwhCst4sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590708736, ("DT", 0, 4, 13), "MBwhCst4sec13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588611584, ("DT", 0, 4, 5), "MBwhCst4sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588873728, ("DT", 0, 4, 6), "MBwhCst4sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589135872, ("DT", 0, 4, 7), "MBwhCst4sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589398016, ("DT", 0, 4, 8), "MBwhCst4sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589660160, ("DT", 0, 4, 9), "MBwhCst4sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589922304, ("DT", 0, 4, 10), "MBwhCst4sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590970880, ("DT", 0, 4, 14), "MBwhCst4sec14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590184448, ("DT", 0, 4, 11), "MBwhCst4sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590446592, ("DT", 0, 4, 12), "MBwhCst4sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587595776, ("DT", 1, 4, 1), "MBwhDst4sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587857920, ("DT", 1, 4, 2), "MBwhDst4sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588120064, ("DT", 1, 4, 3), "MBwhDst4sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588382208, ("DT", 1, 4, 4), "MBwhDst4sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590741504, ("DT", 1, 4, 13), "MBwhDst4sec13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588644352, ("DT", 1, 4, 5), "MBwhDst4sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588906496, ("DT", 1, 4, 6), "MBwhDst4sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589168640, ("DT", 1, 4, 7), "MBwhDst4sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589430784, ("DT", 1, 4, 8), "MBwhDst4sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589692928, ("DT", 1, 4, 9), "MBwhDst4sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589955072, ("DT", 1, 4, 10), "MBwhDst4sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(591003648, ("DT", 1, 4, 14), "MBwhDst4sec14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590217216, ("DT", 1, 4, 11), "MBwhDst4sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590479360, ("DT", 1, 4, 12), "MBwhDst4sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587628544, ("DT", 2, 4, 1), "MBwhEst4sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587890688, ("DT", 2, 4, 2), "MBwhEst4sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588152832, ("DT", 2, 4, 3), "MBwhEst4sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588414976, ("DT", 2, 4, 4), "MBwhEst4sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590774272, ("DT", 2, 4, 13), "MBwhEst4sec13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588677120, ("DT", 2, 4, 5), "MBwhEst4sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588939264, ("DT", 2, 4, 6), "MBwhEst4sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589201408, ("DT", 2, 4, 7), "MBwhEst4sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589463552, ("DT", 2, 4, 8), "MBwhEst4sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589725696, ("DT", 2, 4, 9), "MBwhEst4sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589987840, ("DT", 2, 4, 10), "MBwhEst4sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(591036416, ("DT", 2, 4, 14), "MBwhEst4sec14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590249984, ("DT", 2, 4, 11), "MBwhEst4sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590512128, ("DT", 2, 4, 12), "MBwhEst4sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017672, ("CSC", 1, 1, 1, 1), "MEp11_01"))
reports[-1].posNum = 2933
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00329336, 0.00332903, 0), \
                           ValErr(0.0202114, 0.0822441, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00011189, 8.96079e-05, 0), \
                           914.465, 2933, 2933, -nan)
reports[-1].sigmaresid = ValErr(0.177158, 0.00231309, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00342189, None, -0.00102619, None, -0.00252412, None, -0.000774255, None, -0.00252412, None, -0.000774255, None, -0.00192765, None, -0.000899224, None, -0.00192765, None, -0.000899224, None, 0.177205, None, 0.00624408, None, 0.177205, None, 0.00624408, None)
reports[-1].CovMatrix = ['1.10825e-05','1.70486e-06','-5.53622e-08','1.64357e-09','0','0','0','0','0','1.70486e-06','0.00676409','-9.4179e-08','5.07969e-08','0','0','0','0','0','-5.53622e-08','-9.4179e-08','8.02957e-09','5.21384e-11','0','0','0','0','0','1.64357e-09','5.07969e-08','5.21384e-11','5.35041e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017688, ("CSC", 1, 1, 1, 3), "MEp11_03"))
reports[-1].posNum = 2806
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00123021, 0.00326119, 0), \
                           ValErr(0.061482, 0.0825887, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.59036e-05, 8.72611e-05, 0), \
                           1011.51, 2806, 2806, -nan)
reports[-1].sigmaresid = ValErr(0.168736, 0.00225242, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000285455, None, -0.000824351, None, 0.000879443, None, -0.000678893, None, 0.000879443, None, -0.000678893, None, 0.00353368, None, -0.000639242, None, 0.00353368, None, -0.000639242, None, 0.168757, None, 0.00575259, None, 0.168757, None, 0.00575259, None)
reports[-1].CovMatrix = ['1.06354e-05','9.29182e-06','-6.04827e-08','1.78603e-09','0','0','0','0','0','9.29182e-06','0.00682089','-2.31302e-07','5.44366e-08','0','0','0','0','0','-6.04827e-08','-2.31302e-07','7.6145e-09','4.39002e-11','0','0','0','0','0','1.78603e-09','5.44366e-08','4.39002e-11','5.07338e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017704, ("CSC", 1, 1, 1, 5), "MEp11_05"))
reports[-1].posNum = 2898
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000979368, 0.00340091, 0), \
                           ValErr(-0.00181404, 0.0855814, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.12823e-05, 9.11834e-05, 0), \
                           848.084, 2898, 2898, -nan)
reports[-1].sigmaresid = ValErr(0.18058, 0.00237195, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00153845, None, -0.000676724, None, -0.00110896, None, -0.000511648, None, -0.00110896, None, -0.000511648, None, -0.00653252, None, -0.000404684, None, -0.00653252, None, -0.000404684, None, 0.180581, None, 0.00600404, None, 0.180581, None, 0.00600404, None)
reports[-1].CovMatrix = ['1.15662e-05','5.80078e-06','-5.09226e-08','1.89722e-09','0','0','0','0','0','5.80078e-06','0.00732418','-3.16859e-07','5.29448e-08','0','0','0','0','0','-5.09226e-08','-3.16859e-07','8.31441e-09','4.45008e-11','0','0','0','0','0','1.89722e-09','5.29448e-08','4.45008e-11','5.62614e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017720, ("CSC", 1, 1, 1, 7), "MEp11_07"))
reports[-1].posNum = 2745
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000529412, 0.00334592, 0), \
                           ValErr(0.00982016, 0.0853686, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.05872e-05, 8.96335e-05, 0), \
                           932.293, 2745, 2745, -nan)
reports[-1].sigmaresid = ValErr(0.172291, 0.00232528, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00213649, None, -0.000947148, None, -0.000450659, None, -0.000887757, None, -0.000450659, None, -0.000887757, None, -0.0101865, None, -0.000737241, None, -0.0101865, None, -0.000737241, None, 0.172292, None, 0.00539869, None, 0.172292, None, 0.00539869, None)
reports[-1].CovMatrix = ['1.11952e-05','-5.67721e-06','-5.50665e-08','1.84613e-09','0','0','0','0','0','-5.67721e-06','0.00728779','5.40731e-08','5.45921e-08','0','0','0','0','0','-5.50665e-08','5.40731e-08','8.03416e-09','5.06655e-11','0','0','0','0','0','1.84613e-09','5.45921e-08','5.06655e-11','5.40694e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017736, ("CSC", 1, 1, 1, 9), "MEp11_09"))
reports[-1].posNum = 2674
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000767395, 0.00345997, 0), \
                           ValErr(0.0714004, 0.0876722, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.82652e-06, 9.19035e-05, 0), \
                           885.195, 2674, 2674, -nan)
reports[-1].sigmaresid = ValErr(0.173779, 0.00237633, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00367615, None, -0.000336618, None, -0.000774244, None, -0.000263935, None, -0.000774244, None, -0.000263935, None, -0.000686088, None, -0.000200873, None, -0.000686088, None, -0.000200873, None, 0.1738, None, 0.00544072, None, 0.1738, None, 0.00544072, None)
reports[-1].CovMatrix = ['1.19714e-05','-9.89412e-06','-7.50572e-08','2.01539e-09','0','0','0','0','0','-9.89412e-06','0.00768641','9.04889e-08','5.1015e-08','0','0','0','0','0','-7.50572e-08','9.04889e-08','8.44625e-09','4.88969e-11','0','0','0','0','0','2.01539e-09','5.1015e-08','4.88969e-11','5.64694e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017752, ("CSC", 1, 1, 1, 11), "MEp11_11"))
reports[-1].posNum = 2902
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000522007, 0.0032681, 0), \
                           ValErr(0.0171098, 0.0837218, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.24807e-05, 8.78312e-05, 0), \
                           974.457, 2902, 2902, -nan)
reports[-1].sigmaresid = ValErr(0.172954, 0.00227022, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000254816, None, 0.000183631, None, 0.000682787, None, 0.000186011, None, 0.000682787, None, 0.000186011, None, 0.00469453, None, 0.000321179, None, 0.00469453, None, 0.000321179, None, 0.172958, None, 0.00599424, None, 0.172958, None, 0.00599424, None)
reports[-1].CovMatrix = ['1.06805e-05','-1.21727e-06','-5.35619e-08','1.83348e-09','0','0','0','0','0','-1.21727e-06','0.00700934','-1.62091e-07','5.34393e-08','0','0','0','0','0','-5.35619e-08','-1.62091e-07','7.71431e-09','4.05046e-11','0','0','0','0','0','1.83348e-09','5.34393e-08','4.05046e-11','5.15389e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017768, ("CSC", 1, 1, 1, 13), "MEp11_13"))
reports[-1].posNum = 2834
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00157779, 0.00338436, 0), \
                           ValErr(-0.0138796, 0.0842176, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.91425e-06, 9e-05, 0), \
                           900.253, 2834, 2834, -nan)
reports[-1].sigmaresid = ValErr(0.176118, 0.00233933, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000569354, None, 0.000167501, None, -0.00161059, None, 0.000249262, None, -0.00161059, None, 0.000249262, None, -0.0115437, None, 0.000109015, None, -0.0115437, None, 0.000109015, None, 0.176119, None, 0.00716907, None, 0.176119, None, 0.00716907, None)
reports[-1].CovMatrix = ['1.14539e-05','-1.99433e-06','-6.42001e-08','1.74226e-09','0','0','0','0','0','-1.99433e-06','0.00709261','1.05717e-07','5.53273e-08','0','0','0','0','0','-6.42001e-08','1.05717e-07','8.1e-09','4.40349e-11','0','0','0','0','0','1.74226e-09','5.53273e-08','4.40349e-11','5.47245e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017784, ("CSC", 1, 1, 1, 15), "MEp11_15"))
reports[-1].posNum = 2829
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000222258, 0.00330546, 0), \
                           ValErr(-0.0332153, 0.0819724, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.14447e-05, 8.7808e-05, 0), \
                           967.682, 2829, 2829, -nan)
reports[-1].sigmaresid = ValErr(0.171873, 0.00228494, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00301494, None, 0.000252641, None, 0.000275212, None, 0.000360866, None, 0.000275212, None, 0.000360866, None, 0.00235608, None, 0.000293717, None, 0.00235608, None, 0.000293717, None, 0.171879, None, 0.00532116, None, 0.171879, None, 0.00532116, None)
reports[-1].CovMatrix = ['1.0926e-05','-9.43505e-06','-6.05114e-08','1.53122e-09','0','0','0','0','0','-9.43505e-06','0.00671947','2.03291e-07','5.17576e-08','0','0','0','0','0','-6.05114e-08','2.03291e-07','7.71024e-09','4.84539e-11','0','0','0','0','0','1.53122e-09','5.17576e-08','4.84539e-11','5.22096e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017800, ("CSC", 1, 1, 1, 17), "MEp11_17"))
reports[-1].posNum = 2795
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00179511, 0.00329339, 0), \
                           ValErr(-0.0616753, 0.0813809, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.27627e-05, 8.77382e-05, 0), \
                           969.015, 2795, 2795, -nan)
reports[-1].sigmaresid = ValErr(0.171079, 0.00228818, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-3.55091e-05, None, 0.000671052, None, 0.00120944, None, 0.000658361, None, 0.00120944, None, 0.000658361, None, -0.00779293, None, 0.000717342, None, -0.00779293, None, 0.000717342, None, 0.171123, None, 0.00561637, None, 0.171123, None, 0.00561637, None)
reports[-1].CovMatrix = ['1.08464e-05','-1.38581e-06','-5.37107e-08','1.77035e-09','0','0','0','0','0','-1.38581e-06','0.00662285','6.73475e-08','5.45302e-08','0','0','0','0','0','-5.37107e-08','6.73475e-08','7.69799e-09','4.84401e-11','0','0','0','0','0','1.77035e-09','5.45302e-08','4.84401e-11','5.23578e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017816, ("CSC", 1, 1, 1, 19), "MEp11_19"))
reports[-1].posNum = 2732
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00134503, 0.00336439, 0), \
                           ValErr(-0.0502652, 0.0846906, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.04992e-05, 8.91917e-05, 0), \
                           936.305, 2732, 2732, -nan)
reports[-1].sigmaresid = ValErr(0.171763, 0.00232371, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00438469, None, 0.00015953, None, -0.00114372, None, 0.000112503, None, -0.00114372, None, 0.000112503, None, 0.000327633, None, 3.34536e-05, None, 0.000327633, None, 3.34536e-05, None, 0.171775, None, 0.00490651, None, 0.171775, None, 0.00490651, None)
reports[-1].CovMatrix = ['1.13191e-05','-8.27169e-06','-6.40398e-08','1.90827e-09','0','0','0','0','0','-8.27169e-06','0.0071725','3.06052e-07','6.37685e-08','0','0','0','0','0','-6.40398e-08','3.06052e-07','7.95516e-09','4.72779e-11','0','0','0','0','0','1.90827e-09','6.37685e-08','4.72779e-11','5.39965e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017832, ("CSC", 1, 1, 1, 21), "MEp11_21"))
reports[-1].posNum = 3084
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000193667, 0.00317267, 0), \
                           ValErr(-0.0242304, 0.0778395, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.47028e-05, 8.50923e-05, 0), \
                           1053.86, 3084, 3084, -nan)
reports[-1].sigmaresid = ValErr(0.171932, 0.00218919, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00164356, None, -0.000217894, None, -0.000335345, None, -0.000143657, None, -0.000335345, None, -0.000143657, None, -0.00532494, None, -0.000123157, None, -0.00532494, None, -0.000123157, None, 0.171935, None, 0.00571599, None, 0.171935, None, 0.00571599, None)
reports[-1].CovMatrix = ['1.00659e-05','-6.90197e-06','-5.86629e-08','1.5257e-09','0','0','0','0','0','-6.90197e-06','0.00605898','1.42885e-07','4.90478e-08','0','0','0','0','0','-5.86629e-08','1.42885e-07','7.24069e-09','4.37586e-11','0','0','0','0','0','1.5257e-09','4.90478e-08','4.37586e-11','4.79257e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017848, ("CSC", 1, 1, 1, 23), "MEp11_23"))
reports[-1].posNum = 2610
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00171032, 0.00338225, 0), \
                           ValErr(-0.0342921, 0.0842401, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.10006e-05, 8.85291e-05, 0), \
                           974.265, 2610, 2610, -nan)
reports[-1].sigmaresid = ValErr(0.16659, 0.00230574, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0018586, None, 0.0009346, None, -0.00105817, None, 0.000931667, None, -0.00105817, None, 0.000931667, None, 0.00671578, None, 0.00107251, None, 0.00671578, None, 0.00107251, None, 0.16661, None, 0.00579186, None, 0.16661, None, 0.00579186, None)
reports[-1].CovMatrix = ['1.14396e-05','1.01105e-05','-7.90568e-08','1.87718e-09','0','0','0','0','0','1.01105e-05','0.00709639','-2.02744e-07','6.17466e-08','0','0','0','0','0','-7.90568e-08','-2.02744e-07','7.8374e-09','4.56873e-11','0','0','0','0','0','1.87718e-09','6.17466e-08','4.56873e-11','5.31646e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017864, ("CSC", 1, 1, 1, 25), "MEp11_25"))
reports[-1].posNum = 2859
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000650053, 0.00325365, 0), \
                           ValErr(-0.0350323, 0.0824898, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.29269e-05, 8.56601e-05, 0), \
                           1030.41, 2859, 2859, -nan)
reports[-1].sigmaresid = ValErr(0.168747, 0.00223158, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00162153, None, 9.41759e-05, None, 0.000316038, None, 4.05908e-05, None, 0.000316038, None, 4.05908e-05, None, -0.00323204, None, 0.000259817, None, -0.00323204, None, 0.000259817, None, 0.168766, None, 0.00539522, None, 0.168766, None, 0.00539522, None)
reports[-1].CovMatrix = ['1.05863e-05','2.58258e-05','-6.3765e-08','1.80917e-09','0','0','0','0','0','2.58258e-05','0.00680457','-4.27341e-07','5.90727e-08','0','0','0','0','0','-6.3765e-08','-4.27341e-07','7.33766e-09','4.1457e-11','0','0','0','0','0','1.80917e-09','5.90727e-08','4.1457e-11','4.97994e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017880, ("CSC", 1, 1, 1, 27), "MEp11_27"))
reports[-1].posNum = 2798
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000720337, 0.00335101, 0), \
                           ValErr(0.038463, 0.0854959, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.41174e-06, 8.82839e-05, 0), \
                           956.067, 2798, 2798, -nan)
reports[-1].sigmaresid = ValErr(0.171936, 0.00229841, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00208773, None, 0.000427056, None, 0.000770911, None, 0.000411244, None, 0.000770911, None, 0.000411244, None, 0.00196306, None, 0.000474727, None, 0.00196306, None, 0.000474727, None, 0.171942, None, 0.00561114, None, 0.171942, None, 0.00561114, None)
reports[-1].CovMatrix = ['1.12293e-05','-5.09489e-06','-7.17174e-08','1.67593e-09','0','0','0','0','0','-5.09489e-06','0.00730955','-3.33424e-08','5.36684e-08','0','0','0','0','0','-7.17174e-08','-3.33424e-08','7.79406e-09','4.55928e-11','0','0','0','0','0','1.67593e-09','5.36684e-08','4.55928e-11','5.28271e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017896, ("CSC", 1, 1, 1, 29), "MEp11_29"))
reports[-1].posNum = 2949
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000859398, 0.00320752, 0), \
                           ValErr(-0.0279271, 0.0791207, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.903e-05, 8.61571e-05, 0), \
                           1005.93, 2949, 2949, -nan)
reports[-1].sigmaresid = ValErr(0.172037, 0.0022401, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000612448, None, -0.00137259, None, 0.00100462, None, -0.00150022, None, 0.00100462, None, -0.00150022, None, -0.00683795, None, -0.00126804, None, -0.00683795, None, -0.00126804, None, 0.172044, None, 0.00504084, None, 0.172044, None, 0.00504084, None)
reports[-1].CovMatrix = ['1.02882e-05','-6.39547e-06','-4.28888e-08','1.62477e-09','0','0','0','0','0','-6.39547e-06','0.00626008','2.12819e-07','4.89667e-08','0','0','0','0','0','-4.28888e-08','2.12819e-07','7.42305e-09','4.96503e-11','0','0','0','0','0','1.62477e-09','4.89667e-08','4.96503e-11','5.01804e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017912, ("CSC", 1, 1, 1, 31), "MEp11_31"))
reports[-1].posNum = 2803
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000193496, 0.00340351, 0), \
                           ValErr(0.0424963, 0.0857461, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.77642e-06, 9.08948e-05, 0), \
                           903.127, 2803, 2803, -nan)
reports[-1].sigmaresid = ValErr(0.175321, 0.00234157, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00348469, None, 0.000138603, None, 0.000197342, None, 0.000271438, None, 0.000197342, None, 0.000271438, None, -0.00153292, None, 0.00033533, None, -0.00153292, None, 0.00033533, None, 0.175328, None, 0.0070977, None, 0.175328, None, 0.0070977, None)
reports[-1].CovMatrix = ['1.15839e-05','-6.59977e-06','-7.09769e-08','1.68991e-09','0','0','0','0','0','-6.59977e-06','0.00735239','-1.37035e-07','5.11942e-08','0','0','0','0','0','-7.09769e-08','-1.37035e-07','8.26186e-09','4.70404e-11','0','0','0','0','0','1.68991e-09','5.11942e-08','4.70404e-11','5.48297e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017928, ("CSC", 1, 1, 1, 33), "MEp11_33"))
reports[-1].posNum = 2901
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00178919, 0.00321805, 0), \
                           ValErr(0.0752136, 0.0808623, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.31574e-05, 8.52552e-05, 0), \
                           1029.04, 2901, 2901, -nan)
reports[-1].sigmaresid = ValErr(0.169711, 0.00222802, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00426131, None, -0.000892918, None, 0.00166125, None, -0.000756609, None, 0.00166125, None, -0.000756609, None, 0.00667309, None, -0.000981986, None, 0.00667309, None, -0.000981986, None, 0.169739, None, 0.00585954, None, 0.169739, None, 0.00585954, None)
reports[-1].CovMatrix = ['1.03558e-05','-4.25898e-06','-5.55672e-08','1.66573e-09','0','0','0','0','0','-4.25898e-06','0.00653872','-1.73782e-09','5.12319e-08','0','0','0','0','0','-5.55672e-08','-1.73782e-09','7.26845e-09','4.50846e-11','0','0','0','0','0','1.66573e-09','5.12319e-08','4.50846e-11','4.96408e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017944, ("CSC", 1, 1, 1, 35), "MEp11_35"))
reports[-1].posNum = 2812
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00230969, 0.00331817, 0), \
                           ValErr(0.0515091, 0.0829226, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.04266e-05, 8.76957e-05, 0), \
                           960.918, 2812, 2812, -nan)
reports[-1].sigmaresid = ValErr(0.171932, 0.00229263, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00165786, None, -0.00112402, None, -0.00210806, None, -0.000690634, None, -0.00210806, None, -0.000690634, None, -0.00109622, None, -0.000895793, None, -0.00109622, None, -0.000895793, None, 0.171945, None, 0.00602249, None, 0.171945, None, 0.00602249, None)
reports[-1].CovMatrix = ['1.10102e-05','-6.38085e-06','-6.16488e-08','1.69722e-09','0','0','0','0','0','-6.38085e-06','0.00687615','1.61813e-07','5.30069e-08','0','0','0','0','0','-6.16488e-08','1.61813e-07','7.69053e-09','4.73301e-11','0','0','0','0','0','1.69722e-09','5.30069e-08','4.73301e-11','5.25616e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017680, ("CSC", 1, 1, 1, 2), "MEp11_02"))
reports[-1].posNum = 2907
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00104756, 0.00290581, 0), \
                           ValErr(-0.00196331, 0.0722929, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.68039e-07, 7.72399e-05, 0), \
                           1299.32, 2907, 2907, -nan)
reports[-1].sigmaresid = ValErr(0.154757, 0.00202961, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000280982, None, -0.00269033, None, 0.00104466, None, -0.00212212, None, 0.00104466, None, -0.00212212, None, 0.00132612, None, -0.00233001, None, 0.00132612, None, -0.00233001, None, 0.154757, None, 0.00659563, None, 0.154757, None, 0.00659563, None)
reports[-1].CovMatrix = ['8.44371e-06','-3.20176e-06','-3.48724e-08','1.49539e-09','0','0','0','0','0','-3.20176e-06','0.00522626','1.11297e-07','4.88422e-08','0','0','0','0','0','-3.48724e-08','1.11297e-07','5.966e-09','4.7645e-11','0','0','0','0','0','1.49539e-09','4.88422e-08','4.7645e-11','4.11932e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017696, ("CSC", 1, 1, 1, 4), "MEp11_04"))
reports[-1].posNum = 2820
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000739947, 0.00297458, 0), \
                           ValErr(0.0260326, 0.0745047, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.68523e-06, 7.95679e-05, 0), \
                           1284.65, 2820, 2820, -nan)
reports[-1].sigmaresid = ValErr(0.153432, 0.00204303, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00109168, None, -0.00232885, None, 0.000711817, None, -0.00213088, None, 0.000711817, None, -0.00213088, None, -0.00373132, None, -0.00214535, None, -0.00373132, None, -0.00214535, None, 0.153437, None, 0.00520387, None, 0.153437, None, 0.00520387, None)
reports[-1].CovMatrix = ['8.8481e-06','2.97162e-06','-5.61641e-08','1.48372e-09','0','0','0','0','0','2.97162e-06','0.00555095','2.06671e-08','5.16221e-08','0','0','0','0','0','-5.61641e-08','2.06671e-08','6.33104e-09','4.53783e-11','0','0','0','0','0','1.48372e-09','5.16221e-08','4.53783e-11','4.17398e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017712, ("CSC", 1, 1, 1, 6), "MEp11_06"))
reports[-1].posNum = 2907
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000115483, 0.00293789, 0), \
                           ValErr(0.0204676, 0.0729908, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.34432e-06, 7.84051e-05, 0), \
                           1295.29, 2907, 2907, -nan)
reports[-1].sigmaresid = ValErr(0.154972, 0.00203243, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00154049, None, -0.00164586, None, 0.000188564, None, -0.00140927, None, 0.000188564, None, -0.00140927, None, -0.00771181, None, -0.0012971, None, -0.00771181, None, -0.0012971, None, 0.154974, None, 0.00594318, None, 0.154974, None, 0.00594318, None)
reports[-1].CovMatrix = ['8.6312e-06','-1.2033e-06','-4.7619e-08','1.55704e-09','0','0','0','0','0','-1.2033e-06','0.00532766','-1.15522e-07','5.06571e-08','0','0','0','0','0','-4.7619e-08','-1.15522e-07','6.14735e-09','3.99874e-11','0','0','0','0','0','1.55704e-09','5.06571e-08','3.99874e-11','4.13076e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017728, ("CSC", 1, 1, 1, 8), "MEp11_08"))
reports[-1].posNum = 2963
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000471275, 0.00325746, 0), \
                           ValErr(0.0279809, 0.0910873, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.12085e-05, 8.72491e-05, 0), \
                           1318.99, 2963, 2963, -nan)
reports[-1].sigmaresid = ValErr(0.155037, 0.00201676, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00158774, None, -0.00136667, None, 6.17474e-05, None, -0.00113934, None, 6.17474e-05, None, -0.00113934, None, -0.00308075, None, -0.00125239, None, -0.00308075, None, -0.00125239, None, 0.155052, None, 0.0056984, None, 0.155052, None, 0.0056984, None)
reports[-1].CovMatrix = ['1.0611e-05','7.43085e-05','-1.08755e-07','-1.28474e-07','0','0','0','0','0','7.43085e-05','0.00829689','-2.24709e-06','-4.90825e-06','0','0','0','0','0','-1.08755e-07','-2.24709e-06','7.6124e-09','3.72836e-09','0','0','0','0','0','-1.28474e-07','-4.90825e-06','3.72836e-09','4.06733e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017744, ("CSC", 1, 1, 1, 10), "MEp11_10"))
reports[-1].posNum = 2877
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0010269, 0.00292798, 0), \
                           ValErr(0.0382067, 0.0722574, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.01958e-05, 7.90015e-05, 0), \
                           1304.77, 2877, 2877, -nan)
reports[-1].sigmaresid = ValErr(0.153745, 0.00202682, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000800736, None, -0.00118605, None, -0.00112373, None, -0.00104566, None, -0.00112373, None, -0.00104566, None, -0.00609352, None, -0.00102555, None, -0.00609352, None, -0.00102555, None, 0.153754, None, 0.00557642, None, 0.153754, None, 0.00557642, None)
reports[-1].CovMatrix = ['8.57305e-06','2.29478e-06','-4.71202e-08','1.69726e-09','0','0','0','0','0','2.29478e-06','0.00522114','3.14258e-08','5.08796e-08','0','0','0','0','0','-4.71202e-08','3.14258e-08','6.24124e-09','4.06372e-11','0','0','0','0','0','1.69726e-09','5.08796e-08','4.06372e-11','4.10802e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017760, ("CSC", 1, 1, 1, 12), "MEp11_12"))
reports[-1].posNum = 2302
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00150414, 0.00352844, 0), \
                           ValErr(0.0105921, 0.0788631, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.29088e-05, 8.70445e-05, 0), \
                           1067.5, 2302, 2302, -nan)
reports[-1].sigmaresid = ValErr(0.152179, 0.0022427, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000324778, None, -0.000237612, None, 0.000588198, None, -0.0002882, None, 0.000588198, None, -0.0002882, None, 0.00526615, None, -0.000470211, None, 0.00526615, None, -0.000470211, None, 0.152203, None, 0.00577364, None, 0.152203, None, 0.00577364, None)
reports[-1].CovMatrix = ['1.24499e-05','-5.7895e-05','-1.25531e-07','1.24937e-09','0','0','0','0','0','-5.7895e-05','0.00621939','8.65739e-07','5.33994e-08','0','0','0','0','0','-1.25531e-07','8.65739e-07','7.57674e-09','4.74975e-11','0','0','0','0','0','1.24937e-09','5.33994e-08','4.74975e-11','5.02972e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017776, ("CSC", 1, 1, 1, 14), "MEp11_14"))
reports[-1].posNum = 2916
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000709467, 0.00296266, 0), \
                           ValErr(0.0264275, 0.0749319, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.10243e-05, 7.79393e-05, 0), \
                           1271.34, 2916, 2916, -nan)
reports[-1].sigmaresid = ValErr(0.156464, 0.00204882, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000226575, None, -9.14667e-05, None, 0.000572425, None, 3.84436e-05, None, 0.000572425, None, 3.84436e-05, None, 0.00459134, None, -3.82601e-05, None, 0.00459134, None, -3.82601e-05, None, 0.15647, None, 0.00589184, None, 0.15647, None, 0.00589184, None)
reports[-1].CovMatrix = ['8.77737e-06','-6.30919e-06','-4.78013e-08','1.45123e-09','0','0','0','0','0','-6.30919e-06','0.00561479','7.64778e-08','4.85822e-08','0','0','0','0','0','-4.78013e-08','7.64778e-08','6.07454e-09','4.39226e-11','0','0','0','0','0','1.45123e-09','4.85822e-08','4.39226e-11','4.19766e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017792, ("CSC", 1, 1, 1, 16), "MEp11_16"))
reports[-1].posNum = 2827
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00227078, 0.00290808, 0), \
                           ValErr(0.0055105, 0.0726688, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.31608e-05, 7.66356e-05, 0), \
                           1324.02, 2827, 2827, -nan)
reports[-1].sigmaresid = ValErr(0.15148, 0.0020145, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00256564, None, 0.000947444, None, 0.00179536, None, 0.000904294, None, 0.00179536, None, 0.000904294, None, 0.00489372, None, 0.000738553, None, 0.00489372, None, 0.000738553, None, 0.151501, None, 0.00594084, None, 0.151501, None, 0.00594084, None)
reports[-1].CovMatrix = ['8.45695e-06','-3.9975e-06','-4.44663e-08','1.62083e-09','0','0','0','0','0','-3.9975e-06','0.00528076','-4.22834e-08','4.97779e-08','0','0','0','0','0','-4.44663e-08','-4.22834e-08','5.87302e-09','4.32914e-11','0','0','0','0','0','1.62083e-09','4.97779e-08','4.32914e-11','4.0582e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017808, ("CSC", 1, 1, 1, 18), "MEp11_18"))
reports[-1].posNum = 3047
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00254162, 0.00282022, 0), \
                           ValErr(-0.0280638, 0.0709672, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.18883e-05, 7.51422e-05, 0), \
                           1429.04, 3047, 3047, -nan)
reports[-1].sigmaresid = ValErr(0.151384, 0.00193923, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0034123, None, 0.000493514, None, 0.00189457, None, 0.000327259, None, 0.00189457, None, 0.000327259, None, 0.00720323, None, 0.000238817, None, 0.00720323, None, 0.000238817, None, 0.15141, None, 0.00578642, None, 0.15141, None, 0.00578642, None)
reports[-1].CovMatrix = ['7.95365e-06','-3.86014e-06','-4.92539e-08','1.38079e-09','0','0','0','0','0','-3.86014e-06','0.00503634','1.17362e-08','4.21993e-08','0','0','0','0','0','-4.92539e-08','1.17362e-08','5.64635e-09','3.69823e-11','0','0','0','0','0','1.38079e-09','4.21993e-08','3.69823e-11','3.76062e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017824, ("CSC", 1, 1, 1, 20), "MEp11_20"))
reports[-1].posNum = 2859
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000913338, 0.00362987, 0), \
                           ValErr(0.0480753, 0.0734386, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.87653e-05, 9.61138e-05, 0), \
                           1433.14, 2859, 2859, -nan)
reports[-1].sigmaresid = ValErr(0.146573, 0.00214569, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00020567, None, 0.00203598, None, -0.00120351, None, 0.00205117, None, -0.00120351, None, 0.00205117, None, -0.0052826, None, 0.00210717, None, -0.0052826, None, 0.00210717, None, 0.146592, None, 0.00580985, None, 0.146592, None, 0.00580985, None)
reports[-1].CovMatrix = ['1.3176e-05','-8.05804e-06','-1.88577e-07','-1.36233e-07','0','0','0','0','0','-8.05804e-06','0.00539322','5.17263e-07','-2.18012e-05','0','0','0','0','0','-1.88577e-07','5.17263e-07','9.23786e-09','-2.84929e-09','0','0','0','0','0','-1.36233e-07','-2.18012e-05','-2.84929e-09','4.60397e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017840, ("CSC", 1, 1, 1, 22), "MEp11_22"))
reports[-1].posNum = 3052
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000977197, 0.00288387, 0), \
                           ValErr(-0.0212021, 0.0731056, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.39688e-05, 7.62089e-05, 0), \
                           1345.8, 3052, 3052, -nan)
reports[-1].sigmaresid = ValErr(0.15569, 0.00199276, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000425641, None, 0.000965997, None, -0.00134095, None, 0.0013435, None, -0.00134095, None, 0.0013435, None, -0.000775668, None, 0.00114863, None, -0.000775668, None, 0.00114863, None, 0.1557, None, 0.00624729, None, 0.1557, None, 0.00624729, None)
reports[-1].CovMatrix = ['8.3167e-06','-3.63227e-06','-4.65173e-08','1.39248e-09','0','0','0','0','0','-3.63227e-06','0.00534443','4.44429e-08','4.30191e-08','0','0','0','0','0','-4.65173e-08','4.44429e-08','5.8078e-09','4.25328e-11','0','0','0','0','0','1.39248e-09','4.30191e-08','4.25328e-11','3.97111e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017856, ("CSC", 1, 1, 1, 24), "MEp11_24"))
reports[-1].posNum = 2870
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00229813, 0.0035418, 0), \
                           ValErr(0.0216728, 0.118132, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.7101e-05, 0.000108711, 0), \
                           1379.94, 2870, 2870, -nan)
reports[-1].sigmaresid = ValErr(0.149604, 0.00198771, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00318187, None, 0.000793801, None, 0.00173255, None, 0.000769698, None, 0.00173255, None, 0.000769698, None, 0.00091687, None, 0.000827987, None, 0.00091687, None, 0.000827987, None, 0.149623, None, 0.00590978, None, 0.149623, None, 0.00590978, None)
reports[-1].CovMatrix = ['1.25443e-05','1.28091e-05','1.07799e-07','3.07892e-09','0','0','0','0','0','1.28091e-05','0.0139551','-2.1326e-07','1.15169e-06','0','0','0','0','0','1.07799e-07','-2.1326e-07','1.1818e-08','1.44103e-10','0','0','0','0','0','3.07892e-09','1.15169e-06','1.44103e-10','3.95099e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017872, ("CSC", 1, 1, 1, 26), "MEp11_26"))
reports[-1].posNum = 3286
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000117695, 0.00326667, 0), \
                           ValErr(0.0136686, 0.0983215, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.48178e-05, 8.6143e-05, 0), \
                           1509.31, 3286, 3286, -nan)
reports[-1].sigmaresid = ValErr(0.152856, 0.00201371, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00136373, None, -0.000467942, None, 1.03861e-06, None, -0.000451856, None, 1.03861e-06, None, -0.000451856, None, -0.000624958, None, -0.000471258, None, -0.000624958, None, -0.000471258, None, 0.152858, None, 0.00613569, None, 0.152858, None, 0.00613569, None)
reports[-1].CovMatrix = ['1.06711e-05','-6.32569e-05','-1.15574e-07','-5.22546e-07','0','0','0','0','0','-6.32569e-05','0.00966712','1.952e-07','-2.89611e-05','0','0','0','0','0','-1.15574e-07','1.952e-07','7.42062e-09','2.50478e-08','0','0','0','0','0','-5.22546e-07','-2.89611e-05','2.50478e-08','4.05502e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017888, ("CSC", 1, 1, 1, 28), "MEp11_28"))
reports[-1].posNum = 2757
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00148184, 0.00308272, 0), \
                           ValErr(0.0104678, 0.111754, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.45889e-05, 8.092e-05, 0), \
                           1283.16, 2757, 2757, -nan)
reports[-1].sigmaresid = ValErr(0.151925, 0.00220561, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00473739, None, 0.00434345, None, 0.00129287, None, 0.00402801, None, 0.00129287, None, 0.00402801, None, -0.00112843, None, 0.00421617, None, -0.00112843, None, 0.00421617, None, 0.15193, None, 0.0057963, None, 0.15193, None, 0.0057963, None)
reports[-1].CovMatrix = ['9.50316e-06','-2.42659e-05','-6.45589e-08','-6.5956e-07','0','0','0','0','0','-2.42659e-05','0.012489','1.09251e-06','-7.24393e-06','0','0','0','0','0','-6.45589e-08','1.09251e-06','6.54804e-09','1.20845e-08','0','0','0','0','0','-6.5956e-07','-7.24393e-06','1.20845e-08','4.86471e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017904, ("CSC", 1, 1, 1, 30), "MEp11_30"))
reports[-1].posNum = 2935
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00139767, 0.00332762, 0), \
                           ValErr(-0.0244371, 0.111764, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.77913e-05, 0.000102522, 0), \
                           1413.88, 2935, 2935, -nan)
reports[-1].sigmaresid = ValErr(0.149467, 0.001966, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00474948, None, -0.000575245, None, 0.00125496, None, -0.000634791, None, 0.00125496, None, -0.000634791, None, 0.00263819, None, -0.000718492, None, 0.00263819, None, -0.000718492, None, 0.149473, None, 0.00544211, None, 0.149473, None, 0.00544211, None)
reports[-1].CovMatrix = ['1.1073e-05','-2.27786e-05','-1.66279e-07','5.04934e-09','0','0','0','0','0','-2.27786e-05','0.0124912','-4.60014e-07','-1.74937e-06','0','0','0','0','0','-1.66279e-07','-4.60014e-07','1.05108e-08','2.36213e-11','0','0','0','0','0','5.04934e-09','-1.74937e-06','2.36213e-11','3.86516e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017920, ("CSC", 1, 1, 1, 32), "MEp11_32"))
reports[-1].posNum = 2894
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00309783, 0.00357984, 0), \
                           ValErr(-0.0109382, 0.110474, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.13561e-05, 9.43419e-05, 0), \
                           1361.08, 2894, 2894, -nan)
reports[-1].sigmaresid = ValErr(0.151185, 0.00201834, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00218796, None, -0.000433302, None, 0.00262902, None, -0.000312773, None, 0.00262902, None, -0.000312773, None, -0.000588639, None, -0.00027425, None, -0.000588639, None, -0.00027425, None, 0.151197, None, 0.00571325, None, 0.151197, None, 0.00571325, None)
reports[-1].CovMatrix = ['1.28153e-05','3.14274e-06','-1.70393e-07','7.08337e-08','0','0','0','0','0','3.14274e-06','0.0122046','5.96778e-08','-2.93418e-05','0','0','0','0','0','-1.70393e-07','5.96778e-08','8.90039e-09','-2.01071e-09','0','0','0','0','0','7.08337e-08','-2.93418e-05','-2.01071e-09','4.07371e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017936, ("CSC", 1, 1, 1, 34), "MEp11_34"))
reports[-1].posNum = 2933
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-9.49866e-05, 0.00356451, 0), \
                           ValErr(0.0438102, 0.0715409, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.88585e-05, 9.58669e-05, 0), \
                           1380.19, 2933, 2933, -nan)
reports[-1].sigmaresid = ValErr(0.151146, 0.00197394, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00192077, None, -0.0031503, None, -0.000404503, None, -0.00315304, None, -0.000404503, None, -0.00315304, None, 0.00754641, None, -0.00329474, None, 0.00754641, None, -0.00329474, None, 0.151159, None, 0.00540412, None, 0.151159, None, 0.00540412, None)
reports[-1].CovMatrix = ['1.27057e-05','3.0796e-06','-1.70205e-07','3.45091e-08','0','0','0','0','0','3.0796e-06','0.0051181','2.73448e-07','-3.7609e-08','0','0','0','0','0','-1.70205e-07','2.73448e-07','9.19046e-09','-9.61018e-10','0','0','0','0','0','3.45091e-08','-3.7609e-08','-9.61018e-10','3.89645e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017952, ("CSC", 1, 1, 1, 36), "MEp11_36"))
reports[-1].posNum = 2834
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00153723, 0.00289713, 0), \
                           ValErr(0.0589085, 0.0751199, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.53916e-05, 7.77687e-05, 0), \
                           1314.77, 2834, 2834, -nan)
reports[-1].sigmaresid = ValErr(0.152151, 0.00202094, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000510975, None, -0.00147642, None, -0.00169322, None, -0.00117552, None, -0.00169322, None, -0.00117552, None, 0.000177795, None, -0.00112975, None, 0.000177795, None, -0.00112975, None, 0.152172, None, 0.0061704, None, 0.152172, None, 0.0061704, None)
reports[-1].CovMatrix = ['8.39337e-06','1.00227e-06','-3.68624e-08','1.60591e-09','0','0','0','0','0','1.00227e-06','0.00564299','-1.28503e-07','5.28522e-08','0','0','0','0','0','-3.68624e-08','-1.28503e-07','6.04796e-09','4.27963e-11','0','0','0','0','0','1.60591e-09','5.28522e-08','4.27963e-11','4.08421e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018184, ("CSC", 1, 1, 2, 1), "MEp12_01"))
reports[-1].posNum = 1240
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00911754, 0.0154635, 0), \
                           ValErr(0.151617, 0.375714, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.31178e-05, 0.000314804, 0), \
                           -899.117, 1240, 1240, -nan)
reports[-1].sigmaresid = ValErr(0.499656, 0.0100334, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0102107, None, -0.000516071, None, 0.0115578, None, -0.000815885, None, 0.0115578, None, -0.000815885, None, -0.00102762, None, -0.000472139, None, -0.00102762, None, -0.000472139, None, 0.499694, None, 0.00829854, None, 0.499694, None, 0.00829854, None)
reports[-1].CovMatrix = ['0.000239119','-0.00117169','-1.69129e-06','3.17001e-08','0','0','0','0','0','-0.00117169','0.141161','2.92674e-06','1.30255e-06','0','0','0','0','0','-1.69129e-06','2.92674e-06','9.91016e-08','9.1989e-10','0','0','0','0','0','3.17001e-08','1.30255e-06','9.1989e-10','0.00010067','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018200, ("CSC", 1, 1, 2, 3), "MEp12_03"))
reports[-1].posNum = 1446
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00431308, 0.0135118, 0), \
                           ValErr(0.00745416, 0.312578, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.52584e-05, 0.000283215, 0), \
                           -891.613, 1446, 1446, -nan)
reports[-1].sigmaresid = ValErr(0.448266, 0.00833518, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0062616, None, -0.000549826, None, 0.00256889, None, -0.000554485, None, 0.00256889, None, -0.000554485, None, -0.00722412, None, -0.000436471, None, -0.00722412, None, -0.000436471, None, 0.448293, None, 0.00593434, None, 0.448293, None, 0.00593434, None)
reports[-1].CovMatrix = ['0.000182569','5.98263e-05','-1.87016e-06','2.08343e-08','0','0','0','0','0','5.98263e-05','0.0977051','-2.31159e-06','9.77511e-07','0','0','0','0','0','-1.87016e-06','-2.31159e-06','8.02108e-08','5.80656e-10','0','0','0','0','0','2.08343e-08','9.77511e-07','5.80656e-10','6.94756e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018216, ("CSC", 1, 1, 2, 5), "MEp12_05"))
reports[-1].posNum = 1501
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00733213, 0.0137206, 0), \
                           ValErr(-0.218337, 0.33552, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000144577, 0.00028173, 0), \
                           -1073.63, 1501, 1501, -nan)
reports[-1].sigmaresid = ValErr(0.494779, 0.00903054, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00464273, None, -0.00250114, None, -0.00463164, None, -0.00248631, None, -0.00463164, None, -0.00248631, None, -0.0265545, None, -0.00245878, None, -0.0265545, None, -0.00245878, None, 0.494886, None, 0.00676132, None, 0.494886, None, 0.00676132, None)
reports[-1].CovMatrix = ['0.000188255','4.97759e-05','-1.41188e-06','3.91879e-08','0','0','0','0','0','4.97759e-05','0.112574','1.17239e-06','1.36533e-06','0','0','0','0','0','-1.41188e-06','1.17239e-06','7.93717e-08','6.99525e-10','0','0','0','0','0','3.91879e-08','1.36533e-06','6.99525e-10','8.15511e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018232, ("CSC", 1, 1, 2, 7), "MEp12_07"))
reports[-1].posNum = 1569
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00152559, 0.0136043, 0), \
                           ValErr(0.0965373, 0.327009, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.72268e-05, 0.000289992, 0), \
                           -1115.36, 1569, 1569, -nan)
reports[-1].sigmaresid = ValErr(0.492597, 0.00879355, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0021622, None, 0.000433132, None, -0.00225928, None, 0.000391128, None, -0.00225928, None, 0.000391128, None, -0.0107224, None, 0.000480617, None, -0.0107224, None, 0.000480617, None, 0.492613, None, 0.00619464, None, 0.492613, None, 0.00619464, None)
reports[-1].CovMatrix = ['0.000185078','-2.4214e-06','-1.59928e-06','3.0139e-08','0','0','0','0','0','-2.4214e-06','0.106935','1.82139e-06','1.20929e-06','0','0','0','0','0','-1.59928e-06','1.82139e-06','8.40956e-08','7.40665e-10','0','0','0','0','0','3.0139e-08','1.20929e-06','7.40665e-10','7.73269e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018248, ("CSC", 1, 1, 2, 9), "MEp12_09"))
reports[-1].posNum = 1538
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00518229, 0.013919, 0), \
                           ValErr(0.104348, 0.327971, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000192365, 0.000284684, 0), \
                           -1075.75, 1538, 1538, -nan)
reports[-1].sigmaresid = ValErr(0.487001, 0.00878083, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0129239, None, -0.000263197, None, 0.00102225, None, 0.000125656, None, 0.00102225, None, 0.000125656, None, -0.0145143, None, 1.53818e-05, None, -0.0145143, None, 1.53818e-05, None, 0.487089, None, 0.0071953, None, 0.487089, None, 0.0071953, None)
reports[-1].CovMatrix = ['0.00019374','-6.70727e-05','-1.78828e-06','3.00778e-08','0','0','0','0','0','-6.70727e-05','0.107565','-1.0163e-06','1.14235e-06','0','0','0','0','0','-1.78828e-06','-1.0163e-06','8.1045e-08','6.15201e-10','0','0','0','0','0','3.00778e-08','1.14235e-06','6.15201e-10','7.71034e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018264, ("CSC", 1, 1, 2, 11), "MEp12_11"))
reports[-1].posNum = 1612
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000537594, 0.0130992, 0), \
                           ValErr(-0.122784, 0.315921, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.76709e-05, 0.000277082, 0), \
                           -1112.46, 1612, 1612, -nan)
reports[-1].sigmaresid = ValErr(0.482476, 0.00849727, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0184047, None, -0.000907858, None, -0.0011155, None, -0.000779258, None, -0.0011155, None, -0.000779258, None, -0.00100968, None, -0.000786158, None, -0.00100968, None, -0.000786158, None, 0.482516, None, 0.00630611, None, 0.482516, None, 0.00630611, None)
reports[-1].CovMatrix = ['0.000171588','0.000161771','-1.43919e-06','3.16583e-08','0','0','0','0','0','0.000161771','0.0998063','-1.03178e-06','1.12578e-06','0','0','0','0','0','-1.43919e-06','-1.03178e-06','7.67746e-08','5.95629e-10','0','0','0','0','0','3.16583e-08','1.12578e-06','5.95629e-10','7.22039e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018280, ("CSC", 1, 1, 2, 13), "MEp12_13"))
reports[-1].posNum = 1424
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00821838, 0.0135633, 0), \
                           ValErr(0.357366, 0.371946, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000184217, 0.000279764, 0), \
                           -954.494, 1424, 1424, -nan)
reports[-1].sigmaresid = ValErr(0.472998, 0.00886297, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0129493, None, 0.000594696, None, 0.00678556, None, 0.00072206, None, 0.00678556, None, 0.00072206, None, -0.00382251, None, 0.000783374, None, -0.00382251, None, 0.000783374, None, 0.473223, None, 0.00584912, None, 0.473223, None, 0.00584912, None)
reports[-1].CovMatrix = ['0.000183962','-0.000628669','-1.35229e-06','2.52259e-08','0','0','0','0','0','-0.000628669','0.138344','-3.78241e-06','1.25075e-06','0','0','0','0','0','-1.35229e-06','-3.78241e-06','7.8268e-08','7.44515e-10','0','0','0','0','0','2.52259e-08','1.25075e-06','7.44515e-10','7.85527e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018296, ("CSC", 1, 1, 2, 15), "MEp12_15"))
reports[-1].posNum = 1517
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0124168, 0.0132771, 0), \
                           ValErr(0.196292, 0.367294, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000246388, 0.000282191, 0), \
                           -1033.13, 1517, 1517, -nan)
reports[-1].sigmaresid = ValErr(0.478114, 0.00868005, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00325161, None, -0.00182301, None, 0.00735205, None, -0.00155537, None, 0.00735205, None, -0.00155537, None, 0.000946739, None, -0.00154989, None, 0.000946739, None, -0.00154989, None, 0.478282, None, 0.00624992, None, 0.478282, None, 0.00624992, None)
reports[-1].CovMatrix = ['0.000176281','0.000576131','-1.35263e-06','3.79235e-08','0','0','0','0','0','0.000576131','0.134905','1.06405e-06','1.49122e-06','0','0','0','0','0','-1.35263e-06','1.06405e-06','7.96317e-08','6.86672e-10','0','0','0','0','0','3.79235e-08','1.49122e-06','6.86672e-10','7.53437e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018312, ("CSC", 1, 1, 2, 17), "MEp12_17"))
reports[-1].posNum = 1556
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00386669, 0.0129257, 0), \
                           ValErr(-0.152233, 0.314538, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.32926e-05, 0.000272209, 0), \
                           -994.87, 1556, 1556, -nan)
reports[-1].sigmaresid = ValErr(0.458606, 0.00822089, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0252955, None, 0.00294005, None, -0.00242166, None, 0.00283737, None, -0.00242166, None, 0.00283737, None, 0.00429358, None, 0.00292729, None, 0.00429358, None, 0.00292729, None, 0.458651, None, 0.00574741, None, 0.458651, None, 0.00574741, None)
reports[-1].CovMatrix = ['0.000167073','2.49479e-05','-1.53576e-06','2.66407e-08','0','0','0','0','0','2.49479e-05','0.098934','2.95974e-06','1.0453e-06','0','0','0','0','0','-1.53576e-06','2.95974e-06','7.40977e-08','5.85021e-10','0','0','0','0','0','2.66407e-08','1.0453e-06','5.85021e-10','6.75833e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018328, ("CSC", 1, 1, 2, 19), "MEp12_19"))
reports[-1].posNum = 1597
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000301661, 0.0125718, 0), \
                           ValErr(-0.0963893, 0.314227, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000127922, 0.000256213, 0), \
                           -1063.36, 1597, 1597, -nan)
reports[-1].sigmaresid = ValErr(0.470911, 0.00833241, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0158305, None, -0.000848357, None, 0.00182085, None, -0.000890858, None, 0.00182085, None, -0.000890858, None, 0.00297246, None, -0.00085976, None, 0.00297246, None, -0.00085976, None, 0.470963, None, 0.00592058, None, 0.470963, None, 0.00592058, None)
reports[-1].CovMatrix = ['0.00015805','-0.000135833','-1.12141e-06','2.767e-08','0','0','0','0','0','-0.000135833','0.0987386','4.52604e-06','1.07213e-06','0','0','0','0','0','-1.12141e-06','4.52604e-06','6.56452e-08','6.38274e-10','0','0','0','0','0','2.767e-08','1.07213e-06','6.38274e-10','6.94295e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018344, ("CSC", 1, 1, 2, 21), "MEp12_21"))
reports[-1].posNum = 744
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00720349, 0.019889, 0), \
                           ValErr(0.0390582, 0.453347, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.42435e-05, 0.000404549, 0), \
                           -525.303, 744, 744, -nan)
reports[-1].sigmaresid = ValErr(0.490247, 0.0127096, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0107603, None, -0.000302908, None, 0.00898015, None, -0.000338826, None, 0.00898015, None, -0.000338826, None, 0.0345864, None, -0.000144644, None, 0.0345864, None, -0.000144644, None, 0.490248, None, 0.00591564, None, 0.490248, None, 0.00591564, None)
reports[-1].CovMatrix = ['0.000395571','0.000996459','-3.35939e-06','6.52495e-08','0','0','0','0','0','0.000996459','0.205523','-6.82511e-06','2.7884e-06','0','0','0','0','0','-3.35939e-06','-6.82511e-06','1.6366e-07','1.27343e-09','0','0','0','0','0','6.52495e-08','2.7884e-06','1.27343e-09','0.000161537','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018360, ("CSC", 1, 1, 2, 23), "MEp12_23"))
reports[-1].posNum = 1654
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00100879, 0.0122383, 0), \
                           ValErr(0.04324, 0.295706, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.78176e-05, 0.00025409, 0), \
                           -1083.59, 1654, 1654, -nan)
reports[-1].sigmaresid = ValErr(0.465889, 0.00810026, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0182896, None, 0.00126724, None, -0.00261188, None, 0.00103068, None, -0.00261188, None, 0.00103068, None, 0.00485348, None, 0.00130399, None, 0.00485348, None, 0.00130399, None, 0.465913, None, 0.00641802, None, 0.465913, None, 0.00641802, None)
reports[-1].CovMatrix = ['0.000149777','-0.00012834','-1.09122e-06','2.58337e-08','0','0','0','0','0','-0.00012834','0.0874421','1.95119e-06','9.34516e-07','0','0','0','0','0','-1.09122e-06','1.95119e-06','6.45616e-08','5.84846e-10','0','0','0','0','0','2.58337e-08','9.34516e-07','5.84846e-10','6.56145e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018376, ("CSC", 1, 1, 2, 25), "MEp12_25"))
reports[-1].posNum = 1655
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00537857, 0.0132888, 0), \
                           ValErr(0.0750881, 0.321702, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.82135e-05, 0.000276436, 0), \
                           -1170.82, 1655, 1655, -nan)
reports[-1].sigmaresid = ValErr(0.490921, 0.00853314, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000969953, None, 0.00153014, None, -0.00730987, None, 0.00165946, None, -0.00730987, None, 0.00165946, None, -0.00481412, None, 0.00156206, None, -0.00481412, None, 0.00156206, None, 0.490937, None, 0.00702405, None, 0.490937, None, 0.00702405, None)
reports[-1].CovMatrix = ['0.000176594','-6.76899e-05','-1.53671e-06','3.52175e-08','0','0','0','0','0','-6.76899e-05','0.103492','-8.4738e-07','1.15579e-06','0','0','0','0','0','-1.53671e-06','-8.4738e-07','7.64171e-08','5.52374e-10','0','0','0','0','0','3.52175e-08','1.15579e-06','5.52374e-10','7.28149e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018392, ("CSC", 1, 1, 2, 27), "MEp12_27"))
reports[-1].posNum = 1404
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0200488, 0.0145543, 0), \
                           ValErr(-0.209177, 0.340293, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000100217, 0.00028826, 0), \
                           -950.973, 1404, 1404, -nan)
reports[-1].sigmaresid = ValErr(0.476348, 0.00898927, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00220777, None, -0.0026286, None, 0.0184121, None, -0.00230385, None, 0.0184121, None, -0.00230385, None, 0.0314242, None, -0.00267155, None, 0.0314242, None, -0.00267155, None, 0.476439, None, 0.00615348, None, 0.476439, None, 0.00615348, None)
reports[-1].CovMatrix = ['0.000211827','0.000611303','-2.01203e-06','3.78054e-08','0','0','0','0','0','0.000611303','0.115799','-8.13798e-06','1.31159e-06','0','0','0','0','0','-2.01203e-06','-8.13798e-06','8.30936e-08','5.22713e-10','0','0','0','0','0','3.78054e-08','1.31159e-06','5.22713e-10','8.08075e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018408, ("CSC", 1, 1, 2, 29), "MEp12_29"))
reports[-1].posNum = 1605
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00619484, 0.0130313, 0), \
                           ValErr(0.089003, 0.306993, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000249959, 0.000277772, 0), \
                           -1064.02, 1605, 1605, -nan)
reports[-1].sigmaresid = ValErr(0.469542, 0.00828746, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000586541, None, 0.000208128, None, -0.000989838, None, 0.000411542, None, -0.000989838, None, 0.000411542, None, 0.00377999, None, 0.000405902, None, 0.00377999, None, 0.000405902, None, 0.469666, None, 0.00688367, None, 0.469666, None, 0.00688367, None)
reports[-1].CovMatrix = ['0.000169814','-0.00031449','-1.57691e-06','2.30913e-08','0','0','0','0','0','-0.00031449','0.0942447','8.34862e-06','1.03743e-06','0','0','0','0','0','-1.57691e-06','8.34862e-06','7.71574e-08','6.73439e-10','0','0','0','0','0','2.30913e-08','1.03743e-06','6.73439e-10','6.86823e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018424, ("CSC", 1, 1, 2, 31), "MEp12_31"))
reports[-1].posNum = 1251
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00254284, 0.0154388, 0), \
                           ValErr(-0.342449, 0.412776, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.49728e-05, 0.000308314, 0), \
                           -866.656, 1251, 1251, -nan)
reports[-1].sigmaresid = ValErr(0.483759, 0.00967126, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0109162, None, -0.000876864, None, -0.00156324, None, -0.000883816, None, -0.00156324, None, -0.000883816, None, -0.0121271, None, -0.000685161, None, -0.0121271, None, -0.000685161, None, 0.483901, None, 0.0051537, None, 0.483901, None, 0.0051537, None)
reports[-1].CovMatrix = ['0.000238358','-0.00134512','-1.99401e-06','2.81917e-08','0','0','0','0','0','-0.00134512','0.170384','3.62227e-06','1.23049e-06','0','0','0','0','0','-1.99401e-06','3.62227e-06','9.50575e-08','8.26743e-10','0','0','0','0','0','2.81917e-08','1.23049e-06','8.26743e-10','9.3534e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018440, ("CSC", 1, 1, 2, 33), "MEp12_33"))
reports[-1].posNum = 1690
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00629043, 0.0129323, 0), \
                           ValErr(0.0368924, 0.309648, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000152759, 0.000273444, 0), \
                           -1176.83, 1690, 1690, -nan)
reports[-1].sigmaresid = ValErr(0.485495, 0.00835074, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00218985, None, -0.000538475, None, 0.00335988, None, -0.000503168, None, 0.00335988, None, -0.000503168, None, -0.0131022, None, -0.000359363, None, -0.0131022, None, -0.000359363, None, 0.485542, None, 0.00624973, None, 0.485542, None, 0.00624973, None)
reports[-1].CovMatrix = ['0.000167245','-7.68545e-05','-1.44084e-06','2.77604e-08','0','0','0','0','0','-7.68545e-05','0.0958817','2.41321e-06','1.06406e-06','0','0','0','0','0','-1.44084e-06','2.41321e-06','7.47717e-08','6.29394e-10','0','0','0','0','0','2.77604e-08','1.06406e-06','6.29394e-10','6.97352e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018456, ("CSC", 1, 1, 2, 35), "MEp12_35"))
reports[-1].posNum = 1354
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00628547, 0.0139356, 0), \
                           ValErr(0.174856, 0.326006, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00019746, 0.000271145, 0), \
                           -861.589, 1354, 1354, -nan)
reports[-1].sigmaresid = ValErr(0.457213, 0.00878607, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0100556, None, -0.000106651, None, 0.00185721, None, -9.44144e-05, None, 0.00185721, None, -9.44144e-05, None, -0.0222506, None, -1.4533e-05, None, -0.0222506, None, -1.4533e-05, None, 0.457349, None, 0.00568236, None, 0.457349, None, 0.00568236, None)
reports[-1].CovMatrix = ['0.0001942','-0.000100038','-1.70884e-06','2.88078e-08','0','0','0','0','0','-0.000100038','0.10628','6.03633e-08','1.06405e-06','0','0','0','0','0','-1.70884e-06','6.03633e-08','7.35198e-08','5.63308e-10','0','0','0','0','0','2.88078e-08','1.06405e-06','5.63308e-10','7.71954e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018192, ("CSC", 1, 1, 2, 2), "MEp12_02"))
reports[-1].posNum = 1538
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00993408, 0.0130878, 0), \
                           ValErr(-0.0983362, 0.315198, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.20916e-05, 0.000272679, 0), \
                           -1030.04, 1538, 1538, -nan)
reports[-1].sigmaresid = ValErr(0.472739, 0.00852367, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00716049, None, -0.00293663, None, 0.00903009, None, -0.00272953, None, 0.00903009, None, -0.00272953, None, 0.0149267, None, -0.00279757, None, 0.0149267, None, -0.00279757, None, 0.472757, None, 0.00625778, None, 0.472757, None, 0.00625778, None)
reports[-1].CovMatrix = ['0.00017129','-0.000160864','-1.38598e-06','2.78783e-08','0','0','0','0','0','-0.000160864','0.0993496','2.12889e-06','1.06396e-06','0','0','0','0','0','-1.38598e-06','2.12889e-06','7.43536e-08','6.52381e-10','0','0','0','0','0','2.78783e-08','1.06396e-06','6.52381e-10','7.26533e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018208, ("CSC", 1, 1, 2, 4), "MEp12_04"))
reports[-1].posNum = 1433
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0130349, 0.0141121, 0), \
                           ValErr(0.107458, 0.314292, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000145464, 0.000301061, 0), \
                           -877.379, 1433, 1433, -nan)
reports[-1].sigmaresid = ValErr(0.446346, 0.00833754, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00822414, None, -0.000924872, None, -0.00955649, None, -0.000844007, None, -0.00955649, None, -0.000844007, None, -0.00545489, None, -0.000785217, None, -0.00545489, None, -0.000785217, None, 0.4464, None, 0.00599024, None, 0.4464, None, 0.00599024, None)
reports[-1].CovMatrix = ['0.000199151','0.000371483','-2.32546e-06','2.67708e-08','0','0','0','0','0','0.000371483','0.0987796','-6.1769e-06','9.55895e-07','0','0','0','0','0','-2.32546e-06','-6.1769e-06','9.06378e-08','4.9991e-10','0','0','0','0','0','2.67708e-08','9.55895e-07','4.9991e-10','6.95149e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018224, ("CSC", 1, 1, 2, 6), "MEp12_06"))
reports[-1].posNum = 1563
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00772085, 0.012699, 0), \
                           ValErr(0.263634, 0.307444, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.30693e-05, 0.000273089, 0), \
                           -1016.64, 1563, 1563, -nan)
reports[-1].sigmaresid = ValErr(0.46371, 0.00829377, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0133225, None, 0.001405, None, 0.00588269, None, 0.00139779, None, 0.00588269, None, 0.00139779, None, 0.0232331, None, 0.00124693, None, 0.0232331, None, 0.00124693, None, 0.463833, None, 0.00597654, None, 0.463833, None, 0.00597654, None)
reports[-1].CovMatrix = ['0.000161266','0.000130856','-1.32426e-06','2.98106e-08','0','0','0','0','0','0.000130856','0.0945218','-7.00092e-08','1.02304e-06','0','0','0','0','0','-1.32426e-06','-7.00092e-08','7.45777e-08','5.86068e-10','0','0','0','0','0','2.98106e-08','1.02304e-06','5.86068e-10','6.87869e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018240, ("CSC", 1, 1, 2, 8), "MEp12_08"))
reports[-1].posNum = 1498
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0068126, 0.0129091, 0), \
                           ValErr(0.174995, 0.307251, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.57416e-05, 0.000261278, 0), \
                           -931.844, 1498, 1498, -nan)
reports[-1].sigmaresid = ValErr(0.450735, 0.00823478, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0144508, None, -0.00166193, None, -0.00485667, None, -0.0016233, None, -0.00485667, None, -0.0016233, None, 0.00253434, None, -0.00157096, None, 0.00253434, None, -0.00157096, None, 0.450802, None, 0.00643094, None, 0.450802, None, 0.00643094, None)
reports[-1].CovMatrix = ['0.000166644','3.95651e-05','-1.45473e-06','2.5932e-08','0','0','0','0','0','3.95651e-05','0.0944031','2.91415e-07','9.58843e-07','0','0','0','0','0','-1.45473e-06','2.91415e-07','6.82662e-08','5.32803e-10','0','0','0','0','0','2.5932e-08','9.58843e-07','5.32803e-10','6.78119e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018256, ("CSC", 1, 1, 2, 10), "MEp12_10"))
reports[-1].posNum = 1503
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00652081, 0.0131365, 0), \
                           ValErr(0.0436168, 0.311569, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.43795e-05, 0.000268471, 0), \
                           -986.702, 1503, 1503, -nan)
reports[-1].sigmaresid = ValErr(0.466522, 0.00850897, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0182281, None, -0.00119221, None, 0.00521948, None, -0.00110793, None, 0.00521948, None, -0.00110793, None, -0.0130057, None, -0.00102701, None, -0.0130057, None, -0.00102701, None, 0.466534, None, 0.0061983, None, 0.466534, None, 0.0061983, None)
reports[-1].CovMatrix = ['0.000172568','8.824e-05','-1.41263e-06','3.03413e-08','0','0','0','0','0','8.824e-05','0.0970752','-1.20656e-07','1.06972e-06','0','0','0','0','0','-1.41263e-06','-1.20656e-07','7.20765e-08','5.84033e-10','0','0','0','0','0','3.03413e-08','1.06972e-06','5.84033e-10','7.2403e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018272, ("CSC", 1, 1, 2, 12), "MEp12_12"))
reports[-1].posNum = 1448
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00018736, 0.0134681, 0), \
                           ValErr(-0.0872828, 0.316676, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.57728e-05, 0.000281584, 0), \
                           -917.548, 1448, 1448, -nan)
reports[-1].sigmaresid = ValErr(0.455996, 0.00847347, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0202379, None, -0.00131201, None, -0.00174418, None, -0.00115177, None, -0.00174418, None, -0.00115177, None, 0.0159095, None, -0.00126864, None, 0.0159095, None, -0.00126864, None, 0.456022, None, 0.0057738, None, 0.456022, None, 0.0057738, None)
reports[-1].CovMatrix = ['0.000181388','-4.12476e-05','-1.72992e-06','2.68094e-08','0','0','0','0','0','-4.12476e-05','0.100284','-1.21082e-06','1.03056e-06','0','0','0','0','0','-1.72992e-06','-1.21082e-06','7.92894e-08','5.53364e-10','0','0','0','0','0','2.68094e-08','1.03056e-06','5.53364e-10','7.18001e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018288, ("CSC", 1, 1, 2, 14), "MEp12_14"))
reports[-1].posNum = 1733
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00584924, 0.0118089, 0), \
                           ValErr(-0.0451098, 0.291777, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.86439e-05, 0.000254132, 0), \
                           -1148.6, 1733, 1733, -nan)
reports[-1].sigmaresid = ValErr(0.469467, 0.00797426, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00159035, None, -0.000624762, None, 0.00690135, None, -0.000650562, None, 0.00690135, None, -0.000650562, None, 0.0142762, None, -0.000618189, None, 0.0142762, None, -0.000618189, None, 0.469483, None, 0.00638208, None, 0.469483, None, 0.00638208, None)
reports[-1].CovMatrix = ['0.000139449','-5.19925e-05','-8.88807e-07','2.70171e-08','0','0','0','0','0','-5.19925e-05','0.0851341','-4.18704e-07','9.05646e-07','0','0','0','0','0','-8.88807e-07','-4.18704e-07','6.45832e-08','5.87995e-10','0','0','0','0','0','2.70171e-08','9.05646e-07','5.87995e-10','6.35891e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018304, ("CSC", 1, 1, 2, 16), "MEp12_16"))
reports[-1].posNum = 1567
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000206838, 0.0122264, 0), \
                           ValErr(0.0698979, 0.285227, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00010809, 0.000254419, 0), \
                           -950.191, 1567, 1567, -nan)
reports[-1].sigmaresid = ValErr(0.443718, 0.00792601, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00285623, None, -0.000527209, None, -0.00230447, None, -0.000444561, None, -0.00230447, None, -0.000444561, None, 0.0109078, None, -0.000549612, None, 0.0109078, None, -0.000549612, None, 0.443755, None, 0.00647504, None, 0.443755, None, 0.00647504, None)
reports[-1].CovMatrix = ['0.000149486','-4.57635e-05','-1.24214e-06','2.56375e-08','0','0','0','0','0','-4.57635e-05','0.0813546','3.34824e-06','8.67502e-07','0','0','0','0','0','-1.24214e-06','3.34824e-06','6.47291e-08','5.25532e-10','0','0','0','0','0','2.56375e-08','8.67502e-07','5.25532e-10','6.2822e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018320, ("CSC", 1, 1, 2, 18), "MEp12_18"))
reports[-1].posNum = 1712
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00554605, 0.0122646, 0), \
                           ValErr(0.0233682, 0.297396, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.71278e-05, 0.000259984, 0), \
                           -1132.81, 1712, 1712, -nan)
reports[-1].sigmaresid = ValErr(0.468953, 0.00801422, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00308092, None, 0.000422617, None, -0.00491882, None, 0.000535019, None, -0.00491882, None, 0.000535019, None, -0.0123671, None, 0.000592915, None, -0.0123671, None, 0.000592915, None, 0.468958, None, 0.00637266, None, 0.468958, None, 0.00637266, None)
reports[-1].CovMatrix = ['0.000150421','0.000179152','-1.21245e-06','2.82577e-08','0','0','0','0','0','0.000179152','0.0884444','-2.28424e-06','9.66276e-07','0','0','0','0','0','-1.21245e-06','-2.28424e-06','6.75917e-08','5.25578e-10','0','0','0','0','0','2.82577e-08','9.66276e-07','5.25578e-10','6.4228e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018336, ("CSC", 1, 1, 2, 20), "MEp12_20"))
reports[-1].posNum = 1316
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00939224, 0.0141454, 0), \
                           ValErr(0.191993, 0.336314, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000110954, 0.000280608, 0), \
                           -877.768, 1316, 1316, -nan)
reports[-1].sigmaresid = ValErr(0.471447, 0.00918935, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0265771, None, 0.000628649, None, 0.00661847, None, 0.000712081, None, 0.00661847, None, 0.000712081, None, -0.0213988, None, 0.000918765, None, -0.0213988, None, 0.000918765, None, 0.471542, None, 0.00642353, None, 0.471542, None, 0.00642353, None)
reports[-1].CovMatrix = ['0.000200092','0.000229587','-1.54189e-06','3.9075e-08','0','0','0','0','0','0.000229587','0.113107','5.47506e-06','1.37865e-06','0','0','0','0','0','-1.54189e-06','5.47506e-06','7.87411e-08','7.19521e-10','0','0','0','0','0','3.9075e-08','1.37865e-06','7.19521e-10','8.44446e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018352, ("CSC", 1, 1, 2, 22), "MEp12_22"))
reports[-1].posNum = 1609
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000470818, 0.0123724, 0), \
                           ValErr(-0.18055, 0.301522, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.89977e-05, 0.000255519, 0), \
                           -1034.95, 1609, 1609, -nan)
reports[-1].sigmaresid = ValErr(0.460376, 0.00811559, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00848545, None, -0.000398781, None, -0.00133758, None, -0.00039514, None, -0.00133758, None, -0.00039514, None, -0.0134371, None, -0.000410026, None, -0.0134371, None, -0.000410026, None, 0.460433, None, 0.00566187, None, 0.460433, None, 0.00566187, None)
reports[-1].CovMatrix = ['0.000153076','4.09496e-05','-1.18062e-06','2.69563e-08','0','0','0','0','0','4.09496e-05','0.0909158','-1.73204e-06','9.61746e-07','0','0','0','0','0','-1.18062e-06','-1.73204e-06','6.52898e-08','5.32016e-10','0','0','0','0','0','2.69563e-08','9.61746e-07','5.32016e-10','6.58631e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018368, ("CSC", 1, 1, 2, 24), "MEp12_24"))
reports[-1].posNum = 1793
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00311177, 0.0121909, 0), \
                           ValErr(-0.162858, 0.299029, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.53591e-07, 0.000259006, 0), \
                           -1251.21, 1793, 1793, -nan)
reports[-1].sigmaresid = ValErr(0.486214, 0.00811935, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0185016, None, -0.000190516, None, 0.00307724, None, -0.000305865, None, 0.00307724, None, -0.000305865, None, 0.00757697, None, -0.000210613, None, 0.00757697, None, -0.000210613, None, 0.486253, None, 0.00565134, None, 0.486253, None, 0.00565134, None)
reports[-1].CovMatrix = ['0.000148618','-3.56582e-06','-1.06059e-06','2.86576e-08','0','0','0','0','0','-3.56582e-06','0.0894181','-5.86899e-07','9.82498e-07','0','0','0','0','0','-1.06059e-06','-5.86899e-07','6.7084e-08','5.96877e-10','0','0','0','0','0','2.86576e-08','9.82498e-07','5.96877e-10','6.59242e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018384, ("CSC", 1, 1, 2, 26), "MEp12_26"))
reports[-1].posNum = 1378
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00399514, 0.0138352, 0), \
                           ValErr(-0.28911, 0.308328, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00018842, 0.00027351, 0), \
                           -808.179, 1378, 1378, -nan)
reports[-1].sigmaresid = ValErr(0.434982, 0.00828573, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00836652, None, -4.52393e-05, None, 0.000134659, None, 8.31178e-05, None, 0.000134659, None, 8.31178e-05, None, -0.0240043, None, 1.99373e-05, None, -0.0240043, None, 1.99373e-05, None, 0.435203, None, 0.00609384, None, 0.435203, None, 0.00609384, None)
reports[-1].CovMatrix = ['0.000191412','-0.00037064','-1.99566e-06','2.00605e-08','0','0','0','0','0','-0.00037064','0.0950663','3.14591e-06','8.9821e-07','0','0','0','0','0','-1.99566e-06','3.14591e-06','7.48076e-08','5.05217e-10','0','0','0','0','0','2.00605e-08','8.9821e-07','5.05217e-10','6.86538e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018400, ("CSC", 1, 1, 2, 28), "MEp12_28"))
reports[-1].posNum = 1721
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00507956, 0.0120307, 0), \
                           ValErr(0.115604, 0.297082, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000120891, 0.000249951, 0), \
                           -1130.9, 1721, 1721, -nan)
reports[-1].sigmaresid = ValErr(0.466818, 0.0079569, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00301089, None, 0.00162181, None, 0.00310019, None, 0.00151157, None, 0.00310019, None, 0.00151157, None, -0.00268026, None, 0.00162939, None, -0.00268026, None, 0.00162939, None, 0.466867, None, 0.00569461, None, 0.466867, None, 0.00569461, None)
reports[-1].CovMatrix = ['0.000144737','-4.82124e-05','-1.06257e-06','2.55393e-08','0','0','0','0','0','-4.82124e-05','0.0882579','-7.24617e-07','9.20041e-07','0','0','0','0','0','-1.06257e-06','-7.24617e-07','6.24757e-08','5.70074e-10','0','0','0','0','0','2.55393e-08','9.20041e-07','5.70074e-10','6.33125e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018416, ("CSC", 1, 1, 2, 30), "MEp12_30"))
reports[-1].posNum = 1181
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000484041, 0.0146677, 0), \
                           ValErr(0.08402, 0.310576, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.84147e-05, 0.000278634, 0), \
                           -610.737, 1181, 1181, -nan)
reports[-1].sigmaresid = ValErr(0.405837, 0.00835047, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00305397, None, -0.000624789, None, 0.00147806, None, -0.000507382, None, 0.00147806, None, -0.000507382, None, -0.00263757, None, -0.000481552, None, -0.00263757, None, -0.000481552, None, 0.405854, None, 0.00602965, None, 0.405854, None, 0.00602965, None)
reports[-1].CovMatrix = ['0.000215141','0.000379409','-2.41561e-06','2.55013e-08','0','0','0','0','0','0.000379409','0.0964574','-5.00668e-06','9.42238e-07','0','0','0','0','0','-2.41561e-06','-5.00668e-06','7.76371e-08','3.6549e-10','0','0','0','0','0','2.55013e-08','9.42238e-07','3.6549e-10','6.97308e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018432, ("CSC", 1, 1, 2, 32), "MEp12_32"))
reports[-1].posNum = 1540
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00393913, 0.013521, 0), \
                           ValErr(0.0392673, 0.320231, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.32115e-05, 0.00027527, 0), \
                           -1047.16, 1540, 1540, -nan)
reports[-1].sigmaresid = ValErr(0.477605, 0.00860579, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0159137, None, 0.000164028, None, 0.0035578, None, -0.00013677, None, 0.0035578, None, -0.00013677, None, -0.00591561, None, 7.21233e-05, None, -0.00591561, None, 7.21233e-05, None, 0.47761, None, 0.00567628, None, 0.47761, None, 0.00567628, None)
reports[-1].CovMatrix = ['0.000182816','0.000379115','-1.60472e-06','3.41829e-08','0','0','0','0','0','0.000379115','0.102548','-5.17779e-06','1.14914e-06','0','0','0','0','0','-1.60472e-06','-5.17779e-06','7.57738e-08','5.30214e-10','0','0','0','0','0','3.41829e-08','1.14914e-06','5.30214e-10','7.406e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018448, ("CSC", 1, 1, 2, 34), "MEp12_34"))
reports[-1].posNum = 1502
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0125301, 0.0126978, 0), \
                           ValErr(-0.306539, 0.308757, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000104025, 0.000251451, 0), \
                           -974.522, 1502, 1502, -nan)
reports[-1].sigmaresid = ValErr(0.462959, 0.00844683, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0149328, None, 0.000571445, None, -0.0110072, None, 0.000739332, None, -0.0110072, None, 0.000739332, None, -0.0166185, None, 0.000553928, None, -0.0166185, None, 0.000553928, None, 0.463139, None, 0.00603205, None, 0.463139, None, 0.00603205, None)
reports[-1].CovMatrix = ['0.000161234','-0.000119789','-1.08075e-06','2.82625e-08','0','0','0','0','0','-0.000119789','0.0953309','2.43839e-06','1.0398e-06','0','0','0','0','0','-1.08075e-06','2.43839e-06','6.32276e-08','6.28825e-10','0','0','0','0','0','2.82625e-08','1.0398e-06','6.28825e-10','7.13494e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018464, ("CSC", 1, 1, 2, 36), "MEp12_36"))
reports[-1].posNum = 1225
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00354106, 0.0145352, 0), \
                           ValErr(0.180646, 0.354992, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.01713e-05, 0.00027145, 0), \
                           -824.718, 1225, 1225, -nan)
reports[-1].sigmaresid = ValErr(0.474403, 0.00958436, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0123598, None, -0.000427442, None, -0.00340973, None, -0.000247339, None, -0.00340973, None, -0.000247339, None, -0.0197586, None, -0.000342295, None, -0.0197586, None, -0.000342295, None, 0.474456, None, 0.00544959, None, 0.474456, None, 0.00544959, None)
reports[-1].CovMatrix = ['0.000211272','0.000364982','-1.40529e-06','4.25157e-08','0','0','0','0','0','0.000364982','0.12602','-3.02111e-06','1.41524e-06','0','0','0','0','0','-1.40529e-06','-3.02111e-06','7.36852e-08','6.84981e-10','0','0','0','0','0','4.25157e-08','1.41524e-06','6.84981e-10','9.18606e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018696, ("CSC", 1, 1, 3, 1), "MEp13_01"))
reports[-1].posNum = 536
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0108972, 0.055474, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000465158, 0.00133506, 0), \
                           -894.374, 536, 536, -nan)
reports[-1].sigmaresid = ValErr(1.28362, 0.0392048, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0171519, None, -0.00278613, None, -0.0115353, None, -0.0026755, None, -0.0115353, None, -0.0026755, None, -0.0308408, None, -0.00230188, None, -0.0308408, None, -0.00230188, None, 1.28375, None, 0.00914341, None, 1.28375, None, 0.00914341, None)
reports[-1].CovMatrix = ['0.00307736','2.43061e-06','1.42635e-06','0','0','0','0','0','0','2.43061e-06','1.78238e-06','3.44322e-08','0','0','0','0','0','0','1.42635e-06','3.44322e-08','0.00153709','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018704, ("CSC", 1, 1, 3, 2), "MEp13_02"))
reports[-1].posNum = 482
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018712, ("CSC", 1, 1, 3, 3), "MEp13_03"))
reports[-1].posNum = 539
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0162742, 0.0630336, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000153247, 0.00162195, 0), \
                           -955.245, 539, 539, -nan)
reports[-1].sigmaresid = ValErr(1.42378, 0.0433634, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0313497, None, -9.56148e-05, None, 0.0148979, None, 0.000375483, None, 0.0148979, None, 0.000375483, None, -0.113426, None, 0.000919811, None, -0.113426, None, 0.000919811, None, 1.42379, None, 0.0105893, None, 1.42379, None, 0.0105893, None)
reports[-1].CovMatrix = ['0.00397324','2.36316e-05','2.24912e-06','0','0','0','0','0','0','2.36316e-05','2.63072e-06','5.81904e-08','0','0','0','0','0','0','2.24912e-06','5.81904e-08','0.00188048','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018720, ("CSC", 1, 1, 3, 4), "MEp13_04"))
reports[-1].posNum = 494
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018728, ("CSC", 1, 1, 3, 5), "MEp13_05"))
reports[-1].posNum = 496
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018736, ("CSC", 1, 1, 3, 6), "MEp13_06"))
reports[-1].posNum = 434
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018744, ("CSC", 1, 1, 3, 7), "MEp13_07"))
reports[-1].posNum = 650
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0111485, 0.0480939, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.37674e-05, 0.00122288, 0), \
                           -1054.62, 650, 650, -nan)
reports[-1].sigmaresid = ValErr(1.22576, 0.0339959, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0310983, None, 0.00145901, None, 0.0111916, None, 0.00180438, None, 0.0111916, None, 0.00180438, None, -0.0626292, None, 0.00186327, None, -0.0626292, None, 0.00186327, None, 1.22576, None, 0.0105824, None, 1.22576, None, 0.0105824, None)
reports[-1].CovMatrix = ['0.00231302','1.49849e-06','1.02584e-06','0','0','0','0','0','0','1.49849e-06','1.49543e-06','2.69286e-08','0','0','0','0','0','0','1.02584e-06','2.69286e-08','0.00115576','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018752, ("CSC", 1, 1, 3, 8), "MEp13_08"))
reports[-1].posNum = 717
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.02932, 0.0478276, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.52146e-06, 0.00117142, 0), \
                           -1192.68, 717, 717, -nan)
reports[-1].sigmaresid = ValErr(1.27709, 0.0337285, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0100723, None, 0.00071656, None, 0.0291856, None, 0.00112406, None, 0.0291856, None, 0.00112406, None, 0.0580806, None, 0.00119548, None, 0.0580806, None, 0.00119548, None, 1.27697, None, 0.0100904, None, 1.27697, None, 0.0100904, None)
reports[-1].CovMatrix = ['0.00228748','-4.18497e-06','1.14965e-06','0','0','0','0','0','0','-4.18497e-06','1.37223e-06','2.37543e-08','0','0','0','0','0','0','1.14965e-06','2.37543e-08','0.00113765','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018760, ("CSC", 1, 1, 3, 9), "MEp13_09"))
reports[-1].posNum = 685
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00505891, 0.0529545, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.31505e-06, 0.00127652, 0), \
                           -1185.19, 685, 685, -nan)
reports[-1].sigmaresid = ValErr(1.3652, 0.0368849, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0167666, None, 0.00397633, None, -0.00472626, None, 0.00483103, None, -0.00472626, None, 0.00483103, None, -0.024712, None, 0.00511567, None, -0.024712, None, 0.00511567, None, 1.36514, None, 0.0106851, None, 1.36514, None, 0.0106851, None)
reports[-1].CovMatrix = ['0.00280418','-1.1655e-05','4.86468e-07','0','0','0','0','0','0','-1.1655e-05','1.62951e-06','3.05796e-08','0','0','0','0','0','0','4.86468e-07','3.05796e-08','0.00136055','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018768, ("CSC", 1, 1, 3, 10), "MEp13_10"))
reports[-1].posNum = 525
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.043496, 0.054068, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.35227e-05, 0.00125704, 0), \
                           -853.894, 525, 525, -nan)
reports[-1].sigmaresid = ValErr(1.23063, 0.0379773, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0140301, None, 0.0025348, None, -0.0431817, None, 0.00288735, None, -0.0431817, None, 0.00288735, None, -0.0479038, None, 0.00263428, None, -0.0479038, None, 0.00263428, None, 1.23063, None, 0.0070481, None, 1.23063, None, 0.0070481, None)
reports[-1].CovMatrix = ['0.00292335','-7.81826e-06','1.13869e-06','0','0','0','0','0','0','-7.81826e-06','1.58014e-06','2.64786e-08','0','0','0','0','0','0','1.13869e-06','2.64786e-08','0.00144234','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018776, ("CSC", 1, 1, 3, 11), "MEp13_11"))
reports[-1].posNum = 304
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018784, ("CSC", 1, 1, 3, 12), "MEp13_12"))
reports[-1].posNum = 279
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018792, ("CSC", 1, 1, 3, 13), "MEp13_13"))
reports[-1].posNum = 588
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0523582, 0.0524047, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00135732, 0.00125828, 0), \
                           -972.746, 588, 588, -nan)
reports[-1].sigmaresid = ValErr(1.26544, 0.0369014, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0315923, None, -0.0016805, None, 0.0472835, None, -0.00137106, None, 0.0472835, None, -0.00137106, None, 0.135691, None, -0.00150359, None, 0.135691, None, -0.00150359, None, 1.26666, None, 0.00910311, None, 1.26666, None, 0.00910311, None)
reports[-1].CovMatrix = ['0.00274625','-6.02126e-06','9.13474e-07','0','0','0','0','0','0','-6.02126e-06','1.58327e-06','2.89043e-08','0','0','0','0','0','0','9.13474e-07','2.89043e-08','0.00136177','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018800, ("CSC", 1, 1, 3, 14), "MEp13_14"))
reports[-1].posNum = 568
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.041964, 0.0567896, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000547211, 0.00133496, 0), \
                           -958.228, 568, 568, -nan)
reports[-1].sigmaresid = ValErr(1.30745, 0.0387907, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0561767, None, 0.000282201, None, -0.0359436, None, 0.000389403, None, -0.0359436, None, 0.000389403, None, -0.0836752, None, 0.000250632, None, -0.0836752, None, 0.000250632, None, 1.30765, None, 0.00826499, None, 1.30765, None, 0.00826499, None)
reports[-1].CovMatrix = ['0.00322506','-1.95964e-05','1.06604e-06','0','0','0','0','0','0','-1.95964e-05','1.78211e-06','2.50561e-08','0','0','0','0','0','0','1.06604e-06','2.50561e-08','0.00150478','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018808, ("CSC", 1, 1, 3, 15), "MEp13_15"))
reports[-1].posNum = 550
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0132782, 0.0522672, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000352087, 0.00121042, 0), \
                           -891.035, 550, 550, -nan)
reports[-1].sigmaresid = ValErr(1.22279, 0.0368679, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.036797, None, -9.28592e-05, None, 0.0143647, None, 6.3351e-05, None, 0.0143647, None, 6.3351e-05, None, 0.0391726, None, -0.000160573, None, 0.0391726, None, -0.000160573, None, 1.22287, None, 0.0101123, None, 1.22287, None, 0.0101123, None)
reports[-1].CovMatrix = ['0.00273186','-4.4149e-06','1.05582e-06','0','0','0','0','0','0','-4.4149e-06','1.46513e-06','2.69627e-08','0','0','0','0','0','0','1.05582e-06','2.69627e-08','0.0013593','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018816, ("CSC", 1, 1, 3, 16), "MEp13_16"))
reports[-1].posNum = 517
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00351473, 0.0563385, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000739795, 0.00135318, 0), \
                           -860.459, 517, 517, -nan)
reports[-1].sigmaresid = ValErr(1.27823, 0.0397546, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(7.72439e-05, None, -0.000503306, None, 0.00140018, None, -0.000816677, None, 0.00140018, None, -0.000816677, None, 0.117137, None, -0.000607929, None, 0.117137, None, -0.000607929, None, 1.27849, None, 0.0118338, None, 1.27849, None, 0.0118338, None)
reports[-1].CovMatrix = ['0.00317402','-5.01188e-06','1.5532e-06','0','0','0','0','0','0','-5.01188e-06','1.83109e-06','2.78748e-08','0','0','0','0','0','0','1.5532e-06','2.78748e-08','0.0015805','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018824, ("CSC", 1, 1, 3, 17), "MEp13_17"))
reports[-1].posNum = 622
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0296621, 0.0564771, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000334771, 0.00139086, 0), \
                           -1095.64, 622, 622, -nan)
reports[-1].sigmaresid = ValErr(1.40852, 0.039934, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000628909, None, 0.00167033, None, -0.0296044, None, 0.00177164, None, -0.0296044, None, 0.00177164, None, 0.043375, None, 0.00169194, None, 0.043375, None, 0.00169194, None, 1.40859, None, 0.00876632, None, 1.40859, None, 0.00876632, None)
reports[-1].CovMatrix = ['0.00318966','-3.52395e-07','1.46185e-06','0','0','0','0','0','0','-3.52395e-07','1.93448e-06','3.60244e-08','0','0','0','0','0','0','1.46185e-06','3.60244e-08','0.00159479','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018832, ("CSC", 1, 1, 3, 18), "MEp13_18"))
reports[-1].posNum = 491
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018840, ("CSC", 1, 1, 3, 19), "MEp13_19"))
reports[-1].posNum = 603
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00129357, 0.0534424, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00084197, 0.00125598, 0), \
                           -1012.41, 603, 603, -nan)
reports[-1].sigmaresid = ValErr(1.29695, 0.0373457, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0724608, None, 0.00128114, None, -0.00417845, None, 0.00152208, None, -0.00417845, None, 0.00152208, None, -0.0226549, None, 0.00174584, None, -0.0226549, None, 0.00174584, None, 1.29743, None, 0.00933956, None, 1.29743, None, 0.00933956, None)
reports[-1].CovMatrix = ['0.00285609','-1.02477e-05','1.08711e-06','0','0','0','0','0','0','-1.02477e-05','1.57748e-06','2.5421e-08','0','0','0','0','0','0','1.08711e-06','2.5421e-08','0.00139476','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018848, ("CSC", 1, 1, 3, 20), "MEp13_20"))
reports[-1].posNum = 739
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000865796, 0.0445944, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000628896, 0.00106634, 0), \
                           -1181.43, 739, 739, -nan)
reports[-1].sigmaresid = ValErr(1.19692, 0.0311329, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0656402, None, 0.000542145, None, 0.00504031, None, 0.0004699, None, 0.00504031, None, 0.0004699, None, 0.0810945, None, 0.000205755, None, 0.0810945, None, 0.000205755, None, 1.1972, None, 0.0080704, None, 1.1972, None, 0.0080704, None)
reports[-1].CovMatrix = ['0.00198866','-7.54674e-06','7.28906e-07','0','0','0','0','0','0','-7.54674e-06','1.13709e-06','1.74653e-08','0','0','0','0','0','0','7.28906e-07','1.74653e-08','0.000969287','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018856, ("CSC", 1, 1, 3, 21), "MEp13_21"))
reports[-1].posNum = 664
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00685827, 0.0499255, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00110181, 0.00126135, 0), \
                           -1105.33, 664, 664, -nan)
reports[-1].sigmaresid = ValErr(1.27854, 0.0350838, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.04867, None, 0.000356703, None, 0.0117024, None, -7.00382e-05, None, 0.0117024, None, -7.00382e-05, None, 0.129556, None, 0.00024323, None, 0.129556, None, 0.00024323, None, 1.27927, None, 0.0128767, None, 1.27927, None, 0.0128767, None)
reports[-1].CovMatrix = ['0.00249256','-6.99172e-06','9.82316e-07','0','0','0','0','0','0','-6.99172e-06','1.591e-06','2.49322e-08','0','0','0','0','0','0','9.82316e-07','2.49322e-08','0.00123092','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018864, ("CSC", 1, 1, 3, 22), "MEp13_22"))
reports[-1].posNum = 641
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0328318, 0.0477319, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000104812, 0.00118148, 0), \
                           -1030.19, 641, 641, -nan)
reports[-1].sigmaresid = ValErr(1.20713, 0.0337148, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.023441, None, 0.0026924, None, -0.0330152, None, 0.00281745, None, -0.0330152, None, 0.00281745, None, 0.0733599, None, 0.00257778, None, 0.0733599, None, 0.00257778, None, 1.20711, None, 0.00964693, None, 1.20711, None, 0.00964693, None)
reports[-1].CovMatrix = ['0.00227834','2.65664e-06','1.01432e-06','0','0','0','0','0','0','2.65664e-06','1.3959e-06','2.62087e-08','0','0','0','0','0','0','1.01432e-06','2.62087e-08','0.00113673','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018872, ("CSC", 1, 1, 3, 23), "MEp13_23"))
reports[-1].posNum = 578
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00211188, 0.0512989, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000357826, 0.00117645, 0), \
                           -935.498, 578, 578, -nan)
reports[-1].sigmaresid = ValErr(1.22085, 0.0359055, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0138522, None, 0.000283636, None, -0.00434399, None, 0.00032193, None, -0.00434399, None, 0.00032193, None, -0.0639241, None, 0.000767425, None, -0.0639241, None, 0.000767425, None, 1.22098, None, 0.00849895, None, 1.22098, None, 0.00849895, None)
reports[-1].CovMatrix = ['0.00263158','-8.55722e-06','1.04369e-06','0','0','0','0','0','0','-8.55722e-06','1.38402e-06','2.10462e-08','0','0','0','0','0','0','1.04369e-06','2.10462e-08','0.00128926','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018880, ("CSC", 1, 1, 3, 24), "MEp13_24"))
reports[-1].posNum = 489
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018888, ("CSC", 1, 1, 3, 25), "MEp13_25"))
reports[-1].posNum = 459
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018896, ("CSC", 1, 1, 3, 26), "MEp13_26"))
reports[-1].posNum = 458
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018904, ("CSC", 1, 1, 3, 27), "MEp13_27"))
reports[-1].posNum = 347
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018912, ("CSC", 1, 1, 3, 28), "MEp13_28"))
reports[-1].posNum = 703
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0104694, 0.0483145, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000183797, 0.00113552, 0), \
                           -1159.49, 703, 703, -nan)
reports[-1].sigmaresid = ValErr(1.25909, 0.0335774, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0158678, None, -0.00197353, None, 0.00896284, None, -0.00154018, None, 0.00896284, None, -0.00154018, None, 0.0288153, None, -0.00149245, None, 0.0288153, None, -0.00149245, None, 1.25914, None, 0.00823677, None, 1.25914, None, 0.00823677, None)
reports[-1].CovMatrix = ['0.00233429','-1.01072e-05','9.80115e-07','0','0','0','0','0','0','-1.01072e-05','1.2894e-06','1.74744e-08','0','0','0','0','0','0','9.80115e-07','1.74744e-08','0.00112748','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018920, ("CSC", 1, 1, 3, 29), "MEp13_29"))
reports[-1].posNum = 679
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0122428, 0.0480521, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000491906, 0.00112666, 0), \
                           -1110.6, 679, 679, -nan)
reports[-1].sigmaresid = ValErr(1.24199, 0.0337029, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0297647, None, 0.000753577, None, -0.00951828, None, 0.000362314, None, -0.00951828, None, 0.000362314, None, 0.03509, None, 0.000541408, None, 0.03509, None, 0.000541408, None, 1.24215, None, 0.00931422, None, 1.24215, None, 0.00931422, None)
reports[-1].CovMatrix = ['0.00230901','-6.87365e-06','7.53002e-07','0','0','0','0','0','0','-6.87365e-06','1.26936e-06','2.55846e-08','0','0','0','0','0','0','7.53002e-07','2.55846e-08','0.00113593','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018928, ("CSC", 1, 1, 3, 30), "MEp13_30"))
reports[-1].posNum = 471
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018936, ("CSC", 1, 1, 3, 31), "MEp13_31"))
reports[-1].posNum = 682
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0144482, 0.0488602, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000315906, 0.00117931, 0), \
                           -1132.74, 682, 682, -nan)
reports[-1].sigmaresid = ValErr(1.27377, 0.0344889, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0685885, None, -0.00063009, None, 0.0136834, None, -0.000812179, None, 0.0136834, None, -0.000812179, None, 0.00548038, None, -0.000535459, None, 0.00548038, None, -0.000535459, None, 1.27382, None, 0.0110366, None, 1.27382, None, 0.0110366, None)
reports[-1].CovMatrix = ['0.00238732','-3.39988e-06','9.84391e-07','0','0','0','0','0','0','-3.39988e-06','1.39077e-06','2.47671e-08','0','0','0','0','0','0','9.84391e-07','2.47671e-08','0.00118953','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018944, ("CSC", 1, 1, 3, 32), "MEp13_32"))
reports[-1].posNum = 644
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000461239, 0.044847, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000387713, 0.00106972, 0), \
                           -996.184, 644, 644, -nan)
reports[-1].sigmaresid = ValErr(1.13653, 0.0316698, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0197314, None, 0.0018002, None, 0.00130598, None, 0.00137285, None, 0.00130598, None, 0.00137285, None, -0.0818065, None, 0.00154681, None, -0.0818065, None, 0.00154681, None, 1.13659, None, 0.00756357, None, 1.13659, None, 0.00756357, None)
reports[-1].CovMatrix = ['0.00201126','-2.50908e-06','8.28886e-07','0','0','0','0','0','0','-2.50908e-06','1.1443e-06','1.90132e-08','0','0','0','0','0','0','8.28886e-07','1.90132e-08','0.00100301','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018952, ("CSC", 1, 1, 3, 33), "MEp13_33"))
reports[-1].posNum = 500
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.380163, 0.054965, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.42114e-05, 0.00132822, 0), \
                           -808.457, 500, 500, -nan)
reports[-1].sigmaresid = ValErr(1.2189, 0.0385427, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.414022, None, 0.00302487, None, 0.380557, None, 0.00309149, None, 0.380557, None, 0.00309149, None, 0.340695, None, 0.00355053, None, 0.340695, None, 0.00355053, None, 1.21894, None, 0.00810101, None, 1.21894, None, 0.00810101, None)
reports[-1].CovMatrix = ['0.00302115','-9.36541e-06','1.2756e-06','0','0','0','0','0','0','-9.36541e-06','1.76418e-06','2.97493e-08','0','0','0','0','0','0','1.2756e-06','2.97493e-08','0.00148561','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018960, ("CSC", 1, 1, 3, 34), "MEp13_34"))
reports[-1].posNum = 740
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0275478, 0.0462784, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000906503, 0.0011598, 0), \
                           -1217.53, 740, 740, -nan)
reports[-1].sigmaresid = ValErr(1.25406, 0.0325981, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0376008, None, 0.00142108, None, -0.0244576, None, 0.00194768, None, -0.0244576, None, 0.00194768, None, -0.0184665, None, 0.0016036, None, -0.0184665, None, 0.0016036, None, 1.25456, None, 0.0109783, None, 1.25456, None, 0.0109783, None)
reports[-1].CovMatrix = ['0.00214169','-4.7044e-06','9.99514e-07','0','0','0','0','0','0','-4.7044e-06','1.34514e-06','2.25569e-08','0','0','0','0','0','0','9.99514e-07','2.25569e-08','0.00106267','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018968, ("CSC", 1, 1, 3, 35), "MEp13_35"))
reports[-1].posNum = 704
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00235743, 0.0483002, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000493022, 0.00118245, 0), \
                           -1170.99, 704, 704, -nan)
reports[-1].sigmaresid = ValErr(1.27694, 0.0340334, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0440918, None, 0.00244347, None, 0.000700226, None, 0.002454, None, 0.000700226, None, 0.002454, None, -0.028732, None, 0.00377235, None, -0.028732, None, 0.00377235, None, 1.277, None, 0.0101454, None, 1.277, None, 0.0101454, None)
reports[-1].CovMatrix = ['0.00233291','-4.83693e-06','8.85379e-07','0','0','0','0','0','0','-4.83693e-06','1.39819e-06','1.68692e-08','0','0','0','0','0','0','8.85379e-07','1.68692e-08','0.00115831','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018976, ("CSC", 1, 1, 3, 36), "MEp13_36"))
reports[-1].posNum = 446
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017160, ("CSC", 1, 1, 4, 1), "MEp14_01"))
reports[-1].posNum = 2933
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00329336, 0.00332903, 0), \
                           ValErr(0.0202137, 0.0822531, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00011189, 8.96079e-05, 0), \
                           914.465, 2933, 2933, -nan)
reports[-1].sigmaresid = ValErr(0.177158, 0.00231309, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00342189, None, -0.00102619, None, -0.00252412, None, -0.000774255, None, -0.00252412, None, -0.000774255, None, -0.00192765, None, -0.000899224, None, -0.00192765, None, -0.000899224, None, 0.177205, None, 0.00624408, None, 0.177205, None, 0.00624408, None)
reports[-1].CovMatrix = ['1.10825e-05','1.70505e-06','-5.53622e-08','1.64352e-09','0','0','0','0','0','1.70505e-06','0.00676557','-9.41895e-08','5.08009e-08','0','0','0','0','0','-5.53622e-08','-9.41895e-08','8.02957e-09','5.2136e-11','0','0','0','0','0','1.64352e-09','5.08009e-08','5.2136e-11','5.35041e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017176, ("CSC", 1, 1, 4, 3), "MEp14_03"))
reports[-1].posNum = 2806
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00123021, 0.00326119, 0), \
                           ValErr(0.0615021, 0.0826161, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.59036e-05, 8.72611e-05, 0), \
                           1011.51, 2806, 2806, -nan)
reports[-1].sigmaresid = ValErr(0.168736, 0.00225242, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000285455, None, -0.000824351, None, 0.000879443, None, -0.000678893, None, 0.000879443, None, -0.000678893, None, 0.00353368, None, -0.000639242, None, 0.00353368, None, -0.000639242, None, 0.168757, None, 0.00575259, None, 0.168757, None, 0.00575259, None)
reports[-1].CovMatrix = ['1.06354e-05','9.29491e-06','-6.04827e-08','1.78604e-09','0','0','0','0','0','9.29491e-06','0.00682542','-2.3138e-07','5.44558e-08','0','0','0','0','0','-6.04827e-08','-2.3138e-07','7.6145e-09','4.3902e-11','0','0','0','0','0','1.78604e-09','5.44558e-08','4.3902e-11','5.07338e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017192, ("CSC", 1, 1, 4, 5), "MEp14_05"))
reports[-1].posNum = 2898
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000979368, 0.00340091, 0), \
                           ValErr(-0.00181403, 0.0855806, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.12823e-05, 9.11834e-05, 0), \
                           848.084, 2898, 2898, -nan)
reports[-1].sigmaresid = ValErr(0.18058, 0.00237195, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00153845, None, -0.000676724, None, -0.00110896, None, -0.000511648, None, -0.00110896, None, -0.000511648, None, -0.00653252, None, -0.000404684, None, -0.00653252, None, -0.000404684, None, 0.180581, None, 0.00600404, None, 0.180581, None, 0.00600404, None)
reports[-1].CovMatrix = ['1.15662e-05','5.80073e-06','-5.09226e-08','1.89709e-09','0','0','0','0','0','5.80073e-06','0.00732404','-3.16855e-07','5.29443e-08','0','0','0','0','0','-5.09226e-08','-3.16855e-07','8.31441e-09','4.45022e-11','0','0','0','0','0','1.89709e-09','5.29443e-08','4.45022e-11','5.62614e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017208, ("CSC", 1, 1, 4, 7), "MEp14_07"))
reports[-1].posNum = 2745
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000529412, 0.00334592, 0), \
                           ValErr(0.0098207, 0.0853731, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.05872e-05, 8.96335e-05, 0), \
                           932.293, 2745, 2745, -nan)
reports[-1].sigmaresid = ValErr(0.172291, 0.00232528, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00213649, None, -0.000947148, None, -0.000450659, None, -0.000887757, None, -0.000450659, None, -0.000887757, None, -0.0101865, None, -0.000737241, None, -0.0101865, None, -0.000737241, None, 0.172292, None, 0.00539869, None, 0.172292, None, 0.00539869, None)
reports[-1].CovMatrix = ['1.11952e-05','-5.67751e-06','-5.50665e-08','1.84617e-09','0','0','0','0','0','-5.67751e-06','0.00728857','5.4076e-08','5.45954e-08','0','0','0','0','0','-5.50665e-08','5.4076e-08','8.03416e-09','5.06684e-11','0','0','0','0','0','1.84617e-09','5.45954e-08','5.06684e-11','5.40694e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017224, ("CSC", 1, 1, 4, 9), "MEp14_09"))
reports[-1].posNum = 2674
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000767395, 0.00345997, 0), \
                           ValErr(0.0714275, 0.087706, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.82652e-06, 9.19035e-05, 0), \
                           885.195, 2674, 2674, -nan)
reports[-1].sigmaresid = ValErr(0.173779, 0.00237633, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00367615, None, -0.000336618, None, -0.000774244, None, -0.000263935, None, -0.000774244, None, -0.000263935, None, -0.000686088, None, -0.000200873, None, -0.000686088, None, -0.000200873, None, 0.1738, None, 0.00544072, None, 0.1738, None, 0.00544072, None)
reports[-1].CovMatrix = ['1.19714e-05','-9.89795e-06','-7.50572e-08','2.01537e-09','0','0','0','0','0','-9.89795e-06','0.00769234','9.05246e-08','5.10345e-08','0','0','0','0','0','-7.50572e-08','9.05246e-08','8.44625e-09','4.88976e-11','0','0','0','0','0','2.01537e-09','5.10345e-08','4.88976e-11','5.64694e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017240, ("CSC", 1, 1, 4, 11), "MEp14_11"))
reports[-1].posNum = 2902
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000522007, 0.0032681, 0), \
                           ValErr(0.0171113, 0.0837295, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.24807e-05, 8.78312e-05, 0), \
                           974.457, 2902, 2902, -nan)
reports[-1].sigmaresid = ValErr(0.172954, 0.00227022, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000254816, None, 0.000183631, None, 0.000682787, None, 0.000186011, None, 0.000682787, None, 0.000186011, None, 0.00469453, None, 0.000321179, None, 0.00469453, None, 0.000321179, None, 0.172958, None, 0.00599424, None, 0.172958, None, 0.00599424, None)
reports[-1].CovMatrix = ['1.06805e-05','-1.21738e-06','-5.35619e-08','1.83337e-09','0','0','0','0','0','-1.21738e-06','0.00701063','-1.62107e-07','5.34416e-08','0','0','0','0','0','-5.35619e-08','-1.62107e-07','7.71431e-09','4.05049e-11','0','0','0','0','0','1.83337e-09','5.34416e-08','4.05049e-11','5.15389e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017256, ("CSC", 1, 1, 4, 13), "MEp14_13"))
reports[-1].posNum = 2834
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00157779, 0.00338436, 0), \
                           ValErr(-0.0138787, 0.0842113, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.91425e-06, 9e-05, 0), \
                           900.253, 2834, 2834, -nan)
reports[-1].sigmaresid = ValErr(0.176118, 0.00233933, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000569354, None, 0.000167501, None, -0.00161059, None, 0.000249262, None, -0.00161059, None, 0.000249262, None, -0.0115437, None, 0.000109015, None, -0.0115437, None, 0.000109015, None, 0.176119, None, 0.00716907, None, 0.176119, None, 0.00716907, None)
reports[-1].CovMatrix = ['1.14539e-05','-1.99419e-06','-6.42001e-08','1.74229e-09','0','0','0','0','0','-1.99419e-06','0.00709154','1.05709e-07','5.5322e-08','0','0','0','0','0','-6.42001e-08','1.05709e-07','8.1e-09','4.40332e-11','0','0','0','0','0','1.74229e-09','5.5322e-08','4.40332e-11','5.47245e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017272, ("CSC", 1, 1, 4, 15), "MEp14_15"))
reports[-1].posNum = 2829
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000222258, 0.00330546, 0), \
                           ValErr(-0.0332096, 0.0819577, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.14447e-05, 8.7808e-05, 0), \
                           967.682, 2829, 2829, -nan)
reports[-1].sigmaresid = ValErr(0.171873, 0.00228494, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00301494, None, 0.000252641, None, 0.000275212, None, 0.000360866, None, 0.000275212, None, 0.000360866, None, 0.00235608, None, 0.000293717, None, 0.00235608, None, 0.000293717, None, 0.171879, None, 0.00532116, None, 0.171879, None, 0.00532116, None)
reports[-1].CovMatrix = ['1.0926e-05','-9.43337e-06','-6.05114e-08','1.53118e-09','0','0','0','0','0','-9.43337e-06','0.00671706','2.03254e-07','5.1749e-08','0','0','0','0','0','-6.05114e-08','2.03254e-07','7.71024e-09','4.84538e-11','0','0','0','0','0','1.53118e-09','5.1749e-08','4.84538e-11','5.22096e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017288, ("CSC", 1, 1, 4, 17), "MEp14_17"))
reports[-1].posNum = 2795
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00179511, 0.00329339, 0), \
                           ValErr(-0.0616546, 0.0813538, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.27627e-05, 8.77382e-05, 0), \
                           969.015, 2795, 2795, -nan)
reports[-1].sigmaresid = ValErr(0.171079, 0.00228818, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-3.55091e-05, None, 0.000671052, None, 0.00120944, None, 0.000658361, None, 0.00120944, None, 0.000658361, None, -0.00779293, None, 0.000717342, None, -0.00779293, None, 0.000717342, None, 0.171123, None, 0.00561637, None, 0.171123, None, 0.00561637, None)
reports[-1].CovMatrix = ['1.08464e-05','-1.38535e-06','-5.37107e-08','1.77045e-09','0','0','0','0','0','-1.38535e-06','0.00661844','6.7325e-08','5.45125e-08','0','0','0','0','0','-5.37107e-08','6.7325e-08','7.69799e-09','4.84395e-11','0','0','0','0','0','1.77045e-09','5.45125e-08','4.84395e-11','5.23578e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017304, ("CSC", 1, 1, 4, 19), "MEp14_19"))
reports[-1].posNum = 2732
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00134503, 0.00336439, 0), \
                           ValErr(-0.0502517, 0.0846676, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.04992e-05, 8.91917e-05, 0), \
                           936.305, 2732, 2732, -nan)
reports[-1].sigmaresid = ValErr(0.171763, 0.00232371, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00438469, None, 0.00015953, None, -0.00114372, None, 0.000112503, None, -0.00114372, None, 0.000112503, None, 0.000327633, None, 3.34536e-05, None, 0.000327633, None, 3.34536e-05, None, 0.171775, None, 0.00490651, None, 0.171775, None, 0.00490651, None)
reports[-1].CovMatrix = ['1.13191e-05','-8.26942e-06','-6.40398e-08','1.90828e-09','0','0','0','0','0','-8.26942e-06','0.0071686','3.05969e-07','6.37534e-08','0','0','0','0','0','-6.40398e-08','3.05969e-07','7.95516e-09','4.72782e-11','0','0','0','0','0','1.90828e-09','6.37534e-08','4.72782e-11','5.39965e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017320, ("CSC", 1, 1, 4, 21), "MEp14_21"))
reports[-1].posNum = 3084
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000193667, 0.00317267, 0), \
                           ValErr(-0.0242273, 0.0778293, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.47028e-05, 8.50923e-05, 0), \
                           1053.86, 3084, 3084, -nan)
reports[-1].sigmaresid = ValErr(0.171932, 0.00218919, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00164356, None, -0.000217894, None, -0.000335345, None, -0.000143657, None, -0.000335345, None, -0.000143657, None, -0.00532494, None, -0.000123157, None, -0.00532494, None, -0.000123157, None, 0.171935, None, 0.00571599, None, 0.171935, None, 0.00571599, None)
reports[-1].CovMatrix = ['1.00659e-05','-6.90107e-06','-5.86629e-08','1.52578e-09','0','0','0','0','0','-6.90107e-06','0.0060574','1.42866e-07','4.90429e-08','0','0','0','0','0','-5.86629e-08','1.42866e-07','7.24069e-09','4.37588e-11','0','0','0','0','0','1.52578e-09','4.90429e-08','4.37588e-11','4.79257e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017336, ("CSC", 1, 1, 4, 23), "MEp14_23"))
reports[-1].posNum = 2610
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00171032, 0.00338225, 0), \
                           ValErr(-0.034286, 0.0842245, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.10006e-05, 8.85291e-05, 0), \
                           974.265, 2610, 2610, -nan)
reports[-1].sigmaresid = ValErr(0.16659, 0.00230574, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0018586, None, 0.0009346, None, -0.00105817, None, 0.000931667, None, -0.00105817, None, 0.000931667, None, 0.00671578, None, 0.00107251, None, 0.00671578, None, 0.00107251, None, 0.16661, None, 0.00579186, None, 0.16661, None, 0.00579186, None)
reports[-1].CovMatrix = ['1.14396e-05','1.01086e-05','-7.90568e-08','1.87722e-09','0','0','0','0','0','1.01086e-05','0.00709376','-2.02705e-07','6.17369e-08','0','0','0','0','0','-7.90568e-08','-2.02705e-07','7.8374e-09','4.56875e-11','0','0','0','0','0','1.87722e-09','6.17369e-08','4.56875e-11','5.31646e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017352, ("CSC", 1, 1, 4, 25), "MEp14_25"))
reports[-1].posNum = 2859
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000650054, 0.00325365, 0), \
                           ValErr(-0.0350256, 0.0824742, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.29269e-05, 8.56601e-05, 0), \
                           1030.41, 2859, 2859, -nan)
reports[-1].sigmaresid = ValErr(0.168747, 0.00223158, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00162153, None, 9.41759e-05, None, 0.000316038, None, 4.05908e-05, None, 0.000316038, None, 4.05908e-05, None, -0.00323204, None, 0.000259817, None, -0.00323204, None, 0.000259817, None, 0.168766, None, 0.00539522, None, 0.168766, None, 0.00539522, None)
reports[-1].CovMatrix = ['1.05863e-05','2.58209e-05','-6.3765e-08','1.8093e-09','0','0','0','0','0','2.58209e-05','0.00680199','-4.27259e-07','5.90638e-08','0','0','0','0','0','-6.3765e-08','-4.27259e-07','7.33766e-09','4.14579e-11','0','0','0','0','0','1.8093e-09','5.90638e-08','4.14579e-11','4.97994e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017368, ("CSC", 1, 1, 4, 27), "MEp14_27"))
reports[-1].posNum = 2798
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000720336, 0.00335101, 0), \
                           ValErr(0.0384714, 0.0855136, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.41174e-06, 8.82839e-05, 0), \
                           956.067, 2798, 2798, -nan)
reports[-1].sigmaresid = ValErr(0.171936, 0.00229841, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00208773, None, 0.000427056, None, 0.000770911, None, 0.000411244, None, 0.000770911, None, 0.000411244, None, 0.00196306, None, 0.000474727, None, 0.00196306, None, 0.000474727, None, 0.171942, None, 0.00561114, None, 0.171942, None, 0.00561114, None)
reports[-1].CovMatrix = ['1.12293e-05','-5.09596e-06','-7.17174e-08','1.67589e-09','0','0','0','0','0','-5.09596e-06','0.00731258','-3.33492e-08','5.36783e-08','0','0','0','0','0','-7.17174e-08','-3.33492e-08','7.79406e-09','4.55922e-11','0','0','0','0','0','1.67589e-09','5.36783e-08','4.55922e-11','5.28271e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017384, ("CSC", 1, 1, 4, 29), "MEp14_29"))
reports[-1].posNum = 2949
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000859398, 0.00320752, 0), \
                           ValErr(-0.027923, 0.0791087, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.903e-05, 8.61571e-05, 0), \
                           1005.93, 2949, 2949, -nan)
reports[-1].sigmaresid = ValErr(0.172037, 0.0022401, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000612448, None, -0.00137259, None, 0.00100462, None, -0.00150022, None, 0.00100462, None, -0.00150022, None, -0.00683795, None, -0.00126804, None, -0.00683795, None, -0.00126804, None, 0.172044, None, 0.00504084, None, 0.172044, None, 0.00504084, None)
reports[-1].CovMatrix = ['1.02882e-05','-6.39449e-06','-4.28888e-08','1.62473e-09','0','0','0','0','0','-6.39449e-06','0.00625819','2.12787e-07','4.89567e-08','0','0','0','0','0','-4.28888e-08','2.12787e-07','7.42305e-09','4.96494e-11','0','0','0','0','0','1.62473e-09','4.89567e-08','4.96494e-11','5.01804e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017400, ("CSC", 1, 1, 4, 31), "MEp14_31"))
reports[-1].posNum = 2803
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000193496, 0.00340351, 0), \
                           ValErr(0.0425061, 0.0857657, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.77641e-06, 9.08948e-05, 0), \
                           903.127, 2803, 2803, -nan)
reports[-1].sigmaresid = ValErr(0.175321, 0.00234157, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00348469, None, 0.000138603, None, 0.000197342, None, 0.000271438, None, 0.000197342, None, 0.000271438, None, -0.00153292, None, 0.00033533, None, -0.00153292, None, 0.00033533, None, 0.175328, None, 0.0070977, None, 0.175328, None, 0.0070977, None)
reports[-1].CovMatrix = ['1.15839e-05','-6.60131e-06','-7.09769e-08','1.68992e-09','0','0','0','0','0','-6.60131e-06','0.00735576','-1.37066e-07','5.12053e-08','0','0','0','0','0','-7.09769e-08','-1.37066e-07','8.26186e-09','4.704e-11','0','0','0','0','0','1.68992e-09','5.12053e-08','4.704e-11','5.48297e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017416, ("CSC", 1, 1, 4, 33), "MEp14_33"))
reports[-1].posNum = 2901
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00178919, 0.00321805, 0), \
                           ValErr(0.0752444, 0.0808951, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.31574e-05, 8.52552e-05, 0), \
                           1029.04, 2901, 2901, -nan)
reports[-1].sigmaresid = ValErr(0.169711, 0.00222802, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00426131, None, -0.000892918, None, 0.00166125, None, -0.000756609, None, 0.00166125, None, -0.000756609, None, 0.00667309, None, -0.000981986, None, 0.00667309, None, -0.000981986, None, 0.169739, None, 0.00585954, None, 0.169739, None, 0.00585954, None)
reports[-1].CovMatrix = ['1.03558e-05','-4.26066e-06','-5.55672e-08','1.66585e-09','0','0','0','0','0','-4.26066e-06','0.00654402','-1.73876e-09','5.12518e-08','0','0','0','0','0','-5.55672e-08','-1.73876e-09','7.26845e-09','4.50831e-11','0','0','0','0','0','1.66585e-09','5.12518e-08','4.50831e-11','4.96408e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017432, ("CSC", 1, 1, 4, 35), "MEp14_35"))
reports[-1].posNum = 2812
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00230969, 0.00331817, 0), \
                           ValErr(0.0515235, 0.0829456, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.04267e-05, 8.76957e-05, 0), \
                           960.918, 2812, 2812, -nan)
reports[-1].sigmaresid = ValErr(0.171932, 0.00229263, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00165786, None, -0.00112402, None, -0.00210806, None, -0.000690634, None, -0.00210806, None, -0.000690634, None, -0.00109622, None, -0.000895793, None, -0.00109622, None, -0.000895793, None, 0.171945, None, 0.00602249, None, 0.171945, None, 0.00602249, None)
reports[-1].CovMatrix = ['1.10102e-05','-6.38266e-06','-6.16488e-08','1.69723e-09','0','0','0','0','0','-6.38266e-06','0.00687997','1.61859e-07','5.30224e-08','0','0','0','0','0','-6.16488e-08','1.61859e-07','7.69053e-09','4.73303e-11','0','0','0','0','0','1.69723e-09','5.30224e-08','4.73303e-11','5.25616e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017168, ("CSC", 1, 1, 4, 2), "MEp14_02"))
reports[-1].posNum = 2907
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00104756, 0.00290581, 0), \
                           ValErr(-0.00196327, 0.0722921, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.68039e-07, 7.72399e-05, 0), \
                           1299.32, 2907, 2907, -nan)
reports[-1].sigmaresid = ValErr(0.154757, 0.00202961, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000280982, None, -0.00269033, None, 0.00104466, None, -0.00212212, None, 0.00104466, None, -0.00212212, None, 0.00132612, None, -0.00233001, None, 0.00132612, None, -0.00233001, None, 0.154757, None, 0.00659563, None, 0.154757, None, 0.00659563, None)
reports[-1].CovMatrix = ['8.44371e-06','-3.20172e-06','-3.48724e-08','1.49534e-09','0','0','0','0','0','-3.20172e-06','0.00522615','1.11296e-07','4.88413e-08','0','0','0','0','0','-3.48724e-08','1.11296e-07','5.966e-09','4.76437e-11','0','0','0','0','0','1.49534e-09','4.88413e-08','4.76437e-11','4.11932e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017184, ("CSC", 1, 1, 4, 4), "MEp14_04"))
reports[-1].posNum = 2820
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000739947, 0.00297458, 0), \
                           ValErr(0.0260361, 0.0745152, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.68523e-06, 7.95679e-05, 0), \
                           1284.65, 2820, 2820, -nan)
reports[-1].sigmaresid = ValErr(0.153432, 0.00204303, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00109168, None, -0.00232885, None, 0.000711817, None, -0.00213088, None, 0.000711817, None, -0.00213088, None, -0.00373132, None, -0.00214535, None, -0.00373132, None, -0.00214535, None, 0.153437, None, 0.00520387, None, 0.153437, None, 0.00520387, None)
reports[-1].CovMatrix = ['8.8481e-06','2.97204e-06','-5.61641e-08','1.4836e-09','0','0','0','0','0','2.97204e-06','0.00555251','2.06698e-08','5.16275e-08','0','0','0','0','0','-5.61641e-08','2.06698e-08','6.33104e-09','4.53768e-11','0','0','0','0','0','1.4836e-09','5.16275e-08','4.53768e-11','4.17398e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017200, ("CSC", 1, 1, 4, 6), "MEp14_06"))
reports[-1].posNum = 2907
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000115483, 0.00293789, 0), \
                           ValErr(0.0204698, 0.0729989, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.34432e-06, 7.84051e-05, 0), \
                           1295.29, 2907, 2907, -nan)
reports[-1].sigmaresid = ValErr(0.154972, 0.00203243, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00154049, None, -0.00164586, None, 0.000188564, None, -0.00140927, None, 0.000188564, None, -0.00140927, None, -0.00771181, None, -0.0012971, None, -0.00771181, None, -0.0012971, None, 0.154974, None, 0.00594318, None, 0.154974, None, 0.00594318, None)
reports[-1].CovMatrix = ['8.6312e-06','-1.20343e-06','-4.7619e-08','1.55701e-09','0','0','0','0','0','-1.20343e-06','0.00532883','-1.15535e-07','5.06636e-08','0','0','0','0','0','-4.7619e-08','-1.15535e-07','6.14735e-09','3.99892e-11','0','0','0','0','0','1.55701e-09','5.06636e-08','3.99892e-11','4.13076e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017216, ("CSC", 1, 1, 4, 8), "MEp14_08"))
reports[-1].posNum = 2963
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000471275, 0.00325746, 0), \
                           ValErr(0.0279851, 0.091101, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.12085e-05, 8.72491e-05, 0), \
                           1318.99, 2963, 2963, -nan)
reports[-1].sigmaresid = ValErr(0.155037, 0.00201676, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00158774, None, -0.00136667, None, 6.17474e-05, None, -0.00113934, None, 6.17474e-05, None, -0.00113934, None, -0.00308075, None, -0.00125239, None, -0.00308075, None, -0.00125239, None, 0.155052, None, 0.0056984, None, 0.155052, None, 0.0056984, None)
reports[-1].CovMatrix = ['1.0611e-05','7.43197e-05','-1.08755e-07','-1.28474e-07','0','0','0','0','0','7.43197e-05','0.0082994','-2.24743e-06','-4.90899e-06','0','0','0','0','0','-1.08755e-07','-2.24743e-06','7.6124e-09','3.72835e-09','0','0','0','0','0','-1.28474e-07','-4.90899e-06','3.72835e-09','4.06733e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017232, ("CSC", 1, 1, 4, 10), "MEp14_10"))
reports[-1].posNum = 2877
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0010269, 0.00292798, 0), \
                           ValErr(0.0382148, 0.0722723, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.01958e-05, 7.90015e-05, 0), \
                           1304.77, 2877, 2877, -nan)
reports[-1].sigmaresid = ValErr(0.153745, 0.00202682, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000800736, None, -0.00118605, None, -0.00112373, None, -0.00104566, None, -0.00112373, None, -0.00104566, None, -0.00609352, None, -0.00102555, None, -0.00609352, None, -0.00102555, None, 0.153754, None, 0.00557642, None, 0.153754, None, 0.00557642, None)
reports[-1].CovMatrix = ['8.57305e-06','2.29524e-06','-4.71202e-08','1.69726e-09','0','0','0','0','0','2.29524e-06','0.00522329','3.14322e-08','5.08907e-08','0','0','0','0','0','-4.71202e-08','3.14322e-08','6.24124e-09','4.06345e-11','0','0','0','0','0','1.69726e-09','5.08907e-08','4.06345e-11','4.10802e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017248, ("CSC", 1, 1, 4, 12), "MEp14_12"))
reports[-1].posNum = 2302
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00150414, 0.00352844, 0), \
                           ValErr(0.0105927, 0.0788676, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.29088e-05, 8.70445e-05, 0), \
                           1067.5, 2302, 2302, -nan)
reports[-1].sigmaresid = ValErr(0.152179, 0.0022427, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000324778, None, -0.000237612, None, 0.000588198, None, -0.0002882, None, 0.000588198, None, -0.0002882, None, 0.00526615, None, -0.000470211, None, 0.00526615, None, -0.000470211, None, 0.152203, None, 0.00577364, None, 0.152203, None, 0.00577364, None)
reports[-1].CovMatrix = ['1.24499e-05','-5.78982e-05','-1.25531e-07','1.24943e-09','0','0','0','0','0','-5.78982e-05','0.0062201','8.65788e-07','5.34015e-08','0','0','0','0','0','-1.25531e-07','8.65788e-07','7.57674e-09','4.74963e-11','0','0','0','0','0','1.24943e-09','5.34015e-08','4.74963e-11','5.02972e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017264, ("CSC", 1, 1, 4, 14), "MEp14_14"))
reports[-1].posNum = 2916
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000709467, 0.00296266, 0), \
                           ValErr(0.0264312, 0.0749426, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.10243e-05, 7.79393e-05, 0), \
                           1271.34, 2916, 2916, -nan)
reports[-1].sigmaresid = ValErr(0.156464, 0.00204882, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000226575, None, -9.14667e-05, None, 0.000572425, None, 3.84436e-05, None, 0.000572425, None, 3.84436e-05, None, 0.00459134, None, -3.82601e-05, None, 0.00459134, None, -3.82601e-05, None, 0.15647, None, 0.00589184, None, 0.15647, None, 0.00589184, None)
reports[-1].CovMatrix = ['8.77737e-06','-6.31009e-06','-4.78013e-08','1.45125e-09','0','0','0','0','0','-6.31009e-06','0.0056164','7.64888e-08','4.85905e-08','0','0','0','0','0','-4.78013e-08','7.64888e-08','6.07454e-09','4.3922e-11','0','0','0','0','0','1.45125e-09','4.85905e-08','4.3922e-11','4.19766e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017280, ("CSC", 1, 1, 4, 16), "MEp14_16"))
reports[-1].posNum = 2827
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00227078, 0.00290808, 0), \
                           ValErr(0.00551066, 0.072671, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.31608e-05, 7.66356e-05, 0), \
                           1324.02, 2827, 2827, -nan)
reports[-1].sigmaresid = ValErr(0.15148, 0.0020145, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00256564, None, 0.000947444, None, 0.00179536, None, 0.000904294, None, 0.00179536, None, 0.000904294, None, 0.00489372, None, 0.000738553, None, 0.00489372, None, 0.000738553, None, 0.151501, None, 0.00594084, None, 0.151501, None, 0.00594084, None)
reports[-1].CovMatrix = ['8.45695e-06','-3.99761e-06','-4.44663e-08','1.62072e-09','0','0','0','0','0','-3.99761e-06','0.00528107','-4.22847e-08','4.97805e-08','0','0','0','0','0','-4.44663e-08','-4.22847e-08','5.87302e-09','4.32919e-11','0','0','0','0','0','1.62072e-09','4.97805e-08','4.32919e-11','4.0582e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017296, ("CSC", 1, 1, 4, 18), "MEp14_18"))
reports[-1].posNum = 3047
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00254162, 0.00282022, 0), \
                           ValErr(-0.0280595, 0.0709564, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.18883e-05, 7.51422e-05, 0), \
                           1429.04, 3047, 3047, -nan)
reports[-1].sigmaresid = ValErr(0.151384, 0.00193923, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0034123, None, 0.000493514, None, 0.00189457, None, 0.000327259, None, 0.00189457, None, 0.000327259, None, 0.00720323, None, 0.000238817, None, 0.00720323, None, 0.000238817, None, 0.15141, None, 0.00578642, None, 0.15141, None, 0.00578642, None)
reports[-1].CovMatrix = ['7.95365e-06','-3.85954e-06','-4.92539e-08','1.38072e-09','0','0','0','0','0','-3.85954e-06','0.00503481','1.17341e-08','4.21928e-08','0','0','0','0','0','-4.92539e-08','1.17341e-08','5.64635e-09','3.69833e-11','0','0','0','0','0','1.38072e-09','4.21928e-08','3.69833e-11','3.76062e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017312, ("CSC", 1, 1, 4, 20), "MEp14_20"))
reports[-1].posNum = 2859
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000913338, 0.00362987, 0), \
                           ValErr(0.0480877, 0.0734577, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.87653e-05, 9.61138e-05, 0), \
                           1433.14, 2859, 2859, -nan)
reports[-1].sigmaresid = ValErr(0.146573, 0.00214569, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00020567, None, 0.00203598, None, -0.00120351, None, 0.00205117, None, -0.00120351, None, 0.00205117, None, -0.0052826, None, 0.00210717, None, -0.0052826, None, 0.00210717, None, 0.146592, None, 0.00580985, None, 0.146592, None, 0.00580985, None)
reports[-1].CovMatrix = ['1.3176e-05','-8.06015e-06','-1.88577e-07','-1.36233e-07','0','0','0','0','0','-8.06015e-06','0.00539603','5.17398e-07','-2.1807e-05','0','0','0','0','0','-1.88577e-07','5.17398e-07','9.23786e-09','-2.8493e-09','0','0','0','0','0','-1.36233e-07','-2.1807e-05','-2.8493e-09','4.60398e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017328, ("CSC", 1, 1, 4, 22), "MEp14_22"))
reports[-1].posNum = 3052
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000977197, 0.00288387, 0), \
                           ValErr(-0.0211995, 0.0730972, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.39688e-05, 7.62089e-05, 0), \
                           1345.8, 3052, 3052, -nan)
reports[-1].sigmaresid = ValErr(0.15569, 0.00199276, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000425641, None, 0.000965997, None, -0.00134095, None, 0.0013435, None, -0.00134095, None, 0.0013435, None, -0.000775668, None, 0.00114863, None, -0.000775668, None, 0.00114863, None, 0.1557, None, 0.00624729, None, 0.1557, None, 0.00624729, None)
reports[-1].CovMatrix = ['8.3167e-06','-3.63185e-06','-4.65173e-08','1.39252e-09','0','0','0','0','0','-3.63185e-06','0.00534321','4.44376e-08','4.30142e-08','0','0','0','0','0','-4.65173e-08','4.44376e-08','5.8078e-09','4.25338e-11','0','0','0','0','0','1.39252e-09','4.30142e-08','4.25338e-11','3.97111e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017344, ("CSC", 1, 1, 4, 24), "MEp14_24"))
reports[-1].posNum = 2870
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00229813, 0.0035418, 0), \
                           ValErr(0.0216754, 0.118145, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.7101e-05, 0.000108711, 0), \
                           1379.94, 2870, 2870, -nan)
reports[-1].sigmaresid = ValErr(0.149604, 0.00198771, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00318187, None, 0.000793801, None, 0.00173255, None, 0.000769698, None, 0.00173255, None, 0.000769698, None, 0.00091687, None, 0.000827987, None, 0.00091687, None, 0.000827987, None, 0.149623, None, 0.00590978, None, 0.149623, None, 0.00590978, None)
reports[-1].CovMatrix = ['1.25443e-05','1.28107e-05','1.07799e-07','3.07886e-09','0','0','0','0','0','1.28107e-05','0.0139584','-2.13286e-07','1.15183e-06','0','0','0','0','0','1.07799e-07','-2.13286e-07','1.1818e-08','1.44103e-10','0','0','0','0','0','3.07886e-09','1.15183e-06','1.44103e-10','3.95099e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017360, ("CSC", 1, 1, 4, 26), "MEp14_26"))
reports[-1].posNum = 3286
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000117695, 0.00326667, 0), \
                           ValErr(0.0136696, 0.0983288, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.48178e-05, 8.6143e-05, 0), \
                           1509.31, 3286, 3286, -nan)
reports[-1].sigmaresid = ValErr(0.152856, 0.00201371, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00136373, None, -0.000467942, None, 1.03861e-06, None, -0.000451856, None, 1.03861e-06, None, -0.000451856, None, -0.000624958, None, -0.000471258, None, -0.000624958, None, -0.000471258, None, 0.152858, None, 0.00613569, None, 0.152858, None, 0.00613569, None)
reports[-1].CovMatrix = ['1.06711e-05','-6.32614e-05','-1.15574e-07','-5.22549e-07','0','0','0','0','0','-6.32614e-05','0.00966855','1.95213e-07','-2.89631e-05','0','0','0','0','0','-1.15574e-07','1.95213e-07','7.42062e-09','2.50478e-08','0','0','0','0','0','-5.22549e-07','-2.89631e-05','2.50478e-08','4.05502e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017376, ("CSC", 1, 1, 4, 28), "MEp14_28"))
reports[-1].posNum = 2757
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00148184, 0.00308272, 0), \
                           ValErr(0.0104684, 0.11176, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.45889e-05, 8.092e-05, 0), \
                           1283.16, 2757, 2757, -nan)
reports[-1].sigmaresid = ValErr(0.151925, 0.00220561, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00473739, None, 0.00434345, None, 0.00129287, None, 0.00402801, None, 0.00129287, None, 0.00402801, None, -0.00112843, None, 0.00421617, None, -0.00112843, None, 0.00421617, None, 0.15193, None, 0.0057963, None, 0.15193, None, 0.0057963, None)
reports[-1].CovMatrix = ['9.50316e-06','-2.42672e-05','-6.45589e-08','-6.5956e-07','0','0','0','0','0','-2.42672e-05','0.0124904','1.09257e-06','-7.24435e-06','0','0','0','0','0','-6.45589e-08','1.09257e-06','6.54804e-09','1.20845e-08','0','0','0','0','0','-6.5956e-07','-7.24435e-06','1.20845e-08','4.86471e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017392, ("CSC", 1, 1, 4, 30), "MEp14_30"))
reports[-1].posNum = 2935
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00139767, 0.00332762, 0), \
                           ValErr(-0.0244338, 0.11175, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.77913e-05, 0.000102522, 0), \
                           1413.88, 2935, 2935, -nan)
reports[-1].sigmaresid = ValErr(0.149467, 0.001966, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00474948, None, -0.000575245, None, 0.00125496, None, -0.000634791, None, 0.00125496, None, -0.000634791, None, 0.00263819, None, -0.000718492, None, 0.00263819, None, -0.000718492, None, 0.149473, None, 0.00544211, None, 0.149473, None, 0.00544211, None)
reports[-1].CovMatrix = ['1.1073e-05','-2.27756e-05','-1.66279e-07','5.04927e-09','0','0','0','0','0','-2.27756e-05','0.012488','-4.59953e-07','-1.74913e-06','0','0','0','0','0','-1.66279e-07','-4.59953e-07','1.05108e-08','2.36215e-11','0','0','0','0','0','5.04927e-09','-1.74913e-06','2.36215e-11','3.86516e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017408, ("CSC", 1, 1, 4, 32), "MEp14_32"))
reports[-1].posNum = 2894
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00309783, 0.00357984, 0), \
                           ValErr(-0.0109376, 0.110468, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.13561e-05, 9.43419e-05, 0), \
                           1361.08, 2894, 2894, -nan)
reports[-1].sigmaresid = ValErr(0.151185, 0.00201834, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00218796, None, -0.000433302, None, 0.00262902, None, -0.000312773, None, 0.00262902, None, -0.000312773, None, -0.000588639, None, -0.00027425, None, -0.000588639, None, -0.00027425, None, 0.151197, None, 0.00571325, None, 0.151197, None, 0.00571325, None)
reports[-1].CovMatrix = ['1.28153e-05','3.14253e-06','-1.70393e-07','7.08339e-08','0','0','0','0','0','3.14253e-06','0.0122031','5.96735e-08','-2.93402e-05','0','0','0','0','0','-1.70393e-07','5.96735e-08','8.90039e-09','-2.01071e-09','0','0','0','0','0','7.08339e-08','-2.93402e-05','-2.01071e-09','4.07371e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017424, ("CSC", 1, 1, 4, 34), "MEp14_34"))
reports[-1].posNum = 2933
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-9.49872e-05, 0.00356451, 0), \
                           ValErr(0.0438203, 0.0715578, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.88585e-05, 9.58669e-05, 0), \
                           1380.19, 2933, 2933, -nan)
reports[-1].sigmaresid = ValErr(0.151146, 0.00197394, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00192077, None, -0.0031503, None, -0.000404503, None, -0.00315304, None, -0.000404503, None, -0.00315304, None, 0.00754641, None, -0.00329474, None, 0.00754641, None, -0.00329474, None, 0.151159, None, 0.00540412, None, 0.151159, None, 0.00540412, None)
reports[-1].CovMatrix = ['1.27057e-05','3.08019e-06','-1.70205e-07','3.45089e-08','0','0','0','0','0','3.08019e-06','0.00512052','2.73516e-07','-3.76125e-08','0','0','0','0','0','-1.70205e-07','2.73516e-07','9.19046e-09','-9.61014e-10','0','0','0','0','0','3.45089e-08','-3.76125e-08','-9.61014e-10','3.89645e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017440, ("CSC", 1, 1, 4, 36), "MEp14_36"))
reports[-1].posNum = 2834
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00153723, 0.00289713, 0), \
                           ValErr(0.0589274, 0.0751437, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.53916e-05, 7.77687e-05, 0), \
                           1314.77, 2834, 2834, -nan)
reports[-1].sigmaresid = ValErr(0.152151, 0.00202094, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000510975, None, -0.00147642, None, -0.00169322, None, -0.00117552, None, -0.00169322, None, -0.00117552, None, 0.000177795, None, -0.00112975, None, 0.000177795, None, -0.00112975, None, 0.152172, None, 0.0061704, None, 0.152172, None, 0.0061704, None)
reports[-1].CovMatrix = ['8.39337e-06','1.0026e-06','-3.68624e-08','1.60589e-09','0','0','0','0','0','1.0026e-06','0.00564658','-1.28544e-07','5.2869e-08','0','0','0','0','0','-3.68624e-08','-1.28544e-07','6.04796e-09','4.27959e-11','0','0','0','0','0','1.60589e-09','5.2869e-08','4.27959e-11','4.08421e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021256, ("CSC", 1, 2, 1, 1), "MEp21_01"))
reports[-1].posNum = 5655
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00637353, 0.00503544, 0), \
                           ValErr(0.0396882, 0.0580965, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00012913, 0.000103039, 0), \
                           -2497.79, 5655, 5655, -nan)
reports[-1].sigmaresid = ValErr(0.376349, 0.00353885, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0165865, None, -0.000554012, None, 0.00568112, None, -0.00026622, None, 0.00568112, None, -0.00026622, None, 0.00910444, None, -0.000422101, None, 0.00910444, None, -0.000422101, None, 0.376414, None, 0.0100484, None, 0.376414, None, 0.0100484, None)
reports[-1].CovMatrix = ['2.53557e-05','-3.97313e-07','-5.72606e-08','5.5501e-09','0','0','0','0','0','-3.97313e-07','0.0033752','-8.31569e-08','6.80865e-08','0','0','0','0','0','-5.72606e-08','-8.31569e-08','1.0617e-08','1.03037e-10','0','0','0','0','0','5.5501e-09','6.80865e-08','1.03037e-10','1.25234e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021272, ("CSC", 1, 2, 1, 3), "MEp21_03"))
reports[-1].posNum = 5662
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000601406, 0.00502264, 0), \
                           ValErr(0.0588555, 0.058543, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000107524, 0.00010263, 0), \
                           -2496.38, 5662, 5662, -nan)
reports[-1].sigmaresid = ValErr(0.376049, 0.00353382, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00828521, None, -0.00323643, None, 9.04965e-05, None, -0.00291642, None, 9.04965e-05, None, -0.00291642, None, 0.0072405, None, -0.00322924, None, 0.0072405, None, -0.00322924, None, 0.37612, None, 0.0110609, None, 0.37612, None, 0.0110609, None)
reports[-1].CovMatrix = ['2.52269e-05','-1.34076e-06','-5.1414e-08','5.19413e-09','0','0','0','0','0','-1.34076e-06','0.00342728','1.08964e-07','6.79913e-08','0','0','0','0','0','-5.1414e-08','1.08964e-07','1.05328e-08','1.08244e-10','0','0','0','0','0','5.19413e-09','6.79913e-08','1.08244e-10','1.24879e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021288, ("CSC", 1, 2, 1, 5), "MEp21_05"))
reports[-1].posNum = 5600
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00559914, 0.00509778, 0), \
                           ValErr(0.0166268, 0.0585881, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.44142e-05, 0.000104809, 0), \
                           -2504.67, 5600, 5600, -nan)
reports[-1].sigmaresid = ValErr(0.378448, 0.003576, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0021866, None, -0.00184853, None, 0.00524409, None, -0.00165149, None, 0.00524409, None, -0.00165149, None, 0.00075785, None, -0.00177515, None, 0.00075785, None, -0.00177515, None, 0.37846, None, 0.0104764, None, 0.37846, None, 0.0104764, None)
reports[-1].CovMatrix = ['2.59874e-05','6.58054e-06','-6.65247e-08','5.38217e-09','0','0','0','0','0','6.58054e-06','0.00343257','-1.70325e-07','6.80281e-08','0','0','0','0','0','-6.65247e-08','-1.70325e-07','1.0985e-08','1.04601e-10','0','0','0','0','0','5.38217e-09','6.80281e-08','1.04601e-10','1.27878e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021304, ("CSC", 1, 2, 1, 7), "MEp21_07"))
reports[-1].posNum = 5757
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00294655, 0.00495211, 0), \
                           ValErr(0.0112737, 0.0572238, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.14958e-05, 0.000100226, 0), \
                           -2481.68, 5757, 5757, -nan)
reports[-1].sigmaresid = ValErr(0.372371, 0.00347026, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0053632, None, -0.00455969, None, 0.00258855, None, -0.00458895, None, 0.00258855, None, -0.00458895, None, 0.00203154, None, -0.00474472, None, 0.00203154, None, -0.00474472, None, 0.37238, None, 0.0101964, None, 0.37238, None, 0.0101964, None)
reports[-1].CovMatrix = ['2.45234e-05','4.69488e-06','-6.58716e-08','5.24758e-09','0','0','0','0','0','4.69488e-06','0.00327457','-3.72361e-08','6.51962e-08','0','0','0','0','0','-6.58716e-08','-3.72361e-08','1.00453e-08','9.74926e-11','0','0','0','0','0','5.24758e-09','6.51962e-08','9.74926e-11','1.20428e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021320, ("CSC", 1, 2, 1, 9), "MEp21_09"))
reports[-1].posNum = 5748
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00102487, 0.00487855, 0), \
                           ValErr(0.00631608, 0.0563022, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.87772e-05, 9.83123e-05, 0), \
                           -2390.11, 5748, 5748, -nan)
reports[-1].sigmaresid = ValErr(0.366733, 0.00342039, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00287599, None, -0.00079567, None, 0.000512664, None, -0.000626172, None, 0.000512664, None, -0.000626172, None, -0.000639121, None, -0.000652164, None, -0.000639121, None, -0.000652164, None, 0.366753, None, 0.010052, None, 0.366753, None, 0.010052, None)
reports[-1].CovMatrix = ['2.38003e-05','9.54406e-06','-6.01569e-08','5.11628e-09','0','0','0','0','0','9.54406e-06','0.00316994','-2.93032e-08','6.49268e-08','0','0','0','0','0','-6.01569e-08','-2.93032e-08','9.66532e-09','8.62089e-11','0','0','0','0','0','5.11628e-09','6.49268e-08','8.62089e-11','1.16991e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021336, ("CSC", 1, 2, 1, 11), "MEp21_11"))
reports[-1].posNum = 6125
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00367352, 0.00487915, 0), \
                           ValErr(-0.00622331, 0.0561933, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000106565, 9.86758e-05, 0), \
                           -2737.39, 6125, 6125, -nan)
reports[-1].sigmaresid = ValErr(0.378319, 0.00341814, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0115009, None, -0.000498397, None, 0.00296339, None, -0.000586803, None, 0.00296339, None, -0.000586803, None, 0.00935302, None, -0.00061724, None, 0.00935302, None, -0.00061724, None, 0.378355, None, 0.0104768, None, 0.378355, None, 0.0104768, None)
reports[-1].CovMatrix = ['2.38061e-05','2.71015e-06','-6.52742e-08','4.81825e-09','0','0','0','0','0','2.71015e-06','0.00315768','-1.23607e-07','6.15096e-08','0','0','0','0','0','-6.52742e-08','-1.23607e-07','9.73692e-09','9.35192e-11','0','0','0','0','0','4.81825e-09','6.15096e-08','9.35192e-11','1.16837e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021352, ("CSC", 1, 2, 1, 13), "MEp21_13"))
reports[-1].posNum = 5457
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0034207, 0.00546637, 0), \
                           ValErr(-0.0466932, 0.0704001, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.22675e-05, 0.000105998, 0), \
                           -2532.68, 5457, 5457, -nan)
reports[-1].sigmaresid = ValErr(0.384881, 0.00368414, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00629644, None, -0.0006788, None, -0.00262292, None, -0.000782417, None, -0.00262292, None, -0.000782417, None, 0.00282114, None, -0.000830282, None, 0.00282114, None, -0.000830282, None, 0.384902, None, 0.0102866, None, 0.384902, None, 0.0102866, None)
reports[-1].CovMatrix = ['2.98813e-05','0.000109696','-6.7062e-08','8.03266e-09','0','0','0','0','0','0.000109696','0.00495617','-3.76812e-07','1.1783e-07','0','0','0','0','0','-6.7062e-08','-3.76812e-07','1.12356e-08','1.14969e-10','0','0','0','0','0','8.03266e-09','1.1783e-07','1.14969e-10','1.35729e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021368, ("CSC", 1, 2, 1, 15), "MEp21_15"))
reports[-1].posNum = 5922
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00244343, 0.00489017, 0), \
                           ValErr(0.00276155, 0.0562769, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000132618, 9.9551e-05, 0), \
                           -2571.26, 5922, 5922, -nan)
reports[-1].sigmaresid = ValErr(0.373533, 0.00343226, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00274763, None, -0.00133392, None, -0.00323581, None, -0.00103444, None, -0.00323581, None, -0.00103444, None, -0.00255801, None, -0.00116563, None, -0.00255801, None, -0.00116563, None, 0.373588, None, 0.0105156, None, 0.373588, None, 0.0105156, None)
reports[-1].CovMatrix = ['2.39137e-05','-1.99272e-06','-5.90977e-08','4.98284e-09','0','0','0','0','0','-1.99272e-06','0.00316709','1.08012e-07','6.21098e-08','0','0','0','0','0','-5.90977e-08','1.08012e-07','9.9104e-09','9.42726e-11','0','0','0','0','0','4.98284e-09','6.21098e-08','9.42726e-11','1.17804e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021384, ("CSC", 1, 2, 1, 17), "MEp21_17"))
reports[-1].posNum = 5768
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00141681, 0.00495636, 0), \
                           ValErr(0.0765299, 0.0571981, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.71528e-05, 0.000101198, 0), \
                           -2491.46, 5768, 5768, -nan)
reports[-1].sigmaresid = ValErr(0.372696, 0.00346998, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00176784, None, 0.00237262, None, 0.00101054, None, 0.00251756, None, 0.00101054, None, 0.00251756, None, 0.00548851, None, 0.00229787, None, 0.00548851, None, 0.00229787, None, 0.37276, None, 0.0104392, None, 0.37276, None, 0.0104392, None)
reports[-1].CovMatrix = ['2.45655e-05','3.76154e-06','-7.01265e-08','4.93179e-09','0','0','0','0','0','3.76154e-06','0.00327162','-3.3552e-08','6.4491e-08','0','0','0','0','0','-7.01265e-08','-3.3552e-08','1.02411e-08','9.65387e-11','0','0','0','0','0','4.93179e-09','6.4491e-08','9.65387e-11','1.20408e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021264, ("CSC", 1, 2, 1, 2), "MEp21_02"))
reports[-1].posNum = 5776
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00644269, 0.00472554, 0), \
                           ValErr(0.0592654, 0.0546595, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000198671, 9.59464e-05, 0), \
                           -2232.08, 5776, 5776, -nan)
reports[-1].sigmaresid = ValErr(0.356114, 0.00331328, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00165511, None, 0.00263232, None, 0.00508721, None, 0.00293783, None, 0.00508721, None, 0.00293783, None, 0.00564581, None, 0.00304024, None, 0.00564581, None, 0.00304024, None, 0.356284, None, 0.0117414, None, 0.356284, None, 0.0117414, None)
reports[-1].CovMatrix = ['2.23307e-05','5.43387e-06','-5.80196e-08','4.35578e-09','0','0','0','0','0','5.43387e-06','0.00298766','-3.47586e-08','5.68869e-08','0','0','0','0','0','-5.80196e-08','-3.47586e-08','9.2057e-09','8.39841e-11','0','0','0','0','0','4.35578e-09','5.68869e-08','8.39841e-11','1.09778e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021280, ("CSC", 1, 2, 1, 4), "MEp21_04"))
reports[-1].posNum = 5836
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00349385, 0.00479864, 0), \
                           ValErr(0.0677739, 0.0556846, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.5096e-05, 9.72668e-05, 0), \
                           -2361.12, 5836, 5836, -nan)
reports[-1].sigmaresid = ValErr(0.362634, 0.00335657, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00310717, None, 0.00306476, None, 0.00268582, None, 0.00332264, None, 0.00268582, None, 0.00332264, None, 0.000568168, None, 0.00298075, None, 0.000568168, None, 0.00298075, None, 0.36271, None, 0.0113705, None, 0.36271, None, 0.0113705, None)
reports[-1].CovMatrix = ['2.3027e-05','5.70105e-06','-6.75952e-08','4.53955e-09','0','0','0','0','0','5.70105e-06','0.00310077','1.34741e-08','6.02541e-08','0','0','0','0','0','-6.75952e-08','1.34741e-08','9.46082e-09','8.68816e-11','0','0','0','0','0','4.53955e-09','6.02541e-08','8.68816e-11','1.12666e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021296, ("CSC", 1, 2, 1, 6), "MEp21_06"))
reports[-1].posNum = 5444
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00109433, 0.00487119, 0), \
                           ValErr(-0.00468743, 0.0581538, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.94418e-05, 9.75191e-05, 0), \
                           -2011.63, 5444, 5444, -nan)
reports[-1].sigmaresid = ValErr(0.350135, 0.00335548, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000147747, None, -0.00146949, None, 0.000423075, None, -0.00133103, None, 0.000423075, None, -0.00133103, None, -0.000443752, None, -0.00144905, None, -0.000443752, None, -0.00144905, None, 0.350155, None, 0.0114929, None, 0.350155, None, 0.0114929, None)
reports[-1].CovMatrix = ['2.37285e-05','-3.92496e-05','-9.10183e-08','3.49263e-09','0','0','0','0','0','-3.92496e-05','0.00338186','5.86419e-07','5.9708e-08','0','0','0','0','0','-9.10183e-08','5.86419e-07','9.50997e-09','8.902e-11','0','0','0','0','0','3.49263e-09','5.9708e-08','8.902e-11','1.12593e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021312, ("CSC", 1, 2, 1, 8), "MEp21_08"))
reports[-1].posNum = 5715
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00162051, 0.00477168, 0), \
                           ValErr(0.0441124, 0.0547097, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.41461e-05, 9.63416e-05, 0), \
                           -2246.24, 5715, 5715, -nan)
reports[-1].sigmaresid = ValErr(0.358472, 0.00335296, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000511536, None, 2.19649e-05, None, -0.00140397, None, 9.24937e-05, None, -0.00140397, None, 9.24937e-05, None, -0.0024747, None, 8.77911e-05, None, -0.0024747, None, 8.77911e-05, None, 0.358499, None, 0.0108639, None, 0.358499, None, 0.0108639, None)
reports[-1].CovMatrix = ['2.27689e-05','-2.07705e-06','-5.12127e-08','4.34678e-09','0','0','0','0','0','-2.07705e-06','0.00299315','2.59156e-08','5.59136e-08','0','0','0','0','0','-5.12127e-08','2.59156e-08','9.2817e-09','9.09745e-11','0','0','0','0','0','4.34678e-09','5.59136e-08','9.09745e-11','1.12423e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021328, ("CSC", 1, 2, 1, 10), "MEp21_10"))
reports[-1].posNum = 5719
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000782617, 0.0047448, 0), \
                           ValErr(0.044545, 0.0541918, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.42876e-05, 9.60212e-05, 0), \
                           -2183.87, 5719, 5719, -nan)
reports[-1].sigmaresid = ValErr(0.354486, 0.00331451, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00538902, None, -0.000543422, None, 0.000308088, None, -0.000615051, None, 0.000308088, None, -0.000615051, None, -0.0112561, None, -0.000615218, None, -0.0112561, None, -0.000615218, None, 0.35452, None, 0.0108904, None, 0.35452, None, 0.0108904, None)
reports[-1].CovMatrix = ['2.25131e-05','3.72066e-06','-7.02595e-08','4.20413e-09','0','0','0','0','0','3.72066e-06','0.00293675','2.61295e-08','5.61375e-08','0','0','0','0','0','-7.02595e-08','2.61295e-08','9.22007e-09','8.26812e-11','0','0','0','0','0','4.20413e-09','5.61375e-08','8.26812e-11','1.0986e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021344, ("CSC", 1, 2, 1, 12), "MEp21_12"))
reports[-1].posNum = 5592
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00180516, 0.00462364, 0), \
                           ValErr(-0.00589884, 0.0532291, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.23812e-05, 9.22303e-05, 0), \
                           -1928.31, 5592, 5592, -nan)
reports[-1].sigmaresid = ValErr(0.341601, 0.00323011, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0022239, None, -0.00433096, None, 0.00149454, None, -0.00416005, None, 0.00149454, None, -0.00416005, None, 0.00165793, None, -0.00406783, None, 0.00165793, None, -0.00406783, None, 0.34161, None, 0.0105729, None, 0.34161, None, 0.0105729, None)
reports[-1].CovMatrix = ['2.1378e-05','6.50699e-06','-6.50057e-08','3.75684e-09','0','0','0','0','0','6.50699e-06','0.00283334','-3.71266e-08','4.96461e-08','0','0','0','0','0','-6.50057e-08','-3.71266e-08','8.50643e-09','7.70587e-11','0','0','0','0','0','3.75684e-09','4.96461e-08','7.70587e-11','1.04337e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021360, ("CSC", 1, 2, 1, 14), "MEp21_14"))
reports[-1].posNum = 5662
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00272621, 0.00468009, 0), \
                           ValErr(0.041433, 0.0542895, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00015798, 9.44248e-05, 0), \
                           -2065.68, 5662, 5662, -nan)
reports[-1].sigmaresid = ValErr(0.348498, 0.00327484, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000372625, None, 0.00110628, None, 0.00160246, None, 0.00111097, None, 0.00160246, None, 0.00111097, None, -0.000518489, None, 0.00109588, None, -0.000518489, None, 0.00109588, None, 0.348608, None, 0.0100878, None, 0.348608, None, 0.0100878, None)
reports[-1].CovMatrix = ['2.19033e-05','-2.37695e-07','-6.35631e-08','3.91524e-09','0','0','0','0','0','-2.37695e-07','0.00294735','4.25762e-09','5.55348e-08','0','0','0','0','0','-6.35631e-08','4.25762e-09','8.91605e-09','8.11854e-11','0','0','0','0','0','3.91524e-09','5.55348e-08','8.11854e-11','1.07246e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021376, ("CSC", 1, 2, 1, 16), "MEp21_16"))
reports[-1].posNum = 5333
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00041967, 0.00485229, 0), \
                           ValErr(-0.0543314, 0.055847, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.79547e-05, 9.7792e-05, 0), \
                           -1995.35, 5333, 5333, -nan)
reports[-1].sigmaresid = ValErr(0.351763, 0.00340598, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00553548, None, 0.0030983, None, 0.0010961, None, 0.00343226, None, 0.0010961, None, 0.00343226, None, 0.00764511, None, 0.00346323, None, 0.00764511, None, 0.00346323, None, 0.351831, None, 0.0111311, None, 0.351831, None, 0.0111311, None)
reports[-1].CovMatrix = ['2.35447e-05','5.81748e-06','-5.63727e-08','4.43739e-09','0','0','0','0','0','5.81748e-06','0.00311888','-2.60483e-08','5.58552e-08','0','0','0','0','0','-5.63727e-08','-2.60483e-08','9.56328e-09','8.62019e-11','0','0','0','0','0','4.43739e-09','5.58552e-08','8.62019e-11','1.16007e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021392, ("CSC", 1, 2, 1, 18), "MEp21_18"))
reports[-1].posNum = 5686
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00354709, 0.00481488, 0), \
                           ValErr(0.0214179, 0.0551906, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.04048e-05, 9.71348e-05, 0), \
                           -2281.43, 5686, 5686, -nan)
reports[-1].sigmaresid = ValErr(0.361423, 0.00338918, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00222803, None, -0.00257931, None, 0.00324027, None, -0.00247882, None, 0.00324027, None, -0.00247882, None, 0.00211756, None, -0.00247324, None, 0.00211756, None, -0.00247324, None, 0.361446, None, 0.0114824, None, 0.361446, None, 0.0114824, None)
reports[-1].CovMatrix = ['2.31831e-05','-2.86761e-06','-4.40462e-08','4.63838e-09','0','0','0','0','0','-2.86761e-06','0.00304601','-1.40943e-07','5.45008e-08','0','0','0','0','0','-4.40462e-08','-1.40943e-07','9.43517e-09','9.21782e-11','0','0','0','0','0','4.63838e-09','5.45008e-08','9.21782e-11','1.14866e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021768, ("CSC", 1, 2, 2, 1), "MEp22_01"))
reports[-1].posNum = 1767
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0268633, 0.0240807, 0), \
                           ValErr(-0.243662, 0.569318, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000185065, 0.000264773, 0), \
                           -2273.56, 1767, 1767, -nan)
reports[-1].sigmaresid = ValErr(0.876126, 0.0147381, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0200908, None, 0.004988, None, 0.0183604, None, 0.00541309, None, 0.0183604, None, 0.00541309, None, 0.0184754, None, 0.00544299, None, 0.0184754, None, 0.00544299, None, 0.876272, None, 0.00898314, None, 0.876272, None, 0.00898314, None)
reports[-1].CovMatrix = ['0.000579878','-0.000388229','-3.19326e-06','1.15195e-07','0','0','0','0','0','-0.000388229','0.324123','6.81329e-06','5.25467e-06','0','0','0','0','0','-3.19326e-06','6.81329e-06','7.01048e-08','1.382e-09','0','0','0','0','0','1.15195e-07','5.25467e-06','1.382e-09','0.000217213','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021784, ("CSC", 1, 2, 2, 3), "MEp22_03"))
reports[-1].posNum = 1284
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00391971, 0.0293643, 0), \
                           ValErr(0.119601, 0.593925, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.22142e-06, 0.000292771, 0), \
                           -1453.12, 1284, 1284, -nan)
reports[-1].sigmaresid = ValErr(0.750332, 0.0148063, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00369555, None, 0.00100447, None, 0.00437607, None, 0.00159583, None, 0.00437607, None, 0.00159583, None, 0.0163671, None, 0.00107222, None, 0.0163671, None, 0.00107222, None, 0.750353, None, 0.00876279, None, 0.750353, None, 0.00876279, None)
reports[-1].CovMatrix = ['0.00086226','-0.000125861','-6.027e-06','5.86915e-08','0','0','0','0','0','-0.000125861','0.352747','2.06273e-06','3.33416e-06','0','0','0','0','0','-6.027e-06','2.06273e-06','8.57147e-08','1.24619e-09','0','0','0','0','0','5.86915e-08','3.33416e-06','1.24619e-09','0.00021923','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021800, ("CSC", 1, 2, 2, 5), "MEp22_05"))
reports[-1].posNum = 1391
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0208644, 0.0279095, 0), \
                           ValErr(0.0122977, 0.662221, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000198208, 0.000292762, 0), \
                           -1698.56, 1391, 1391, -nan)
reports[-1].sigmaresid = ValErr(0.820508, 0.0155562, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000901415, None, -0.00063166, None, -0.00988094, None, -0.000707691, None, -0.00988094, None, -0.000707691, None, 0.0081327, None, -0.000579023, None, 0.0081327, None, -0.000579023, None, 0.820642, None, 0.00905293, None, 0.820642, None, 0.00905293, None)
reports[-1].CovMatrix = ['0.000778942','0.00356707','-4.85466e-06','1.64149e-07','0','0','0','0','0','0.00356707','0.438537','-1.08029e-05','6.60383e-06','0','0','0','0','0','-4.85466e-06','-1.08029e-05','8.57094e-08','1.07332e-09','0','0','0','0','0','1.64149e-07','6.60383e-06','1.07332e-09','0.000241998','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021816, ("CSC", 1, 2, 2, 7), "MEp22_07"))
reports[-1].posNum = 1771
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0064884, 0.0238297, 0), \
                           ValErr(0.0317348, 0.553179, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.93027e-05, 0.000251359, 0), \
                           -2291.29, 1771, 1771, -nan)
reports[-1].sigmaresid = ValErr(0.882357, 0.0148257, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0100819, None, -0.00136727, None, 0.00424103, None, -0.00113093, None, 0.00424103, None, -0.00113093, None, -0.0521171, None, -0.000968672, None, -0.0521171, None, -0.000968672, None, 0.882372, None, 0.00874783, None, 0.882372, None, 0.00874783, None)
reports[-1].CovMatrix = ['0.000567853','0.00045247','-2.84233e-06','1.23504e-07','0','0','0','0','0','0.00045247','0.306007','-2.55391e-06','4.49291e-06','0','0','0','0','0','-2.84233e-06','-2.55391e-06','6.31815e-08','1.16352e-09','0','0','0','0','0','1.23504e-07','4.49291e-06','1.16352e-09','0.000219804','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021832, ("CSC", 1, 2, 2, 9), "MEp22_09"))
reports[-1].posNum = 1802
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00263196, 0.0225129, 0), \
                           ValErr(0.153102, 0.547418, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.16263e-05, 0.000235823, 0), \
                           -2349.12, 1802, 1802, -nan)
reports[-1].sigmaresid = ValErr(0.891069, 0.0148426, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0150456, None, -0.00447127, None, 0.000314318, None, -0.00446326, None, 0.000314318, None, -0.00446326, None, -0.0387302, None, -0.00425198, None, -0.0387302, None, -0.00425198, None, 0.891129, None, 0.00942215, None, 0.891129, None, 0.00942215, None)
reports[-1].CovMatrix = ['0.000506829','-0.000303203','-1.91613e-06','1.14713e-07','0','0','0','0','0','-0.000303203','0.299666','1.95961e-06','4.07768e-06','0','0','0','0','0','-1.91613e-06','1.95961e-06','5.56126e-08','1.39243e-09','0','0','0','0','0','1.14713e-07','4.07768e-06','1.39243e-09','0.000220304','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021848, ("CSC", 1, 2, 2, 11), "MEp22_11"))
reports[-1].posNum = 1635
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0223638, 0.0255849, 0), \
                           ValErr(0.0138998, 0.590149, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000228745, 0.000272525, 0), \
                           -2047, 1635, 1635, -nan)
reports[-1].sigmaresid = ValErr(0.846243, 0.0147985, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0491818, None, -0.00186723, None, 0.0100033, None, -0.00187362, None, 0.0100033, None, -0.00187362, None, 0.012147, None, -0.0018897, None, 0.012147, None, -0.0018897, None, 0.846426, None, 0.00954859, None, 0.846426, None, 0.00954859, None)
reports[-1].CovMatrix = ['0.000654585','0.000270004','-4.00611e-06','1.08663e-07','0','0','0','0','0','0.000270004','0.348276','2.72014e-06','4.81592e-06','0','0','0','0','0','-4.00611e-06','2.72014e-06','7.42701e-08','1.18225e-09','0','0','0','0','0','1.08663e-07','4.81592e-06','1.18225e-09','0.000218999','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021864, ("CSC", 1, 2, 2, 13), "MEp22_13"))
reports[-1].posNum = 1742
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0240285, 0.0229414, 0), \
                           ValErr(0.347345, 0.574835, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000285269, 0.000243201, 0), \
                           -2183.76, 1742, 1742, -nan)
reports[-1].sigmaresid = ValErr(0.847574, 0.0143588, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00926983, None, -0.0047822, None, 0.0107959, None, -0.00498508, None, 0.0107959, None, -0.00498508, None, -0.0209312, None, -0.00480678, None, -0.0209312, None, -0.00480678, None, 0.848015, None, 0.0084254, None, 0.848015, None, 0.0084254, None)
reports[-1].CovMatrix = ['0.000526309','0.000956594','-2.57355e-06','1.34367e-07','0','0','0','0','0','0.000956594','0.330435','-3.58026e-06','3.67695e-06','0','0','0','0','0','-2.57355e-06','-3.58026e-06','5.91466e-08','1.00224e-09','0','0','0','0','0','1.34367e-07','3.67695e-06','1.00224e-09','0.000206178','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021880, ("CSC", 1, 2, 2, 15), "MEp22_15"))
reports[-1].posNum = 1682
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00847415, 0.0242053, 0), \
                           ValErr(-0.0795738, 0.61439, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.82853e-05, 0.000252379, 0), \
                           -2091.39, 1682, 1682, -nan)
reports[-1].sigmaresid = ValErr(0.839, 0.0144654, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0211047, None, -0.001387, None, 0.0104585, None, -0.0014036, None, 0.0104585, None, -0.0014036, None, 0.00478753, None, -0.0014008, None, 0.00478753, None, -0.0014008, None, 0.839016, None, 0.00991449, None, 0.839016, None, 0.00991449, None)
reports[-1].CovMatrix = ['0.000585898','-0.00167159','-3.15252e-06','9.08235e-08','0','0','0','0','0','-0.00167159','0.377475','-8.01837e-06','3.94303e-06','0','0','0','0','0','-3.15252e-06','-8.01837e-06','6.36951e-08','9.84058e-10','0','0','0','0','0','9.08235e-08','3.94303e-06','9.84058e-10','0.000209249','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021896, ("CSC", 1, 2, 2, 17), "MEp22_17"))
reports[-1].posNum = 1664
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000956219, 0.0239765, 0), \
                           ValErr(-0.0805102, 0.567684, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.65843e-05, 0.000245259, 0), \
                           -2031.23, 1664, 1664, -nan)
reports[-1].sigmaresid = ValErr(0.820168, 0.0142171, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0157381, None, 0.000609654, None, -3.42389e-05, None, 0.000492067, None, -3.42389e-05, None, 0.000492067, None, 0.0255309, None, 0.000313352, None, 0.0255309, None, 0.000313352, None, 0.820172, None, 0.0101547, None, 0.820172, None, 0.0101547, None)
reports[-1].CovMatrix = ['0.000574871','-0.000947591','-3.19555e-06','7.3081e-08','0','0','0','0','0','-0.000947591','0.322265','7.96287e-06','3.93371e-06','0','0','0','0','0','-3.19555e-06','7.96287e-06','6.01521e-08','1.23869e-09','0','0','0','0','0','7.3081e-08','3.93371e-06','1.23869e-09','0.000202127','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021912, ("CSC", 1, 2, 2, 19), "MEp22_19"))
reports[-1].posNum = 1766
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0382727, 0.0233532, 0), \
                           ValErr(0.0899325, 0.628748, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000204938, 0.000252056, 0), \
                           -2313.55, 1766, 1766, -nan)
reports[-1].sigmaresid = ValErr(0.896837, 0.0150905, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0599422, None, -0.0048164, None, 0.0314657, None, -0.00507783, None, 0.0314657, None, -0.00507783, None, 0.0468739, None, -0.00542507, None, 0.0468739, None, -0.00542507, None, 0.897005, None, 0.00988779, None, 0.897005, None, 0.00988779, None)
reports[-1].CovMatrix = ['0.000545371','-0.00197941','-2.23969e-06','1.10795e-07','0','0','0','0','0','-0.00197941','0.395324','-2.91526e-06','3.76384e-06','0','0','0','0','0','-2.23969e-06','-2.91526e-06','6.35321e-08','1.482e-09','0','0','0','0','0','1.10795e-07','3.76384e-06','1.482e-09','0.000227726','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021928, ("CSC", 1, 2, 2, 21), "MEp22_21"))
reports[-1].posNum = 1587
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0150836, 0.023194, 0), \
                           ValErr(-0.140656, 0.559238, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000238235, 0.000248629, 0), \
                           -2044.68, 1587, 1587, -nan)
reports[-1].sigmaresid = ValErr(0.877597, 0.0155768, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00840668, None, 0.000909915, None, -0.00813775, None, 0.00107764, None, -0.00813775, None, 0.00107764, None, -0.00323881, None, 0.00134423, None, -0.00323881, None, 0.00134423, None, 0.877897, None, 0.0104235, None, 0.877897, None, 0.0104235, None)
reports[-1].CovMatrix = ['0.000537962','-0.000317428','-1.8041e-06','1.29307e-07','0','0','0','0','0','-0.000317428','0.312747','9.43878e-06','5.59922e-06','0','0','0','0','0','-1.8041e-06','9.43878e-06','6.18166e-08','1.73907e-09','0','0','0','0','0','1.29307e-07','5.59922e-06','1.73907e-09','0.000242639','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021944, ("CSC", 1, 2, 2, 23), "MEp22_23"))
reports[-1].posNum = 1955
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00345929, 0.0210046, 0), \
                           ValErr(0.0713582, 0.504642, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.33374e-06, 0.000228083, 0), \
                           -2426.55, 1955, 1955, -nan)
reports[-1].sigmaresid = ValErr(0.837165, 0.0133882, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0311151, None, -0.0021726, None, 0.00375518, None, -0.00197558, None, 0.00375518, None, -0.00197558, None, -0.00760013, None, -0.00212101, None, -0.00760013, None, -0.00212101, None, 0.837166, None, 0.0103499, None, 0.837166, None, 0.0103499, None)
reports[-1].CovMatrix = ['0.000441195','-0.000309446','-2.06972e-06','1.20646e-07','0','0','0','0','0','-0.000309446','0.254663','1.5636e-07','3.88439e-06','0','0','0','0','0','-2.06972e-06','1.5636e-07','5.20217e-08','7.57779e-10','0','0','0','0','0','1.20646e-07','3.88439e-06','7.57779e-10','0.000179246','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021960, ("CSC", 1, 2, 2, 25), "MEp22_25"))
reports[-1].posNum = 1611
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0013137, 0.0275687, 0), \
                           ValErr(-0.519642, 0.577735, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.87454e-05, 0.000289548, 0), \
                           -1967.11, 1611, 1611, -nan)
reports[-1].sigmaresid = ValErr(0.820458, 0.014454, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00644654, None, -0.00242877, None, -0.00230199, None, -0.00236888, None, -0.00230199, None, -0.00236888, None, -0.0614561, None, -0.00244423, None, -0.0614561, None, -0.00244423, None, 0.820677, None, 0.00888243, None, 0.820677, None, 0.00888243, None)
reports[-1].CovMatrix = ['0.000760033','0.00155876','-5.34909e-06','1.4426e-07','0','0','0','0','0','0.00155876','0.333778','-1.58852e-05','4.69615e-06','0','0','0','0','0','-5.34909e-06','-1.58852e-05','8.3838e-08','5.18133e-10','0','0','0','0','0','1.4426e-07','4.69615e-06','5.18133e-10','0.000208921','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021976, ("CSC", 1, 2, 2, 27), "MEp22_27"))
reports[-1].posNum = 1520
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0335662, 0.0268726, 0), \
                           ValErr(0.0801494, 0.639736, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000199237, 0.000279419, 0), \
                           -2005.18, 1520, 1520, -nan)
reports[-1].sigmaresid = ValErr(0.905076, 0.0164152, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.023034, None, -0.000266447, None, 0.0239426, None, -0.000389031, None, 0.0239426, None, -0.000389031, None, 0.0322786, None, -0.000406475, None, 0.0322786, None, -0.000406475, None, 0.905227, None, 0.00784528, None, 0.905227, None, 0.00784528, None)
reports[-1].CovMatrix = ['0.000722137','0.00260432','-3.67929e-06','1.86101e-07','0','0','0','0','0','0.00260432','0.409263','-1.28165e-05','6.93115e-06','0','0','0','0','0','-3.67929e-06','-1.28165e-05','7.80751e-08','1.34744e-09','0','0','0','0','0','1.86101e-07','6.93115e-06','1.34744e-09','0.000269462','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021992, ("CSC", 1, 2, 2, 29), "MEp22_29"))
reports[-1].posNum = 1854
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00364314, 0.0223028, 0), \
                           ValErr(-0.22986, 0.551489, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.27041e-05, 0.000231673, 0), \
                           -2402.89, 1854, 1854, -nan)
reports[-1].sigmaresid = ValErr(0.884357, 0.0145227, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0115719, None, -0.00158433, None, 0.00184521, None, -0.0012777, None, 0.00184521, None, -0.0012777, None, -0.00564448, None, -0.00121952, None, -0.00564448, None, -0.00121952, None, 0.884416, None, 0.0105797, None, 0.884416, None, 0.0105797, None)
reports[-1].CovMatrix = ['0.000497415','-0.000787848','-1.99005e-06','1.25239e-07','0','0','0','0','0','-0.000787848','0.304141','1.34555e-06','4.73019e-06','0','0','0','0','0','-1.99005e-06','1.34555e-06','5.36726e-08','1.16351e-09','0','0','0','0','0','1.25239e-07','4.73019e-06','1.16351e-09','0.000210911','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604022008, ("CSC", 1, 2, 2, 31), "MEp22_31"))
reports[-1].posNum = 1623
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00659967, 0.0246484, 0), \
                           ValErr(0.526887, 0.619206, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000130632, 0.000263412, 0), \
                           -2171.19, 1623, 1623, -nan)
reports[-1].sigmaresid = ValErr(0.922031, 0.0161834, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0080586, None, -0.00392583, None, -0.00127894, None, -0.00369708, None, -0.00127894, None, -0.00369708, None, -0.0132788, None, -0.00400874, None, -0.0132788, None, -0.00400874, None, 0.922313, None, 0.00942325, None, 0.922313, None, 0.00942325, None)
reports[-1].CovMatrix = ['0.000607541','-0.000490866','-2.39749e-06','1.44616e-07','0','0','0','0','0','-0.000490866','0.383416','-2.72331e-06','4.14734e-06','0','0','0','0','0','-2.39749e-06','-2.72331e-06','6.93861e-08','1.75844e-09','0','0','0','0','0','1.44616e-07','4.14734e-06','1.75844e-09','0.000261904','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604022024, ("CSC", 1, 2, 2, 33), "MEp22_33"))
reports[-1].posNum = 1938
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00247144, 0.0223058, 0), \
                           ValErr(-0.0723157, 0.529577, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.93892e-05, 0.000232908, 0), \
                           -2502.98, 1938, 1938, -nan)
reports[-1].sigmaresid = ValErr(0.880365, 0.0141405, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0245195, None, 0.000427867, None, -0.00120944, None, 0.000856844, None, -0.00120944, None, 0.000856844, None, 0.00291904, None, 0.00078252, None, 0.00291904, None, 0.00078252, None, 0.880378, None, 0.0106483, None, 0.880378, None, 0.0106483, None)
reports[-1].CovMatrix = ['0.000497547','0.000104927','-2.30129e-06','1.03378e-07','0','0','0','0','0','0.000104927','0.280452','-2.35739e-06','4.35018e-06','0','0','0','0','0','-2.30129e-06','-2.35739e-06','5.42462e-08','1.11205e-09','0','0','0','0','0','1.03378e-07','4.35018e-06','1.11205e-09','0.000199956','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604022040, ("CSC", 1, 2, 2, 35), "MEp22_35"))
reports[-1].posNum = 1423
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.003475, 0.0255158, 0), \
                           ValErr(0.0316413, 0.612285, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.42343e-05, 0.000259536, 0), \
                           -1809.55, 1423, 1423, -nan)
reports[-1].sigmaresid = ValErr(0.863039, 0.0161774, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0433963, None, 0.00312789, None, 0.00155526, None, 0.00296622, None, 0.00155526, None, 0.00296622, None, 0.0104021, None, 0.00290001, None, 0.0104021, None, 0.00290001, None, 0.863051, None, 0.0088088, None, 0.863051, None, 0.0088088, None)
reports[-1].CovMatrix = ['0.000651056','-1.29202e-06','-2.93164e-06','1.4373e-07','0','0','0','0','0','-1.29202e-06','0.374893','-2.67572e-06','5.16715e-06','0','0','0','0','0','-2.93164e-06','-2.67572e-06','6.73588e-08','1.39441e-09','0','0','0','0','0','1.4373e-07','5.16715e-06','1.39441e-09','0.000261712','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021776, ("CSC", 1, 2, 2, 2), "MEp22_02"))
reports[-1].posNum = 1438
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00451959, 0.0289424, 0), \
                           ValErr(0.315554, 0.620793, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000148921, 0.000301869, 0), \
                           -1790.75, 1438, 1438, -nan)
reports[-1].sigmaresid = ValErr(0.840626, 0.0156754, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.021881, None, -0.000515851, None, 0.00510428, None, -0.000356849, None, 0.00510428, None, -0.000356849, None, -0.0519496, None, -0.000644618, None, -0.0519496, None, -0.000644618, None, 0.840747, None, 0.0109682, None, 0.840747, None, 0.0109682, None)
reports[-1].CovMatrix = ['0.000837661','-0.00113963','-5.60946e-06','1.05463e-07','0','0','0','0','0','-0.00113963','0.385384','8.74921e-06','4.75617e-06','0','0','0','0','0','-5.60946e-06','8.74921e-06','9.11246e-08','1.37922e-09','0','0','0','0','0','1.05463e-07','4.75617e-06','1.37922e-09','0.000245721','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021792, ("CSC", 1, 2, 2, 4), "MEp22_04"))
reports[-1].posNum = 1315
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0156638, 0.0295702, 0), \
                           ValErr(-0.0587231, 0.605523, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.40003e-05, 0.000285996, 0), \
                           -1540.88, 1315, 1315, -nan)
reports[-1].sigmaresid = ValErr(0.781, 0.0152287, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00567121, None, 0.00171427, None, -0.00894765, None, 0.00215032, None, -0.00894765, None, 0.00215032, None, -0.0374799, None, 0.00196349, None, -0.0374799, None, 0.00196349, None, 0.781047, None, 0.0100776, None, 0.781047, None, 0.0100776, None)
reports[-1].CovMatrix = ['0.000874395','0.000682189','-5.78889e-06','1.26134e-07','0','0','0','0','0','0.000682189','0.366658','-1.78824e-06','5.91434e-06','0','0','0','0','0','-5.78889e-06','-1.78824e-06','8.17938e-08','9.80738e-10','0','0','0','0','0','1.26134e-07','5.91434e-06','9.80738e-10','0.000231915','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021808, ("CSC", 1, 2, 2, 6), "MEp22_06"))
reports[-1].posNum = 1631
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000943165, 0.0253201, 0), \
                           ValErr(0.371361, 0.553492, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.46166e-05, 0.000266485, 0), \
                           -1944.52, 1631, 1631, -nan)
reports[-1].sigmaresid = ValErr(0.797138, 0.0139567, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0103258, None, -0.00475622, None, 0.00305913, None, -0.00462885, None, 0.00305913, None, -0.00462885, None, 0.00834103, None, -0.00484563, None, 0.00834103, None, -0.00484563, None, 0.797268, None, 0.00803867, None, 0.797268, None, 0.00803867, None)
reports[-1].CovMatrix = ['0.000641107','0.00073494','-4.2214e-06','1.34396e-07','0','0','0','0','0','0.00073494','0.306353','-5.31424e-06','4.03716e-06','0','0','0','0','0','-4.2214e-06','-5.31424e-06','7.10144e-08','4.91925e-10','0','0','0','0','0','1.34396e-07','4.03716e-06','4.91925e-10','0.00019479','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021824, ("CSC", 1, 2, 2, 8), "MEp22_08"))
reports[-1].posNum = 1752
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00358904, 0.0224315, 0), \
                           ValErr(0.120856, 0.556185, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.73388e-05, 0.000232209, 0), \
                           -2226.92, 1752, 1752, -nan)
reports[-1].sigmaresid = ValErr(0.862541, 0.014571, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0134781, None, -0.00292967, None, 0.0020091, None, -0.00327292, None, 0.0020091, None, -0.00327292, None, -0.00777617, None, -0.00325115, None, -0.00777617, None, -0.00325115, None, 0.862566, None, 0.0118309, None, 0.862566, None, 0.0118309, None)
reports[-1].CovMatrix = ['0.000503171','0.000606122','-2.0514e-06','1.43553e-07','0','0','0','0','0','0.000606122','0.309342','-5.78794e-06','3.50023e-06','0','0','0','0','0','-2.0514e-06','-5.78794e-06','5.39209e-08','8.59862e-10','0','0','0','0','0','1.43553e-07','3.50023e-06','8.59862e-10','0.000212317','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021840, ("CSC", 1, 2, 2, 10), "MEp22_10"))
reports[-1].posNum = 1872
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.012336, 0.0220997, 0), \
                           ValErr(-0.192612, 0.531017, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.95009e-05, 0.000238718, 0), \
                           -2410.99, 1872, 1872, -nan)
reports[-1].sigmaresid = ValErr(0.877193, 0.0143357, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00604823, None, 0.00199603, None, 0.00944929, None, 0.00260436, None, 0.00944929, None, 0.00260436, None, -0.00281377, None, 0.00253484, None, -0.00281377, None, 0.00253484, None, 0.877258, None, 0.00994168, None, 0.877258, None, 0.00994168, None)
reports[-1].CovMatrix = ['0.000488395','-0.00035674','-2.0993e-06','1.14519e-07','0','0','0','0','0','-0.00035674','0.281979','1.1665e-05','5.00333e-06','0','0','0','0','0','-2.0993e-06','1.1665e-05','5.69864e-08','1.34577e-09','0','0','0','0','0','1.14519e-07','5.00333e-06','1.34577e-09','0.000205513','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021856, ("CSC", 1, 2, 2, 12), "MEp22_12"))
reports[-1].posNum = 1572
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0131953, 0.0253611, 0), \
                           ValErr(0.13925, 0.545063, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000126533, 0.000257184, 0), \
                           -1863.92, 1572, 1572, -nan)
reports[-1].sigmaresid = ValErr(0.79195, 0.0141235, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0172908, None, -1.62685e-05, None, 0.00562137, None, 0.000564194, None, 0.00562137, None, 0.000564194, None, 0.00788579, None, 0.000389717, None, 0.00788579, None, 0.000389717, None, 0.792042, None, 0.00973892, None, 0.792042, None, 0.00973892, None)
reports[-1].CovMatrix = ['0.000643185','5.24234e-05','-4.01764e-06','8.52171e-08','0','0','0','0','0','5.24234e-05','0.297094','-4.6267e-06','2.7772e-06','0','0','0','0','0','-4.01764e-06','-4.6267e-06','6.61434e-08','9.33776e-10','0','0','0','0','0','8.52171e-08','2.7772e-06','9.33776e-10','0.000199476','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021872, ("CSC", 1, 2, 2, 14), "MEp22_14"))
reports[-1].posNum = 2087
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0132131, 0.0217501, 0), \
                           ValErr(-0.104363, 0.524741, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.67392e-05, 0.000234781, 0), \
                           -2664.01, 2087, 2087, -nan)
reports[-1].sigmaresid = ValErr(0.86721, 0.0134226, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0282175, None, -0.0018718, None, -0.00943943, None, -0.00175111, None, -0.00943943, None, -0.00175111, None, 0.0455998, None, -0.00184371, None, 0.0455998, None, -0.00184371, None, 0.867261, None, 0.0107279, None, 0.867261, None, 0.0107279, None)
reports[-1].CovMatrix = ['0.000473068','-0.000628873','-2.48722e-06','7.21243e-08','0','0','0','0','0','-0.000628873','0.275353','5.82486e-06','4.49327e-06','0','0','0','0','0','-2.48722e-06','5.82486e-06','5.51219e-08','1.28449e-09','0','0','0','0','0','7.21243e-08','4.49327e-06','1.28449e-09','0.000180169','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021888, ("CSC", 1, 2, 2, 16), "MEp22_16"))
reports[-1].posNum = 1941
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0158447, 0.0219257, 0), \
                           ValErr(0.105482, 0.532751, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000105589, 0.000231235, 0), \
                           -2538.72, 1941, 1941, -nan)
reports[-1].sigmaresid = ValErr(0.894929, 0.0143631, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0262669, None, -0.000599017, None, 0.0121523, None, -0.000853932, None, 0.0121523, None, -0.000853932, None, 0.0211749, None, -0.000810641, None, 0.0211749, None, -0.000810641, None, 0.895003, None, 0.012324, None, 0.895003, None, 0.012324, None)
reports[-1].CovMatrix = ['0.000480735','-0.000308417','-1.90707e-06','1.13887e-07','0','0','0','0','0','-0.000308417','0.283824','4.02999e-06','3.85231e-06','0','0','0','0','0','-1.90707e-06','4.02999e-06','5.34696e-08','1.2125e-09','0','0','0','0','0','1.13887e-07','3.85231e-06','1.2125e-09','0.000206301','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021904, ("CSC", 1, 2, 2, 18), "MEp22_18"))
reports[-1].posNum = 1669
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0074224, 0.0240154, 0), \
                           ValErr(0.36485, 0.531146, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.67973e-05, 0.000251693, 0), \
                           -1989.5, 1669, 1669, -nan)
reports[-1].sigmaresid = ValErr(0.796993, 0.0137946, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00300127, None, 0.000157908, None, 0.00221355, None, 0.000208794, None, 0.00221355, None, 0.000208794, None, 0.0118832, None, 0.000237343, None, 0.0118832, None, 0.000237343, None, 0.797128, None, 0.00857431, None, 0.797128, None, 0.00857431, None)
reports[-1].CovMatrix = ['0.000576737','0.000829111','-3.50729e-06','1.0232e-07','0','0','0','0','0','0.000829111','0.282116','-1.50573e-06','4.16056e-06','0','0','0','0','0','-3.50729e-06','-1.50573e-06','6.33493e-08','9.17866e-10','0','0','0','0','0','1.0232e-07','4.16056e-06','9.17866e-10','0.000190293','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021920, ("CSC", 1, 2, 2, 20), "MEp22_20"))
reports[-1].posNum = 1719
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0141747, 0.0231594, 0), \
                           ValErr(-0.0436755, 0.570673, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000244114, 0.000251235, 0), \
                           -2295.66, 1719, 1719, -nan)
reports[-1].sigmaresid = ValErr(0.919887, 0.0156879, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0257821, None, 0.00155162, None, 0.00770624, None, 0.00150499, None, 0.00770624, None, 0.00150499, None, 0.00149447, None, 0.00143235, None, 0.00149447, None, 0.00143235, None, 0.920163, None, 0.0121246, None, 0.920163, None, 0.0121246, None)
reports[-1].CovMatrix = ['0.000536356','3.29059e-05','-1.66568e-06','1.76689e-07','0','0','0','0','0','3.29059e-05','0.325668','6.87338e-06','5.25772e-06','0','0','0','0','0','-1.66568e-06','6.87338e-06','6.31189e-08','1.63509e-09','0','0','0','0','0','1.76689e-07','5.25772e-06','1.63509e-09','0.000246113','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021936, ("CSC", 1, 2, 2, 22), "MEp22_22"))
reports[-1].posNum = 1830
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00452678, 0.0221619, 0), \
                           ValErr(-0.439648, 0.536598, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.98149e-05, 0.000235706, 0), \
                           -2322.14, 1830, 1830, -nan)
reports[-1].sigmaresid = ValErr(0.860695, 0.0142266, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0124726, None, 0.00394185, None, 0.00247924, None, 0.00410296, None, 0.00247924, None, 0.00410296, None, -0.00562016, None, 0.00394625, None, -0.00562016, None, 0.00394625, None, 0.860875, None, 0.0112595, None, 0.860875, None, 0.0112595, None)
reports[-1].CovMatrix = ['0.000491148','0.000257154','-2.18797e-06','1.29507e-07','0','0','0','0','0','0.000257154','0.287938','-8.44708e-07','4.26876e-06','0','0','0','0','0','-2.18797e-06','-8.44708e-07','5.55573e-08','1.20259e-09','0','0','0','0','0','1.29507e-07','4.26876e-06','1.20259e-09','0.000202399','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021952, ("CSC", 1, 2, 2, 24), "MEp22_24"))
reports[-1].posNum = 1950
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00673589, 0.0225172, 0), \
                           ValErr(-0.0623644, 0.504558, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.33107e-05, 0.000243901, 0), \
                           -2400.33, 1950, 1950, -nan)
reports[-1].sigmaresid = ValErr(0.828616, 0.0132685, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00319107, None, -0.000715086, None, -0.00471987, None, -0.000580227, None, -0.00471987, None, -0.000580227, None, -0.0141065, None, -0.00060789, None, -0.0141065, None, -0.00060789, None, 0.828624, None, 0.00925921, None, 0.828624, None, 0.00925921, None)
reports[-1].CovMatrix = ['0.000507024','-0.000973704','-3.02339e-06','1.11023e-07','0','0','0','0','0','-0.000973704','0.254578','8.04354e-06','2.98026e-06','0','0','0','0','0','-3.02339e-06','8.04354e-06','5.94877e-08','6.18388e-10','0','0','0','0','0','1.11023e-07','2.98026e-06','6.18388e-10','0.000176053','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021968, ("CSC", 1, 2, 2, 26), "MEp22_26"))
reports[-1].posNum = 1474
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00297257, 0.0238662, 0), \
                           ValErr(-0.0466041, 0.568695, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000106553, 0.000244232, 0), \
                           -1764.97, 1474, 1474, -nan)
reports[-1].sigmaresid = ValErr(0.801287, 0.0147579, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0285876, None, -0.000275979, None, 0.00205287, None, -0.000367609, None, 0.00205287, None, -0.000367609, None, -0.00584026, None, -0.000401683, None, -0.00584026, None, -0.000401683, None, 0.801337, None, 0.00944721, None, 0.801337, None, 0.00944721, None)
reports[-1].CovMatrix = ['0.000569596','-8.06653e-06','-2.82063e-06','7.30104e-08','0','0','0','0','0','-8.06653e-06','0.323414','-9.32476e-06','3.67335e-06','0','0','0','0','0','-2.82063e-06','-9.32476e-06','5.96491e-08','1.49069e-09','0','0','0','0','0','7.30104e-08','3.67335e-06','1.49069e-09','0.000217796','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021984, ("CSC", 1, 2, 2, 28), "MEp22_28"))
reports[-1].posNum = 2166
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0114344, 0.0212438, 0), \
                           ValErr(-0.191228, 0.531959, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.3549e-06, 0.00023002, 0), \
                           -2877.9, 2166, 2166, -nan)
reports[-1].sigmaresid = ValErr(0.913688, 0.0138821, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0123192, None, -0.00165902, None, 0.0112032, None, -0.00160648, None, 0.0112032, None, -0.00160648, None, 0.00981089, None, -0.00184269, None, 0.00981089, None, -0.00184269, None, 0.913712, None, 0.0094503, None, 0.913712, None, 0.0094503, None)
reports[-1].CovMatrix = ['0.0004513','-5.36393e-06','-1.86681e-06','1.14569e-07','0','0','0','0','0','-5.36393e-06','0.28298','-1.31624e-06','4.56667e-06','0','0','0','0','0','-1.86681e-06','-1.31624e-06','5.29094e-08','1.16039e-09','0','0','0','0','0','1.14569e-07','4.56667e-06','1.16039e-09','0.000192714','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604022000, ("CSC", 1, 2, 2, 30), "MEp22_30"))
reports[-1].posNum = 1349
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00590624, 0.0250667, 0), \
                           ValErr(0.112754, 0.580447, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.46987e-05, 0.000246056, 0), \
                           -1669.45, 1349, 1349, -nan)
reports[-1].sigmaresid = ValErr(0.834102, 0.0160581, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00867354, None, -0.00125184, None, 0.00159279, None, -0.000487503, None, 0.00159279, None, -0.000487503, None, -0.0234489, None, -0.000864768, None, -0.0234489, None, -0.000864768, None, 0.834164, None, 0.0132209, None, 0.834164, None, 0.0132209, None)
reports[-1].CovMatrix = ['0.000628342','0.000836965','-2.59001e-06','1.57072e-07','0','0','0','0','0','0.000836965','0.336918','-1.32236e-06','4.89463e-06','0','0','0','0','0','-2.59001e-06','-1.32236e-06','6.05436e-08','1.30817e-09','0','0','0','0','0','1.57072e-07','4.89463e-06','1.30817e-09','0.000257864','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604022016, ("CSC", 1, 2, 2, 32), "MEp22_32"))
reports[-1].posNum = 1767
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00202816, 0.0231531, 0), \
                           ValErr(0.0413846, 0.554619, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000239149, 0.000240702, 0), \
                           -2278.04, 1767, 1767, -nan)
reports[-1].sigmaresid = ValErr(0.878306, 0.0147738, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00142461, None, -0.00211136, None, -0.00795643, None, -0.00146939, None, -0.00795643, None, -0.00146939, None, -0.0025719, None, -0.00147977, None, -0.0025719, None, -0.00147977, None, 0.878586, None, 0.0127819, None, 0.878586, None, 0.0127819, None)
reports[-1].CovMatrix = ['0.000536066','-4.68067e-05','-2.39695e-06','1.29642e-07','0','0','0','0','0','-4.68067e-05','0.307602','8.81772e-06','4.76314e-06','0','0','0','0','0','-2.39695e-06','8.81772e-06','5.79377e-08','1.23551e-09','0','0','0','0','0','1.29642e-07','4.76314e-06','1.23551e-09','0.000218267','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604022032, ("CSC", 1, 2, 2, 34), "MEp22_34"))
reports[-1].posNum = 1759
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0109213, 0.0230957, 0), \
                           ValErr(-0.109275, 0.565509, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.29123e-05, 0.000246232, 0), \
                           -2319.01, 1759, 1759, -nan)
reports[-1].sigmaresid = ValErr(0.904309, 0.0152461, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00952518, None, -0.000251889, None, 0.00871771, None, -0.000280274, None, 0.00871771, None, -0.000280274, None, 0.020572, None, -0.00023663, None, 0.020572, None, -0.00023663, None, 0.904348, None, 0.0113554, None, 0.904348, None, 0.0113554, None)
reports[-1].CovMatrix = ['0.000533411','-0.000393455','-2.03407e-06','1.30991e-07','0','0','0','0','0','-0.000393455','0.319801','3.10687e-06','5.06084e-06','0','0','0','0','0','-2.03407e-06','3.10687e-06','6.06302e-08','1.4051e-09','0','0','0','0','0','1.30991e-07','5.06084e-06','1.4051e-09','0.000232446','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604022048, ("CSC", 1, 2, 2, 36), "MEp22_36"))
reports[-1].posNum = 1367
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.016869, 0.0267609, 0), \
                           ValErr(-0.0981201, 0.629363, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.46045e-05, 0.000291757, 0), \
                           -1810.27, 1367, 1367, -nan)
reports[-1].sigmaresid = ValErr(0.909627, 0.0173955, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0191354, None, 0.000118797, None, -0.0158343, None, 0.000206174, None, -0.0158343, None, 0.000206174, None, -0.0247425, None, 5.13891e-05, None, -0.0247425, None, 5.13891e-05, None, 0.909678, None, 0.00975686, None, 0.909678, None, 0.00975686, None)
reports[-1].CovMatrix = ['0.000716144','0.000472003','-3.05875e-06','1.7314e-07','0','0','0','0','0','0.000472003','0.396098','3.92792e-06','7.19853e-06','0','0','0','0','0','-3.05875e-06','3.92792e-06','8.51221e-08','2.23586e-09','0','0','0','0','0','1.7314e-07','7.19853e-06','2.23586e-09','0.000302607','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025352, ("CSC", 1, 3, 1, 1), "MEp31_01"))
reports[-1].posNum = 4823
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00014913, 0.00638974, 0), \
                           ValErr(0.0419418, 0.0727733, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.23974e-06, 0.000149519, 0), \
                           -2913.01, 4823, 4823, -nan)
reports[-1].sigmaresid = ValErr(0.442659, 0.00450707, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-5.22539e-05, None, -0.00184223, None, 0.000123032, None, -0.00168246, None, 0.000123032, None, -0.00168246, None, 0.0039464, None, -0.00174074, None, 0.0039464, None, -0.00174074, None, 0.442674, None, 0.0114275, None, 0.442674, None, 0.0114275, None)
reports[-1].CovMatrix = ['4.08287e-05','2.11596e-06','-6.69708e-08','1.01826e-08','0','0','0','0','0','2.11596e-06','0.00529595','-1.18999e-07','1.23002e-07','0','0','0','0','0','-6.69708e-08','-1.18999e-07','2.2356e-08','2.35901e-10','0','0','0','0','0','1.01826e-08','1.23002e-07','2.35901e-10','2.03137e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025368, ("CSC", 1, 3, 1, 3), "MEp31_03"))
reports[-1].posNum = 4769
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00151062, 0.00646553, 0), \
                           ValErr(0.0415695, 0.0736518, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.52546e-05, 0.00014862, 0), \
                           -2913.35, 4769, 4769, -nan)
reports[-1].sigmaresid = ValErr(0.445728, 0.00456394, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00574524, None, -0.000952093, None, -0.00133327, None, -0.000942527, None, -0.00133327, None, -0.000942527, None, 0.00764171, None, -0.000934853, None, 0.00764171, None, -0.000934853, None, 0.445749, None, 0.0125838, None, 0.445749, None, 0.0125838, None)
reports[-1].CovMatrix = ['4.18031e-05','-5.30428e-06','-5.5434e-08','1.04793e-08','0','0','0','0','0','-5.30428e-06','0.00542458','1.05293e-07','1.27054e-07','0','0','0','0','0','-5.5434e-08','1.05293e-07','2.20879e-08','2.44578e-10','0','0','0','0','0','1.04793e-08','1.27054e-07','2.44578e-10','2.08296e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025384, ("CSC", 1, 3, 1, 5), "MEp31_05"))
reports[-1].posNum = 4655
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00120769, 0.00653634, 0), \
                           ValErr(-0.0147131, 0.0744398, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.20024e-05, 0.000151365, 0), \
                           -2837.13, 4655, 4655, -nan)
reports[-1].sigmaresid = ValErr(0.445098, 0.00461297, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000196938, None, -1.04607e-05, None, -0.0011683, None, 0.000462291, None, -0.0011683, None, 0.000462291, None, -0.00389167, None, 6.80106e-05, None, -0.00389167, None, 6.80106e-05, None, 0.445104, None, 0.0122755, None, 0.445104, None, 0.0122755, None)
reports[-1].CovMatrix = ['4.27238e-05','-1.86591e-05','-4.8976e-08','1.05766e-08','0','0','0','0','0','-1.86591e-05','0.00554128','2.00586e-07','1.28577e-07','0','0','0','0','0','-4.8976e-08','2.00586e-07','2.29114e-08','2.56472e-10','0','0','0','0','0','1.05766e-08','1.28577e-07','2.56472e-10','2.12795e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025400, ("CSC", 1, 3, 1, 7), "MEp31_07"))
reports[-1].posNum = 4843
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00133415, 0.00644611, 0), \
                           ValErr(0.0656043, 0.0740587, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.80131e-05, 0.000148837, 0), \
                           -2976.95, 4843, 4843, -nan)
reports[-1].sigmaresid = ValErr(0.447424, 0.00454618, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000409823, None, -0.00247256, None, -0.000975591, None, -0.0022966, None, -0.000975591, None, -0.0022966, None, 0.00132769, None, -0.00253569, None, 0.00132769, None, -0.00253569, None, 0.447477, None, 0.0124463, None, 0.447477, None, 0.0124463, None)
reports[-1].CovMatrix = ['4.15523e-05','-6.95932e-06','-6.76412e-08','1.03238e-08','0','0','0','0','0','-6.95932e-06','0.00548469','-1.5846e-07','1.24601e-07','0','0','0','0','0','-6.76412e-08','-1.5846e-07','2.21525e-08','2.28463e-10','0','0','0','0','0','1.03238e-08','1.24601e-07','2.28463e-10','2.06678e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025416, ("CSC", 1, 3, 1, 9), "MEp31_09"))
reports[-1].posNum = 4670
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0026353, 0.00648823, 0), \
                           ValErr(-0.0152273, 0.0747661, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.57286e-05, 0.000147696, 0), \
                           -2823.04, 4670, 4670, -nan)
reports[-1].sigmaresid = ValErr(0.44289, 0.0045827, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00183666, None, -0.00209143, None, -0.00245745, None, -0.00199102, None, -0.00245745, None, -0.00199102, None, -0.000275997, None, -0.00184433, None, -0.000275997, None, -0.00184433, None, 0.442912, None, 0.0116052, None, 0.442912, None, 0.0116052, None)
reports[-1].CovMatrix = ['4.20971e-05','-5.80085e-06','-4.41017e-08','1.06482e-08','0','0','0','0','0','-5.80085e-06','0.00558997','1.05527e-07','1.29973e-07','0','0','0','0','0','-4.41017e-08','1.05527e-07','2.18142e-08','2.4483e-10','0','0','0','0','0','1.06482e-08','1.29973e-07','2.4483e-10','2.10011e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025432, ("CSC", 1, 3, 1, 11), "MEp31_11"))
reports[-1].posNum = 5029
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00076083, 0.00638494, 0), \
                           ValErr(-0.0295167, 0.0735795, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.4103e-05, 0.000146767, 0), \
                           -3133.57, 5029, 5029, -nan)
reports[-1].sigmaresid = ValErr(0.451203, 0.00449899, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00791553, None, -0.0013302, None, -0.000571228, None, -0.00116688, None, -0.000571228, None, -0.00116688, None, -0.00392952, None, -0.00109372, None, -0.00392952, None, -0.00109372, None, 0.451213, None, 0.0113257, None, 0.451213, None, 0.0113257, None)
reports[-1].CovMatrix = ['4.07675e-05','1.35671e-05','-7.38183e-08','1.04963e-08','0','0','0','0','0','1.35671e-05','0.00541394','-8.87794e-08','1.31379e-07','0','0','0','0','0','-7.38183e-08','-8.87794e-08','2.15406e-08','2.30008e-10','0','0','0','0','0','1.04963e-08','1.31379e-07','2.30008e-10','2.0241e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025448, ("CSC", 1, 3, 1, 13), "MEp31_13"))
reports[-1].posNum = 5157
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0038284, 0.00627177, 0), \
                           ValErr(-0.0189659, 0.0737217, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.9041e-05, 0.000145266, 0), \
                           -3174.52, 5157, 5157, -nan)
reports[-1].sigmaresid = ValErr(0.447821, 0.00440952, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00201036, None, -0.000451393, None, 0.00384754, None, -0.000205881, None, 0.00384754, None, -0.000205881, None, 0.0072508, None, -0.000162222, None, 0.0072508, None, -0.000162222, None, 0.447825, None, 0.0122144, None, 0.447825, None, 0.0122144, None)
reports[-1].CovMatrix = ['3.93351e-05','-2.94161e-05','-8.06326e-08','8.34983e-09','0','0','0','0','0','-2.94161e-05','0.00543489','5.01347e-07','1.25093e-07','0','0','0','0','0','-8.06326e-08','5.01347e-07','2.11023e-08','2.33883e-10','0','0','0','0','0','8.34983e-09','1.25093e-07','2.33883e-10','1.94439e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025464, ("CSC", 1, 3, 1, 15), "MEp31_15"))
reports[-1].posNum = 3417
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00451782, 0.00775802, 0), \
                           ValErr(-0.00940029, 0.0843231, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000101142, 0.000173866, 0), \
                           -2101.92, 3417, 3417, -nan)
reports[-1].sigmaresid = ValErr(0.447624, 0.00541472, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0107271, None, 0.0023442, None, 0.00488233, None, 0.00264978, None, 0.00488233, None, 0.00264978, None, 0.00472749, None, 0.00296024, None, 0.00472749, None, 0.00296024, None, 0.447646, None, 0.013974, None, 0.447646, None, 0.013974, None)
reports[-1].CovMatrix = ['6.01869e-05','0.000100029','-6.53217e-08','1.62086e-08','0','0','0','0','0','0.000100029','0.00711039','2.52708e-09','2.02909e-07','0','0','0','0','0','-6.53217e-08','2.52708e-09','3.02293e-08','3.4254e-10','0','0','0','0','0','1.62086e-08','2.02909e-07','3.4254e-10','2.93193e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025480, ("CSC", 1, 3, 1, 17), "MEp31_17"))
reports[-1].posNum = 4831
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000497743, 0.00642938, 0), \
                           ValErr(-0.00737037, 0.0736737, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000108215, 0.000148182, 0), \
                           -2958.28, 4831, 4831, -nan)
reports[-1].sigmaresid = ValErr(0.446379, 0.00454119, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00663094, None, -0.000991392, None, -0.000716682, None, -0.000556198, None, -0.000716682, None, -0.000556198, None, -0.000592096, None, -0.000866282, None, -0.000592096, None, -0.000866282, None, 0.446405, None, 0.0119519, None, 0.446405, None, 0.0119519, None)
reports[-1].CovMatrix = ['4.13369e-05','-7.19268e-06','-4.2558e-08','1.04482e-08','0','0','0','0','0','-7.19268e-06','0.00542782','1.28704e-08','1.26608e-07','0','0','0','0','0','-4.2558e-08','1.28704e-08','2.1958e-08','2.49026e-10','0','0','0','0','0','1.04482e-08','1.26608e-07','2.49026e-10','2.06224e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025360, ("CSC", 1, 3, 1, 2), "MEp31_02"))
reports[-1].posNum = 4781
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000933238, 0.0067273, 0), \
                           ValErr(-0.0244111, 0.0777092, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.27502e-05, 0.000157869, 0), \
                           -3113.19, 4781, 4781, -nan)
reports[-1].sigmaresid = ValErr(0.464043, 0.00474551, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00345327, None, -0.00137039, None, 0.000824542, None, -0.00140093, None, 0.000824542, None, -0.00140093, None, -0.00110996, None, -0.0015423, None, -0.00110996, None, -0.0015423, None, 0.464049, None, 0.0088697, None, 0.464049, None, 0.0088697, None)
reports[-1].CovMatrix = ['4.52565e-05','-3.58815e-06','-7.32148e-08','1.16586e-08','0','0','0','0','0','-3.58815e-06','0.00603871','1.7051e-07','1.46588e-07','0','0','0','0','0','-7.32148e-08','1.7051e-07','2.49226e-08','2.79783e-10','0','0','0','0','0','1.16586e-08','1.46588e-07','2.79783e-10','2.25199e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025376, ("CSC", 1, 3, 1, 4), "MEp31_04"))
reports[-1].posNum = 4828
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00449434, 0.00694587, 0), \
                           ValErr(0.000718825, 0.0805071, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000163983, 0.000163463, 0), \
                           -3300.06, 4828, 4828, -nan)
reports[-1].sigmaresid = ValErr(0.479308, 0.00487772, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00176989, None, -0.00153155, None, 0.00368568, None, -0.0013408, None, 0.00368568, None, -0.0013408, None, -0.000138694, None, -0.00147405, None, -0.000138694, None, -0.00147405, None, 0.479357, None, 0.0109082, None, 0.479357, None, 0.0109082, None)
reports[-1].CovMatrix = ['4.82451e-05','-6.81007e-06','-1.32164e-07','1.18483e-08','0','0','0','0','0','-6.81007e-06','0.0064814','-4.85744e-09','1.56272e-07','0','0','0','0','0','-1.32164e-07','-4.85744e-09','2.672e-08','2.82408e-10','0','0','0','0','0','1.18483e-08','1.56272e-07','2.82408e-10','2.37922e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025392, ("CSC", 1, 3, 1, 6), "MEp31_06"))
reports[-1].posNum = 4675
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00132405, 0.00674224, 0), \
                           ValErr(-0.0335416, 0.0796845, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.04748e-05, 0.000157528, 0), \
                           -2929.22, 4675, 4675, -nan)
reports[-1].sigmaresid = ValErr(0.452774, 0.0046825, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00424682, None, -0.00179379, None, -0.000657294, None, -0.00179073, None, -0.000657294, None, -0.00179073, None, -0.00321227, None, -0.00181164, None, -0.00321227, None, -0.00181164, None, 0.452786, None, 0.0100653, None, 0.452786, None, 0.0100653, None)
reports[-1].CovMatrix = ['4.54578e-05','6.34101e-05','-1.69022e-07','1.21306e-08','0','0','0','0','0','6.34101e-05','0.00634962','-1.46944e-06','1.55114e-07','0','0','0','0','0','-1.69022e-07','-1.46944e-06','2.48152e-08','1.9567e-10','0','0','0','0','0','1.21306e-08','1.55114e-07','1.9567e-10','2.19259e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025408, ("CSC", 1, 3, 1, 8), "MEp31_08"))
reports[-1].posNum = 4713
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00378198, 0.00668784, 0), \
                           ValErr(-0.00763376, 0.0774027, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000122679, 0.000154242, 0), \
                           -3005.42, 4713, 4713, -nan)
reports[-1].sigmaresid = ValErr(0.457832, 0.00471566, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00761192, None, -0.00262687, None, -0.0041518, None, -0.00249667, None, -0.0041518, None, -0.00249667, None, 0.00239968, None, -0.00234832, None, 0.00239968, None, -0.00234832, None, 0.457864, None, 0.0101807, None, 0.457864, None, 0.0101807, None)
reports[-1].CovMatrix = ['4.47272e-05','1.07267e-05','-7.45421e-08','1.16201e-08','0','0','0','0','0','1.07267e-05','0.00599118','-5.17909e-08','1.43946e-07','0','0','0','0','0','-7.45421e-08','-5.17909e-08','2.37906e-08','2.6509e-10','0','0','0','0','0','1.16201e-08','1.43946e-07','2.6509e-10','2.22374e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025424, ("CSC", 1, 3, 1, 10), "MEp31_10"))
reports[-1].posNum = 4738
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00128791, 0.00653478, 0), \
                           ValErr(0.00389279, 0.0750753, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.23351e-05, 0.000154381, 0), \
                           -2910.89, 4738, 4738, -nan)
reports[-1].sigmaresid = ValErr(0.447281, 0.0045948, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00927654, None, 6.49477e-05, None, 0.0014779, None, -1.01851e-06, None, 0.0014779, None, -1.01851e-06, None, 0.0081094, None, 2.55844e-05, None, 0.0081094, None, 2.55844e-05, None, 0.447285, None, 0.0104382, None, 0.447285, None, 0.0104382, None)
reports[-1].CovMatrix = ['4.27033e-05','-9.99297e-07','-1.06785e-07','1.03779e-08','0','0','0','0','0','-9.99297e-07','0.0056363','-6.7184e-08','1.3101e-07','0','0','0','0','0','-1.06785e-07','-6.7184e-08','2.38334e-08','2.39354e-10','0','0','0','0','0','1.03779e-08','1.3101e-07','2.39354e-10','2.11122e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025440, ("CSC", 1, 3, 1, 12), "MEp31_12"))
reports[-1].posNum = 4731
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00204519, 0.00656756, 0), \
                           ValErr(-0.0676547, 0.0757091, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000166278, 0.000151976, 0), \
                           -2902.7, 4731, 4731, -nan)
reports[-1].sigmaresid = ValErr(0.446915, 0.00459447, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00388695, None, 0.00154204, None, -0.00107037, None, 0.00166252, None, -0.00107037, None, 0.00166252, None, 0.00899182, None, 0.00166134, None, 0.00899182, None, 0.00166134, None, 0.447008, None, 0.0109363, None, 0.447008, None, 0.0109363, None)
reports[-1].CovMatrix = ['4.31328e-05','-6.01848e-06','-1.44806e-07','9.35656e-09','0','0','0','0','0','-6.01848e-06','0.00573187','-4.80329e-08','1.32345e-07','0','0','0','0','0','-1.44806e-07','-4.80329e-08','2.30967e-08','2.06354e-10','0','0','0','0','0','9.35656e-09','1.32345e-07','2.06354e-10','2.11092e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025456, ("CSC", 1, 3, 1, 14), "MEp31_14"))
reports[-1].posNum = 4731
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00371046, 0.00679866, 0), \
                           ValErr(-0.0692232, 0.0783142, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000193676, 0.000158722, 0), \
                           -3088.76, 4731, 4731, -nan)
reports[-1].sigmaresid = ValErr(0.464841, 0.00477873, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00735754, None, 0.00047619, None, -0.00280757, None, 0.000495308, None, -0.00280757, None, 0.000495308, None, -0.000697106, None, 0.000396063, None, -0.000697106, None, 0.000396063, None, 0.464952, None, 0.0104687, None, 0.464952, None, 0.0104687, None)
reports[-1].CovMatrix = ['4.62218e-05','-1.87335e-07','-1.17626e-07','1.13612e-08','0','0','0','0','0','-1.87335e-07','0.00613311','-1.34078e-08','1.48345e-07','0','0','0','0','0','-1.17626e-07','-1.34078e-08','2.51927e-08','2.63362e-10','0','0','0','0','0','1.13612e-08','1.48345e-07','2.63362e-10','2.28363e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025472, ("CSC", 1, 3, 1, 16), "MEp31_16"))
reports[-1].posNum = 4810
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000205845, 0.00662565, 0), \
                           ValErr(-0.00480517, 0.0764297, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.03648e-06, 0.000155382, 0), \
                           -3059.06, 4810, 4810, -nan)
reports[-1].sigmaresid = ValErr(0.457049, 0.00465986, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00166613, None, 0.00223951, None, -0.000210167, None, 0.00250739, None, -0.000210167, None, 0.00250739, None, -0.0073922, None, 0.00236277, None, -0.0073922, None, 0.00236277, None, 0.457051, None, 0.0103042, None, 0.457051, None, 0.0103042, None)
reports[-1].CovMatrix = ['4.38993e-05','8.2191e-06','-1.05553e-07','1.11672e-08','0','0','0','0','0','8.2191e-06','0.0058415','-2.47184e-07','1.372e-07','0','0','0','0','0','-1.05553e-07','-2.47184e-07','2.41437e-08','2.38562e-10','0','0','0','0','0','1.11672e-08','1.372e-07','2.38562e-10','2.17143e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025488, ("CSC", 1, 3, 1, 18), "MEp31_18"))
reports[-1].posNum = 4774
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000319681, 0.00681463, 0), \
                           ValErr(0.00972347, 0.078512, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.52927e-05, 0.000157454, 0), \
                           -3163.79, 4774, 4774, -nan)
reports[-1].sigmaresid = ValErr(0.469435, 0.00480418, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00162175, None, 6.5977e-06, None, -0.000562553, None, 0.000239277, None, -0.000562553, None, 0.000239277, None, 0.00232125, None, -6.51721e-05, None, 0.00232125, None, -6.51721e-05, None, 0.469447, None, 0.0103145, None, 0.469447, None, 0.0103145, None)
reports[-1].CovMatrix = ['4.64392e-05','2.44905e-05','-6.70623e-08','1.28664e-08','0','0','0','0','0','2.44905e-05','0.00616413','5.84632e-09','1.56233e-07','0','0','0','0','0','-6.70623e-08','5.84632e-09','2.47918e-08','2.8461e-10','0','0','0','0','0','1.28664e-08','1.56233e-07','2.8461e-10','2.30802e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025864, ("CSC", 1, 3, 2, 1), "MEp32_01"))
reports[-1].posNum = 1959
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00594829, 0.0227039, 0), \
                           ValErr(-0.370507, 0.546443, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.771e-05, 0.000249649, 0), \
                           -2552.32, 1959, 1959, -nan)
reports[-1].sigmaresid = ValErr(0.890398, 0.0142246, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00832076, None, 0.00104986, None, -0.00691544, None, 0.00111305, None, -0.00691544, None, 0.00111305, None, 0.0343592, None, 0.000896095, None, 0.0343592, None, 0.000896095, None, 0.890519, None, 0.0112888, None, 0.890519, None, 0.0112888, None)
reports[-1].CovMatrix = ['0.000515469','-0.000186728','-2.62599e-06','8.58613e-08','0','0','0','0','0','-0.000186728','0.298599','-1.24271e-07','4.37532e-06','0','0','0','0','0','-2.62599e-06','-1.24271e-07','6.23244e-08','1.49241e-09','0','0','0','0','0','8.58613e-08','4.37532e-06','1.49241e-09','0.000202342','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025880, ("CSC", 1, 3, 2, 3), "MEp32_03"))
reports[-1].posNum = 1564
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-1.05833e-05, 0.0280355, 0), \
                           ValErr(0.0830846, 0.561159, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.421e-05, 0.000298468, 0), \
                           -1845.94, 1564, 1564, -nan)
reports[-1].sigmaresid = ValErr(0.78767, 0.0140833, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0217134, None, 0.000954536, None, 0.00155756, None, 0.00116055, None, 0.00155756, None, 0.00116055, None, -0.036255, None, 0.00116633, None, -0.036255, None, 0.00116633, None, 0.787683, None, 0.011205, None, 0.787683, None, 0.011205, None)
reports[-1].CovMatrix = ['0.000785988','0.000436535','-5.88873e-06','1.15268e-07','0','0','0','0','0','0.000436535','0.3149','-5.15857e-06','3.37802e-06','0','0','0','0','0','-5.88873e-06','-5.15857e-06','8.90829e-08','5.7173e-10','0','0','0','0','0','1.15268e-07','3.37802e-06','5.7173e-10','0.000198342','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025896, ("CSC", 1, 3, 2, 5), "MEp32_05"))
reports[-1].posNum = 1664
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.012166, 0.0261792, 0), \
                           ValErr(0.236139, 0.599318, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.41356e-05, 0.000284324, 0), \
                           -2148.34, 1664, 1664, -nan)
reports[-1].sigmaresid = ValErr(0.879966, 0.0152535, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00542007, None, -0.000847315, None, -0.00833687, None, 0.000101305, None, -0.00833687, None, 0.000101305, None, -0.0326649, None, -0.000333781, None, -0.0326649, None, -0.000333781, None, 0.880023, None, 0.0132569, None, 0.880023, None, 0.0132569, None)
reports[-1].CovMatrix = ['0.00068535','-0.00117289','-4.20037e-06','1.10927e-07','0','0','0','0','0','-0.00117289','0.359182','7.311e-06','4.89489e-06','0','0','0','0','0','-4.20037e-06','7.311e-06','8.08401e-08','1.30377e-09','0','0','0','0','0','1.10927e-07','4.89489e-06','1.30377e-09','0.000232672','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025912, ("CSC", 1, 3, 2, 7), "MEp32_07"))
reports[-1].posNum = 1915
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0283455, 0.0230349, 0), \
                           ValErr(0.0219254, 0.539126, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000264846, 0.000250428, 0), \
                           -2493.64, 1915, 1915, -nan)
reports[-1].sigmaresid = ValErr(0.889777, 0.0143772, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0303095, None, -0.000739758, None, -0.0169029, None, 0.00014638, None, -0.0169029, None, 0.00014638, None, -0.0555006, None, -0.000215429, None, -0.0555006, None, -0.000215429, None, 0.890045, None, 0.011798, None, 0.890045, None, 0.011798, None)
reports[-1].CovMatrix = ['0.000530607','-0.000347679','-2.70736e-06','1.0542e-07','0','0','0','0','0','-0.000347679','0.290657','1.11132e-06','4.27542e-06','0','0','0','0','0','-2.70736e-06','1.11132e-06','6.27144e-08','1.31799e-09','0','0','0','0','0','1.0542e-07','4.27542e-06','1.31799e-09','0.000206706','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025928, ("CSC", 1, 3, 2, 9), "MEp32_09"))
reports[-1].posNum = 1856
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00633397, 0.0234356, 0), \
                           ValErr(0.244104, 0.565256, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000128254, 0.0002473, 0), \
                           -2449.03, 1856, 1856, -nan)
reports[-1].sigmaresid = ValErr(0.905366, 0.01486, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0500466, None, -0.00355746, None, 0.00083858, None, -0.00344845, None, 0.00083858, None, -0.00344845, None, -0.0179406, None, -0.0037054, None, -0.0179406, None, -0.0037054, None, 0.905478, None, 0.0116155, None, 0.905478, None, 0.0116155, None)
reports[-1].CovMatrix = ['0.000549227','9.61379e-06','-2.56401e-06','1.13345e-07','0','0','0','0','0','9.61379e-06','0.319514','3.80896e-06','4.0856e-06','0','0','0','0','0','-2.56401e-06','3.80896e-06','6.11575e-08','1.34421e-09','0','0','0','0','0','1.13345e-07','4.0856e-06','1.34421e-09','0.000220822','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025944, ("CSC", 1, 3, 2, 11), "MEp32_11"))
reports[-1].posNum = 1804
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00931871, 0.0245603, 0), \
                           ValErr(0.0606015, 0.56676, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000156691, 0.000269125, 0), \
                           -2318.93, 1804, 1804, -nan)
reports[-1].sigmaresid = ValErr(0.875038, 0.0145679, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0147701, None, 0.00197481, None, 0.0171964, None, 0.00220977, None, 0.0171964, None, 0.00220977, None, 0.0116494, None, 0.00220554, None, 0.0116494, None, 0.00220554, None, 0.875112, None, 0.0103926, None, 0.875112, None, 0.0103926, None)
reports[-1].CovMatrix = ['0.000603209','-0.000533536','-3.59007e-06','8.51094e-08','0','0','0','0','0','-0.000533536','0.321217','4.18646e-07','4.5679e-06','0','0','0','0','0','-3.59007e-06','4.18646e-07','7.24284e-08','1.33223e-09','0','0','0','0','0','8.51094e-08','4.5679e-06','1.33223e-09','0.000212227','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025960, ("CSC", 1, 3, 2, 13), "MEp32_13"))
reports[-1].posNum = 1940
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0139481, 0.0227995, 0), \
                           ValErr(0.382234, 0.569777, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000143741, 0.000245876, 0), \
                           -2546.64, 1940, 1940, -nan)
reports[-1].sigmaresid = ValErr(0.899181, 0.0144348, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0182259, None, -0.00255746, None, -0.00762369, None, -0.00225049, None, -0.00762369, None, -0.00225049, None, 0.0112207, None, -0.00220856, None, 0.0112207, None, -0.00220856, None, 0.89938, None, 0.011539, None, 0.89938, None, 0.011539, None)
reports[-1].CovMatrix = ['0.000519817','-0.000893764','-2.49095e-06','9.25714e-08','0','0','0','0','0','-0.000893764','0.324646','1.28171e-05','3.8278e-06','0','0','0','0','0','-2.49095e-06','1.28171e-05','6.04552e-08','1.63057e-09','0','0','0','0','0','9.25714e-08','3.8278e-06','1.63057e-09','0.000208365','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025976, ("CSC", 1, 3, 2, 15), "MEp32_15"))
reports[-1].posNum = 1978
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0266111, 0.0234055, 0), \
                           ValErr(0.0924569, 0.545988, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.1339e-05, 0.000258429, 0), \
                           -2560.33, 1978, 1978, -nan)
reports[-1].sigmaresid = ValErr(0.88292, 0.0140378, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0331384, None, 0.00151395, None, 0.0230441, None, 0.0018893, None, 0.0230441, None, 0.0018893, None, 0.0554509, None, 0.00183435, None, 0.0554509, None, 0.00183435, None, 0.882932, None, 0.0120638, None, 0.882932, None, 0.0120638, None)
reports[-1].CovMatrix = ['0.000547817','1.18711e-05','-3.19734e-06','1.08368e-07','0','0','0','0','0','1.18711e-05','0.298103','8.83075e-06','3.67893e-06','0','0','0','0','0','-3.19734e-06','8.83075e-06','6.67858e-08','1.09922e-09','0','0','0','0','0','1.08368e-07','3.67893e-06','1.09922e-09','0.000197062','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025992, ("CSC", 1, 3, 2, 17), "MEp32_17"))
reports[-1].posNum = 1904
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.003849, 0.0233571, 0), \
                           ValErr(0.025663, 0.559036, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.09221e-05, 0.000250687, 0), \
                           -2427.77, 1904, 1904, -nan)
reports[-1].sigmaresid = ValErr(0.866042, 0.0140347, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0362813, None, -0.00354458, None, 0.00179385, None, -0.00337027, None, 0.00179385, None, -0.00337027, None, 0.0458107, None, -0.00312282, None, 0.0458107, None, -0.00312282, None, 0.866023, None, 0.0109296, None, 0.866023, None, 0.0109296, None)
reports[-1].CovMatrix = ['0.000545555','0.000442971','-3.08606e-06','1.39302e-07','0','0','0','0','0','0.000442971','0.312521','-5.67168e-06','4.46328e-06','0','0','0','0','0','-3.08606e-06','-5.67168e-06','6.28441e-08','6.52419e-10','0','0','0','0','0','1.39302e-07','4.46328e-06','6.52419e-10','0.000196976','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026008, ("CSC", 1, 3, 2, 19), "MEp32_19"))
reports[-1].posNum = 1894
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00934993, 0.0230668, 0), \
                           ValErr(-0.19569, 0.545129, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.82203e-05, 0.000240923, 0), \
                           -2519.5, 1894, 1894, -nan)
reports[-1].sigmaresid = ValErr(0.915149, 0.0144478, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00600467, None, 0.00110426, None, -0.00687693, None, 0.00146699, None, -0.00687693, None, 0.00146699, None, -0.00624839, None, 0.00146135, None, -0.00624839, None, 0.00146135, None, 0.915194, None, 0.0120433, None, 0.915194, None, 0.0120433, None)
reports[-1].CovMatrix = ['0.000532078','-0.00116655','-2.50647e-06','1.15114e-05','0','0','0','0','0','-0.00116655','0.297166','2.11811e-05','-0.0010119','0','0','0','0','0','-2.50647e-06','2.11811e-05','5.80439e-08','1.68936e-07','0','0','0','0','0','1.15114e-05','-0.0010119','1.68936e-07','0.00020874','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026024, ("CSC", 1, 3, 2, 21), "MEp32_21"))
reports[-1].posNum = 1535
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00573376, 0.0244971, 0), \
                           ValErr(0.249902, 0.59086, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.10885e-05, 0.000259449, 0), \
                           -2013.5, 1535, 1535, -nan)
reports[-1].sigmaresid = ValErr(0.898321, 0.0162125, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0190735, None, 0.000783772, None, 0.00336717, None, 0.00117303, None, 0.00336717, None, 0.00117303, None, 0.00111391, None, 0.00119481, None, 0.00111391, None, 0.00119481, None, 0.898413, None, 0.0121898, None, 0.898413, None, 0.0121898, None)
reports[-1].CovMatrix = ['0.000600106','-0.000163396','-2.22915e-06','1.51399e-07','0','0','0','0','0','-0.000163396','0.349116','-8.47443e-06','4.52969e-06','0','0','0','0','0','-2.22915e-06','-8.47443e-06','6.73139e-08','1.29292e-09','0','0','0','0','0','1.51399e-07','4.52969e-06','1.29292e-09','0.000262848','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026040, ("CSC", 1, 3, 2, 23), "MEp32_23"))
reports[-1].posNum = 2087
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0104661, 0.0211813, 0), \
                           ValErr(0.110689, 0.509409, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000191744, 0.000228265, 0), \
                           -2690.31, 2087, 2087, -nan)
reports[-1].sigmaresid = ValErr(0.878203, 0.0135927, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.014556, None, -0.0028386, None, -0.00316214, None, -0.00251798, None, -0.00316214, None, -0.00251798, None, -0.0149598, None, -0.0027633, None, -0.0149598, None, -0.0027633, None, 0.878381, None, 0.0111764, None, 0.878381, None, 0.0111764, None)
reports[-1].CovMatrix = ['0.000448646','0.000475264','-2.02428e-06','1.011e-07','0','0','0','0','0','0.000475264','0.259498','-3.36604e-06','3.33014e-06','0','0','0','0','0','-2.02428e-06','-3.36604e-06','5.21049e-08','1.04369e-09','0','0','0','0','0','1.011e-07','3.33014e-06','1.04369e-09','0.000184763','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026056, ("CSC", 1, 3, 2, 25), "MEp32_25"))
reports[-1].posNum = 1946
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00280197, 0.0243408, 0), \
                           ValErr(-0.261999, 0.555896, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000119865, 0.000264777, 0), \
                           -2515.55, 1946, 1946, -nan)
reports[-1].sigmaresid = ValErr(0.881379, 0.0141276, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0105242, None, 0.000958664, None, 0.00334915, None, 0.001148, None, 0.00334915, None, 0.001148, None, 0.0127204, None, 0.00100445, None, 0.0127204, None, 0.00100445, None, 0.881488, None, 0.0118104, None, 0.881488, None, 0.0118104, None)
reports[-1].CovMatrix = ['0.000592476','-0.00051924','-3.68035e-06','1.0172e-07','0','0','0','0','0','-0.00051924','0.30902','6.92826e-06','4.33992e-06','0','0','0','0','0','-3.68035e-06','6.92826e-06','7.01067e-08','1.0328e-09','0','0','0','0','0','1.0172e-07','4.33992e-06','1.0328e-09','0.000199592','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026072, ("CSC", 1, 3, 2, 27), "MEp32_27"))
reports[-1].posNum = 1724
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0183883, 0.0245805, 0), \
                           ValErr(-0.113662, 0.46073, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000100174, 0.000257321, 0), \
                           -2271.66, 1724, 1724, -nan)
reports[-1].sigmaresid = ValErr(0.903704, 0.0150865, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0110724, None, -0.00474548, None, -0.0140464, None, -0.00528228, None, -0.0140464, None, -0.00528228, None, -0.0190282, None, -0.00552459, None, -0.0190282, None, -0.00552459, None, 0.903742, None, 0.0112278, None, 0.903742, None, 0.0112278, None)
reports[-1].CovMatrix = ['0.000604203','0.000334003','-3.38232e-06','1.76275e-05','0','0','0','0','0','0.000334003','0.212272','1.70398e-05','-0.00118235','0','0','0','0','0','-3.38232e-06','1.70398e-05','6.62139e-08','8.11347e-08','0','0','0','0','0','1.76275e-05','-0.00118235','8.11347e-08','0.000227606','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026088, ("CSC", 1, 3, 2, 29), "MEp32_29"))
reports[-1].posNum = 1493
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00113402, 0.0256817, 0), \
                           ValErr(-0.115666, 0.594292, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00016204, 0.000265507, 0), \
                           -1896.98, 1493, 1493, -nan)
reports[-1].sigmaresid = ValErr(0.862101, 0.015776, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0446824, None, -0.00448581, None, 0.00531807, None, -0.00448711, None, 0.00531807, None, -0.00448711, None, 0.0045872, None, -0.00449664, None, 0.0045872, None, -0.00449664, None, 0.862244, None, 0.0123393, None, 0.862244, None, 0.0123393, None)
reports[-1].CovMatrix = ['0.000659551','-0.0027742','-3.17886e-06','3.48493e-08','0','0','0','0','0','-0.0027742','0.353183','5.01479e-06','5.49708e-06','0','0','0','0','0','-3.17886e-06','5.01479e-06','7.04938e-08','1.84789e-09','0','0','0','0','0','3.48493e-08','5.49708e-06','1.84789e-09','0.000248884','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026104, ("CSC", 1, 3, 2, 31), "MEp32_31"))
reports[-1].posNum = 1769
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00189227, 0.0244089, 0), \
                           ValErr(-0.1308, 0.614895, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.59369e-05, 0.000258526, 0), \
                           -2384.47, 1769, 1769, -nan)
reports[-1].sigmaresid = ValErr(0.931459, 0.01566, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00293557, None, -0.00159366, None, -0.00249489, None, -0.00124181, None, -0.00249489, None, -0.00124181, None, -0.0608694, None, -0.00146278, None, -0.0608694, None, -0.00146278, None, 0.93146, None, 0.0124758, None, 0.93146, None, 0.0124758, None)
reports[-1].CovMatrix = ['0.000595793','0.00117845','-2.61133e-06','1.4658e-07','0','0','0','0','0','0.00117845','0.378096','-1.5306e-06','4.66683e-06','0','0','0','0','0','-2.61133e-06','-1.5306e-06','6.68354e-08','1.33797e-09','0','0','0','0','0','1.4658e-07','4.66683e-06','1.33797e-09','0.000245237','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026120, ("CSC", 1, 3, 2, 33), "MEp32_33"))
reports[-1].posNum = 2053
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0180666, 0.0227307, 0), \
                           ValErr(0.103848, 0.331665, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.86238e-05, 0.000247298, 0), \
                           -2717.6, 2053, 2053, -nan)
reports[-1].sigmaresid = ValErr(0.909182, 0.0141013, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000210439, None, -0.00260576, None, 0.0154745, None, -0.00228042, None, 0.0154745, None, -0.00228042, None, 0.00999654, None, -0.00233658, None, 0.00999654, None, -0.00233658, None, 0.909198, None, 0.0135981, None, 0.909198, None, 0.0135981, None)
reports[-1].CovMatrix = ['0.000516686','0.00101127','-2.69702e-06','-4.31325e-06','0','0','0','0','0','0.00101127','0.110002','-2.37801e-06','0.000669669','0','0','0','0','0','-2.69702e-06','-2.37801e-06','6.11561e-08','1.19784e-08','0','0','0','0','0','-4.31325e-06','0.000669669','1.19784e-08','0.000198849','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026136, ("CSC", 1, 3, 2, 35), "MEp32_35"))
reports[-1].posNum = 1544
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00460425, 0.0262316, 0), \
                           ValErr(-0.512504, 0.593147, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.63986e-05, 0.000269849, 0), \
                           -1929.51, 1544, 1544, -nan)
reports[-1].sigmaresid = ValErr(0.844283, 0.0151928, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0268769, None, -0.00487318, None, -0.000687242, None, -0.00483998, None, -0.000687242, None, -0.00483998, None, 0.012066, None, -0.00531134, None, 0.012066, None, -0.00531134, None, 0.844509, None, 0.0110589, None, 0.844509, None, 0.0110589, None)
reports[-1].CovMatrix = ['0.000688099','0.000867929','-4.05267e-06','1.67294e-07','0','0','0','0','0','0.000867929','0.351824','-5.58779e-06','5.45689e-06','0','0','0','0','0','-4.05267e-06','-5.58779e-06','7.28185e-08','6.184e-10','0','0','0','0','0','1.67294e-07','5.45689e-06','6.184e-10','0.000230825','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025872, ("CSC", 1, 3, 2, 2), "MEp32_02"))
reports[-1].posNum = 1910
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0088077, 0.0237482, 0), \
                           ValErr(-0.0458946, 0.546496, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00021843, 0.000263013, 0), \
                           -2452.69, 1910, 1910, -nan)
reports[-1].sigmaresid = ValErr(0.873865, 0.0141383, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0305499, None, -0.00245429, None, -0.00179582, None, -0.00256541, None, -0.00179582, None, -0.00256541, None, 0.0195521, None, -0.0024002, None, 0.0195521, None, -0.0024002, None, 0.874045, None, 0.0100265, None, 0.874045, None, 0.0100265, None)
reports[-1].CovMatrix = ['0.000563977','0.00049615','-3.36763e-06','1.24556e-07','0','0','0','0','0','0.00049615','0.298658','-4.90845e-06','4.81805e-06','0','0','0','0','0','-3.36763e-06','-4.90845e-06','6.9176e-08','9.53446e-10','0','0','0','0','0','1.24556e-07','4.81805e-06','9.53446e-10','0.000199894','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025888, ("CSC", 1, 3, 2, 4), "MEp32_04"))
reports[-1].posNum = 1776
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0255338, 0.0278356, 0), \
                           ValErr(0.160342, 0.577111, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000421574, 0.000310127, 0), \
                           -2271.79, 1776, 1776, -nan)
reports[-1].sigmaresid = ValErr(0.869554, 0.0145901, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0169794, None, 0.000614897, None, 0.00041991, None, 0.000616019, None, 0.00041991, None, 0.000616019, None, -0.00692734, None, 0.00084683, None, -0.00692734, None, 0.00084683, None, 0.870029, None, 0.0116859, None, 0.870029, None, 0.0116859, None)
reports[-1].CovMatrix = ['0.000774821','-0.000696369','-5.7883e-06','9.02973e-08','0','0','0','0','0','-0.000696369','0.333057','3.43714e-06','4.50552e-06','0','0','0','0','0','-5.7883e-06','3.43714e-06','9.61787e-08','1.15458e-09','0','0','0','0','0','9.02973e-08','4.50552e-06','1.15458e-09','0.000212873','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025904, ("CSC", 1, 3, 2, 6), "MEp32_06"))
reports[-1].posNum = 2025
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000432678, 0.0231643, 0), \
                           ValErr(0.0313807, 0.544291, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.13725e-05, 0.000260928, 0), \
                           -2653.9, 2025, 2025, -nan)
reports[-1].sigmaresid = ValErr(0.897298, 0.0140997, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0254255, None, -0.00480042, None, 0.000147467, None, -0.00461884, None, 0.000147467, None, -0.00461884, None, -0.00417718, None, -0.00463122, None, -0.00417718, None, -0.00463122, None, 0.897297, None, 0.0114852, None, 0.897297, None, 0.0114852, None)
reports[-1].CovMatrix = ['0.000536587','-0.000624296','-3.066e-06','8.14833e-08','0','0','0','0','0','-0.000624296','0.296253','2.30583e-06','4.36192e-06','0','0','0','0','0','-3.066e-06','2.30583e-06','6.80837e-08','1.37685e-09','0','0','0','0','0','8.14833e-08','4.36192e-06','1.37685e-09','0.000198802','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025920, ("CSC", 1, 3, 2, 8), "MEp32_08"))
reports[-1].posNum = 2065
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00563378, 0.0225694, 0), \
                           ValErr(0.0271734, 0.538926, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000135793, 0.000239663, 0), \
                           -2739.7, 2065, 2065, -nan)
reports[-1].sigmaresid = ValErr(0.911893, 0.014189, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0373267, None, -0.000207487, None, 0.000225201, None, -7.86382e-05, None, 0.000225201, None, -7.86382e-05, None, 0.00387514, None, -0.000456306, None, 0.00387514, None, -0.000456306, None, 0.911989, None, 0.0107948, None, 0.911989, None, 0.0107948, None)
reports[-1].CovMatrix = ['0.000509377','0.000212477','-2.47438e-06','1.02579e-07','0','0','0','0','0','0.000212477','0.290442','-1.04827e-06','4.13278e-06','0','0','0','0','0','-2.47438e-06','-1.04827e-06','5.74384e-08','1.12067e-09','0','0','0','0','0','1.02579e-07','4.13278e-06','1.12067e-09','0.00020133','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025936, ("CSC", 1, 3, 2, 10), "MEp32_10"))
reports[-1].posNum = 2069
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00431602, 0.0222218, 0), \
                           ValErr(0.358768, 0.520419, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.41962e-05, 0.000240546, 0), \
                           -2758.49, 2069, 2069, -nan)
reports[-1].sigmaresid = ValErr(0.917891, 0.0142693, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00630149, None, -0.00263333, None, -0.00128062, None, -0.00199602, None, -0.00128062, None, -0.00199602, None, -0.0382282, None, -0.00225767, None, -0.0382282, None, -0.00225767, None, 0.917998, None, 0.010202, None, 0.917998, None, 0.010202, None)
reports[-1].CovMatrix = ['0.000493809','-0.000521347','-2.22971e-06','1.04296e-07','0','0','0','0','0','-0.000521347','0.270836','2.44361e-06','3.54886e-06','0','0','0','0','0','-2.22971e-06','2.44361e-06','5.78622e-08','1.36306e-09','0','0','0','0','0','1.04296e-07','3.54886e-06','1.36306e-09','0.000203614','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025952, ("CSC", 1, 3, 2, 12), "MEp32_12"))
reports[-1].posNum = 1840
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00234486, 0.0242818, 0), \
                           ValErr(-0.0113342, 0.555753, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000106912, 0.000274781, 0), \
                           -2384.33, 1840, 1840, -nan)
reports[-1].sigmaresid = ValErr(0.884175, 0.0145752, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.028047, None, 0.00142981, None, -0.00737052, None, 0.00173003, None, -0.00737052, None, 0.00173003, None, -0.000418744, None, 0.00151901, None, -0.000418744, None, 0.00151901, None, 0.884205, None, 0.0115215, None, 0.884205, None, 0.0115215, None)
reports[-1].CovMatrix = ['0.000589607','9.06457e-05','-3.52468e-06','1.54819e-07','0','0','0','0','0','9.06457e-05','0.308861','3.33435e-06','4.4165e-06','0','0','0','0','0','-3.52468e-06','3.33435e-06','7.55048e-08','7.47748e-10','0','0','0','0','0','1.54819e-07','4.4165e-06','7.47748e-10','0.00021244','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025968, ("CSC", 1, 3, 2, 14), "MEp32_14"))
reports[-1].posNum = 2318
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000469741, 0.0203425, 0), \
                           ValErr(0.101149, 0.498642, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000119918, 0.000231104, 0), \
                           -3055.32, 2318, 2318, -nan)
reports[-1].sigmaresid = ValErr(0.904042, 0.013277, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.015821, None, 0.00314116, None, -0.00465594, None, 0.00357716, None, -0.00465594, None, 0.00357716, None, -0.0420137, None, 0.00350582, None, -0.0420137, None, 0.00350582, None, 0.904126, None, 0.0122593, None, 0.904126, None, 0.0122593, None)
reports[-1].CovMatrix = ['0.000413818','0.000332799','-1.8034e-06','1.15905e-07','0','0','0','0','0','0.000332799','0.248644','-1.25328e-06','3.57961e-06','0','0','0','0','0','-1.8034e-06','-1.25328e-06','5.34093e-08','1.08493e-09','0','0','0','0','0','1.15905e-07','3.57961e-06','1.08493e-09','0.000176281','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025984, ("CSC", 1, 3, 2, 16), "MEp32_16"))
reports[-1].posNum = 2095
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000709813, 0.0214962, 0), \
                           ValErr(-0.0444234, 0.508537, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000138475, 0.000232839, 0), \
                           -2744.18, 2095, 2095, -nan)
reports[-1].sigmaresid = ValErr(0.896645, 0.0138515, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0176569, None, -0.000316717, None, 0.00599536, None, -2.89811e-05, None, 0.00599536, None, -2.89811e-05, None, 0.00329176, None, -6.61486e-05, None, 0.00329176, None, -6.61486e-05, None, 0.896748, None, 0.0118472, None, 0.896748, None, 0.0118472, None)
reports[-1].CovMatrix = ['0.000462088','8.77266e-05','-2.06067e-06','1.01483e-07','0','0','0','0','0','8.77266e-05','0.25861','-1.44265e-06','4.08413e-06','0','0','0','0','0','-2.06067e-06','-1.44265e-06','5.42138e-08','1.14041e-09','0','0','0','0','0','1.01483e-07','4.08413e-06','1.14041e-09','0.000191865','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026000, ("CSC", 1, 3, 2, 18), "MEp32_18"))
reports[-1].posNum = 2059
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0172416, 0.0226715, 0), \
                           ValErr(-0.20331, 0.530134, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.98383e-06, 0.000256841, 0), \
                           -2708.57, 2059, 2059, -nan)
reports[-1].sigmaresid = ValErr(0.901722, 0.0140519, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0546103, None, -0.00251676, None, -0.017229, None, -0.00282686, None, -0.017229, None, -0.00282686, None, 0.0157325, None, -0.00280788, None, 0.0157325, None, -0.00280788, None, 0.901746, None, 0.0113814, None, 0.901746, None, 0.0113814, None)
reports[-1].CovMatrix = ['0.000513996','-0.000489776','-2.79927e-06','8.69735e-08','0','0','0','0','0','-0.000489776','0.281042','4.59388e-06','4.9867e-06','0','0','0','0','0','-2.79927e-06','4.59388e-06','6.59675e-08','1.35716e-09','0','0','0','0','0','8.69735e-08','4.9867e-06','1.35716e-09','0.000197456','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026016, ("CSC", 1, 3, 2, 20), "MEp32_20"))
reports[-1].posNum = 1870
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00416064, 0.023815, 0), \
                           ValErr(0.102312, 0.570731, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.83939e-05, 0.000245356, 0), \
                           -2528.55, 1870, 1870, -nan)
reports[-1].sigmaresid = ValErr(0.935422, 0.015296, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0222608, None, 0.00235286, None, -0.00598618, None, 0.00236684, None, -0.00598618, None, 0.00236684, None, -0.00529072, None, 0.00220269, None, -0.00529072, None, 0.00220269, None, 0.935424, None, 0.00942585, None, 0.935424, None, 0.00942585, None)
reports[-1].CovMatrix = ['0.000567154','-0.000460177','-2.43756e-06','1.28323e-07','0','0','0','0','0','-0.000460177','0.325734','1.07888e-06','5.68374e-06','0','0','0','0','0','-2.43756e-06','1.07888e-06','6.01997e-08','1.266e-09','0','0','0','0','0','1.28323e-07','5.68374e-06','1.266e-09','0.00023397','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026032, ("CSC", 1, 3, 2, 22), "MEp32_22"))
reports[-1].posNum = 2083
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000220095, 0.0215985, 0), \
                           ValErr(-0.23765, 0.524765, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000141945, 0.000234186, 0), \
                           -2726.76, 2083, 2083, -nan)
reports[-1].sigmaresid = ValErr(0.895948, 0.0138812, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0269928, None, -0.000441624, None, -0.00526057, None, -0.000192772, None, -0.00526057, None, -0.000192772, None, -0.0545663, None, -0.000155098, None, -0.0545663, None, -0.000155098, None, 0.896059, None, 0.00961413, None, 0.896059, None, 0.00961413, None)
reports[-1].CovMatrix = ['0.000466493','-0.000173094','-2.10927e-06','1.07478e-07','0','0','0','0','0','-0.000173094','0.275378','3.82532e-06','4.6834e-06','0','0','0','0','0','-2.10927e-06','3.82532e-06','5.48432e-08','1.14959e-09','0','0','0','0','0','1.07478e-07','4.6834e-06','1.14959e-09','0.000192689','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026048, ("CSC", 1, 3, 2, 24), "MEp32_24"))
reports[-1].posNum = 2210
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0015902, 0.0213361, 0), \
                           ValErr(-0.0529301, 0.513217, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.19392e-05, 0.000240634, 0), \
                           -2927.87, 2210, 2210, -nan)
reports[-1].sigmaresid = ValErr(0.910163, 0.0136897, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0310073, None, -0.00218301, None, -0.00177597, None, -0.00241958, None, -0.00177597, None, -0.00241958, None, -0.00564862, None, -0.00224174, None, -0.00564862, None, -0.00224174, None, 0.910215, None, 0.0102525, None, 0.910215, None, 0.0102525, None)
reports[-1].CovMatrix = ['0.000455231','0.000430079','-2.15211e-06','1.19626e-07','0','0','0','0','0','0.000430079','0.263391','-2.79641e-06','4.2935e-06','0','0','0','0','0','-2.15211e-06','-2.79641e-06','5.79048e-08','1.15539e-09','0','0','0','0','0','1.19626e-07','4.2935e-06','1.15539e-09','0.00018741','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026064, ("CSC", 1, 3, 2, 26), "MEp32_26"))
reports[-1].posNum = 1845
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00762321, 0.0234524, 0), \
                           ValErr(-0.282882, 0.54458, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000150636, 0.000241519, 0), \
                           -2324.25, 1845, 1845, -nan)
reports[-1].sigmaresid = ValErr(0.85283, 0.0140392, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00744748, None, -0.000439705, None, 0.0007252, None, -0.0002899, None, 0.0007252, None, -0.0002899, None, -0.00334223, None, -0.00030948, None, -0.00334223, None, -0.00030948, None, 0.852994, None, 0.0114227, None, 0.852994, None, 0.0114227, None)
reports[-1].CovMatrix = ['0.000550016','0.000440296','-3.00385e-06','8.06273e-08','0','0','0','0','0','0.000440296','0.296567','2.6276e-06','4.62585e-06','0','0','0','0','0','-3.00385e-06','2.6276e-06','5.83312e-08','1.31344e-09','0','0','0','0','0','8.06273e-08','4.62585e-06','1.31344e-09','0.0001971','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026080, ("CSC", 1, 3, 2, 28), "MEp32_28"))
reports[-1].posNum = 2302
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0102619, 0.0215148, 0), \
                           ValErr(0.0776252, 0.530188, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000192464, 0.000238372, 0), \
                           -3144.01, 2302, 2302, -nan)
reports[-1].sigmaresid = ValErr(0.948211, 0.0139743, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00647615, None, 0.00200867, None, -0.00344473, None, 0.0020666, None, -0.00344473, None, 0.0020666, None, -0.024491, None, 0.0020221, None, -0.024491, None, 0.0020221, None, 0.948361, None, 0.0101419, None, 0.948361, None, 0.0101419, None)
reports[-1].CovMatrix = ['0.000462886','0.000161427','-2.02471e-06','1.09081e-07','0','0','0','0','0','0.000161427','0.281099','1.49242e-06','3.95174e-06','0','0','0','0','0','-2.02471e-06','1.49242e-06','5.68212e-08','1.27577e-09','0','0','0','0','0','1.09081e-07','3.95174e-06','1.27577e-09','0.000195282','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026096, ("CSC", 1, 3, 2, 30), "MEp32_30"))
reports[-1].posNum = 1662
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000691435, 0.0248422, 0), \
                           ValErr(0.118014, 0.557481, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.73348e-05, 0.00025069, 0), \
                           -2087.99, 1662, 1662, -nan)
reports[-1].sigmaresid = ValErr(0.849917, 0.0147417, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.017745, None, 0.0017294, None, 0.00173125, None, 0.00226525, None, 0.00173125, None, 0.00226525, None, -0.0287304, None, 0.00161421, None, -0.0287304, None, 0.00161421, None, 0.849922, None, 0.0116896, None, 0.849922, None, 0.0116896, None)
reports[-1].CovMatrix = ['0.000617134','-0.000361219','-3.38401e-06','1.05772e-07','0','0','0','0','0','-0.000361219','0.310786','1.17598e-06','5.22407e-06','0','0','0','0','0','-3.38401e-06','1.17598e-06','6.28456e-08','1.12687e-09','0','0','0','0','0','1.05772e-07','5.22407e-06','1.12687e-09','0.000217321','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026112, ("CSC", 1, 3, 2, 32), "MEp32_32"))
reports[-1].posNum = 2001
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00372346, 0.0238874, 0), \
                           ValErr(0.115223, 0.557508, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.98285e-05, 0.000258239, 0), \
                           -2720.46, 2001, 2001, -nan)
reports[-1].sigmaresid = ValErr(0.942312, 0.0148949, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0364026, None, -0.000123928, None, -0.00177062, None, 0.000510819, None, -0.00177062, None, 0.000510819, None, -0.0404672, None, 0.00019771, None, -0.0404672, None, 0.00019771, None, 0.942358, None, 0.0109888, None, 0.942358, None, 0.0109888, None)
reports[-1].CovMatrix = ['0.000570609','-0.000515299','-2.89787e-06','9.86401e-08','0','0','0','0','0','-0.000515299','0.310815','-5.07947e-07','3.92134e-06','0','0','0','0','0','-2.89787e-06','-5.07947e-07','6.66871e-08','1.43972e-09','0','0','0','0','0','9.86401e-08','3.92134e-06','1.43972e-09','0.00022186','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026128, ("CSC", 1, 3, 2, 34), "MEp32_34"))
reports[-1].posNum = 1941
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00234964, 0.0228986, 0), \
                           ValErr(-0.357079, 0.552339, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.50966e-05, 0.000248337, 0), \
                           -2572.7, 1941, 1941, -nan)
reports[-1].sigmaresid = ValErr(0.910761, 0.0146178, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0227206, None, 4.5529e-05, None, 0.00137846, None, 0.000479506, None, 0.00137846, None, 0.000479506, None, -0.0163295, None, 0.000541297, None, -0.0163295, None, 0.000541297, None, 0.910874, None, 0.0113341, None, 0.910874, None, 0.0113341, None)
reports[-1].CovMatrix = ['0.000524346','0.000504316','-2.44167e-06','1.22985e-07','0','0','0','0','0','0.000504316','0.305078','-4.78084e-06','5.19247e-06','0','0','0','0','0','-2.44167e-06','-4.78084e-06','6.16711e-08','1.35991e-09','0','0','0','0','0','1.22985e-07','5.19247e-06','1.35991e-09','0.000213681','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026144, ("CSC", 1, 3, 2, 36), "MEp32_36"))
reports[-1].posNum = 1711
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00464086, 0.0250612, 0), \
                           ValErr(-0.117379, 0.588269, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.41646e-05, 0.000257575, 0), \
                           -2260.04, 1711, 1711, -nan)
reports[-1].sigmaresid = ValErr(0.906619, 0.0154986, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00889958, None, 0.00174455, None, 0.00706457, None, 0.00201825, None, 0.00706457, None, 0.00201825, None, -0.0159291, None, 0.00181378, None, -0.0159291, None, 0.00181378, None, 0.906627, None, 0.0111068, None, 0.906627, None, 0.0111068, None)
reports[-1].CovMatrix = ['0.000628065','-0.000486259','-3.12592e-06','1.18531e-07','0','0','0','0','0','-0.000486259','0.346061','2.5611e-06','3.94686e-06','0','0','0','0','0','-3.12592e-06','2.5611e-06','6.63446e-08','1.46647e-09','0','0','0','0','0','1.18531e-07','3.94686e-06','1.46647e-09','0.000240208','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029448, ("CSC", 1, 4, 1, 1), "MEp41_01"))
reports[-1].posNum = 3867
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00675486, 0.00825457, 0), \
                           ValErr(0.0798851, 0.0940903, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000154715, 0.000217339, 0), \
                           -2908.2, 3867, 3867, -nan)
reports[-1].sigmaresid = ValErr(0.513306, 0.00583678, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00577602, None, -0.000383444, None, 0.00671263, None, 2.12816e-05, None, 0.00671263, None, 2.12816e-05, None, 0.0104859, None, -0.000228148, None, 0.0104859, None, -0.000228148, None, 0.513389, None, 0.0118575, None, 0.513389, None, 0.0118575, None)
reports[-1].CovMatrix = ['6.81379e-05','1.48193e-06','7.741e-09','2.09323e-08','0','0','0','0','0','1.48193e-06','0.00885298','-1.24614e-07','2.32704e-07','0','0','0','0','0','7.741e-09','-1.24614e-07','4.72363e-08','5.38317e-10','0','0','0','0','0','2.09323e-08','2.32704e-07','5.38317e-10','3.40681e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029464, ("CSC", 1, 4, 1, 3), "MEp41_03"))
reports[-1].posNum = 3783
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00308378, 0.00853957, 0), \
                           ValErr(0.0687092, 0.0969593, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000229702, 0.000223903, 0), \
                           -2931.49, 3783, 3783, -nan)
reports[-1].sigmaresid = ValErr(0.525173, 0.00603767, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0157695, None, -0.00140917, None, -0.00297775, None, -0.00120123, None, -0.00297775, None, -0.00120123, None, -0.0098116, None, -0.00104548, None, -0.0098116, None, -0.00104548, None, 0.525284, None, 0.0119955, None, 0.525284, None, 0.0119955, None)
reports[-1].CovMatrix = ['7.29242e-05','3.60892e-06','-2.8443e-08','2.1893e-08','0','0','0','0','0','3.60892e-06','0.0094011','-7.35287e-07','2.43595e-07','0','0','0','0','0','-2.8443e-08','-7.35287e-07','5.01325e-08','5.53383e-10','0','0','0','0','0','2.1893e-08','2.43595e-07','5.53383e-10','3.64536e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029480, ("CSC", 1, 4, 1, 5), "MEp41_05"))
reports[-1].posNum = 3688
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00378178, 0.00846645, 0), \
                           ValErr(0.053733, 0.0954894, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.32946e-05, 0.000220496, 0), \
                           -2777.9, 3688, 3688, -nan)
reports[-1].sigmaresid = ValErr(0.513907, 0.00598374, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0080248, None, -0.000506019, None, -0.00372579, None, -0.000379868, None, -0.00372579, None, -0.000379868, None, 0.00915871, None, -0.000563732, None, 0.00915871, None, -0.000563732, None, 0.513932, None, 0.0119864, None, 0.513932, None, 0.0119864, None)
reports[-1].CovMatrix = ['7.16808e-05','-1.65935e-05','4.43918e-08','2.17285e-08','0','0','0','0','0','-1.65935e-05','0.00911823','-1.71026e-07','2.36613e-07','0','0','0','0','0','4.43918e-08','-1.71026e-07','4.86185e-08','5.5754e-10','0','0','0','0','0','2.17285e-08','2.36613e-07','5.5754e-10','3.58052e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029496, ("CSC", 1, 4, 1, 7), "MEp41_07"))
reports[-1].posNum = 3780
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00411886, 0.00851066, 0), \
                           ValErr(0.0557976, 0.0976534, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000102888, 0.000226066, 0), \
                           -2911.9, 3780, 3780, -nan)
reports[-1].sigmaresid = ValErr(0.522775, 0.00601241, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00523869, None, 0.00131612, None, -0.00384863, None, 0.00144348, None, -0.00384863, None, 0.00144348, None, -0.0066723, None, 0.00129491, None, -0.0066723, None, 0.00129491, None, 0.522817, None, 0.0111984, None, 0.522817, None, 0.0111984, None)
reports[-1].CovMatrix = ['7.24314e-05','-3.10415e-05','-3.96343e-08','1.92768e-08','0','0','0','0','0','-3.10415e-05','0.0095362','6.68543e-08','2.43571e-07','0','0','0','0','0','-3.96343e-08','6.68543e-08','5.11058e-08','5.72852e-10','0','0','0','0','0','1.92768e-08','2.43571e-07','5.72852e-10','3.61492e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029512, ("CSC", 1, 4, 1, 9), "MEp41_09"))
reports[-1].posNum = 3818
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00158105, 0.00836244, 0), \
                           ValErr(-0.0268399, 0.0967914, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.52397e-05, 0.000220086, 0), \
                           -2895.1, 3818, 3818, -nan)
reports[-1].sigmaresid = ValErr(0.516508, 0.00591075, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00255042, None, -0.00265655, None, 0.0015101, None, -0.0024886, None, 0.0015101, None, -0.0024886, None, 0.0054776, None, -0.00222313, None, 0.0054776, None, -0.00222313, None, 0.516515, None, 0.0122715, None, 0.516515, None, 0.0122715, None)
reports[-1].CovMatrix = ['6.99304e-05','-1.84161e-05','-3.09727e-08','2.04355e-08','0','0','0','0','0','-1.84161e-05','0.00936857','2.65891e-08','2.37196e-07','0','0','0','0','0','-3.09727e-08','2.65891e-08','4.8438e-08','5.42608e-10','0','0','0','0','0','2.04355e-08','2.37196e-07','5.42608e-10','3.4937e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029528, ("CSC", 1, 4, 1, 11), "MEp41_11"))
reports[-1].posNum = 4089
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00259416, 0.00829693, 0), \
                           ValErr(-0.002687, 0.094739, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.88838e-05, 0.000217879, 0), \
                           -3208.54, 4089, 4089, -nan)
reports[-1].sigmaresid = ValErr(0.530324, 0.00586427, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0132276, None, 0.000781094, None, -0.00263009, None, 0.000849599, None, -0.00263009, None, 0.000849599, None, -0.000544921, None, 0.000757943, None, -0.000544921, None, 0.000757943, None, 0.53033, None, 0.012716, None, 0.53033, None, 0.012716, None)
reports[-1].CovMatrix = ['6.8839e-05','1.60949e-05','-3.87711e-08','2.12088e-08','0','0','0','0','0','1.60949e-05','0.00897548','-6.83178e-07','2.39907e-07','0','0','0','0','0','-3.87711e-08','-6.83178e-07','4.74714e-08','5.38289e-10','0','0','0','0','0','2.12088e-08','2.39907e-07','5.38289e-10','3.43898e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029544, ("CSC", 1, 4, 1, 13), "MEp41_13"))
reports[-1].posNum = 4069
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00466711, 0.0080765, 0), \
                           ValErr(-0.093002, 0.0934545, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.63464e-05, 0.00021279, 0), \
                           -3071.21, 4069, 4069, -nan)
reports[-1].sigmaresid = ValErr(0.514707, 0.00570559, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00343754, None, 0.00191152, None, 0.00439336, None, 0.00193688, None, 0.00439336, None, 0.00193688, None, 0.00949954, None, 0.00224828, None, 0.00949954, None, 0.00224828, None, 0.514772, None, 0.0113034, None, 0.514772, None, 0.0113034, None)
reports[-1].CovMatrix = ['6.52299e-05','-2.15302e-05','-5.62437e-08','1.85012e-08','0','0','0','0','0','-2.15302e-05','0.00873374','1.3755e-07','2.24211e-07','0','0','0','0','0','-5.62437e-08','1.3755e-07','4.52796e-08','5.059e-10','0','0','0','0','0','1.85012e-08','2.24211e-07','5.059e-10','3.25538e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029560, ("CSC", 1, 4, 1, 15), "MEp41_15"))
reports[-1].posNum = 3866
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0032889, 0.00823952, 0), \
                           ValErr(-0.00909372, 0.0929226, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.31035e-05, 0.000215302, 0), \
                           -2898.78, 3866, 3866, -nan)
reports[-1].sigmaresid = ValErr(0.512156, 0.00582447, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0139733, None, -0.000481645, None, 0.00330893, None, -0.00018947, None, 0.00330893, None, -0.00018947, None, -0.00137991, None, -0.000314138, None, -0.00137991, None, -0.000314138, None, 0.512157, None, 0.0123344, None, 0.512157, None, 0.0123344, None)
reports[-1].CovMatrix = ['6.78896e-05','1.87225e-05','-1.68461e-09','2.07595e-08','0','0','0','0','0','1.87225e-05','0.0086346','-3.17381e-07','2.30893e-07','0','0','0','0','0','-1.68461e-09','-3.17381e-07','4.63548e-08','5.21199e-10','0','0','0','0','0','2.07595e-08','2.30893e-07','5.21199e-10','3.39245e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029576, ("CSC", 1, 4, 1, 17), "MEp41_17"))
reports[-1].posNum = 3852
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00616608, 0.00848186, 0), \
                           ValErr(0.0451667, 0.0965583, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000189115, 0.00022316, 0), \
                           -2994.14, 3852, 3852, -nan)
reports[-1].sigmaresid = ValErr(0.52642, 0.00599745, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0155418, None, 0.00102285, None, 0.00614156, None, 0.00140638, None, 0.00614156, None, 0.00140638, None, -0.00517263, None, 0.0013431, None, -0.00517263, None, 0.0013431, None, 0.526491, None, 0.0118611, None, 0.526491, None, 0.0118611, None)
reports[-1].CovMatrix = ['7.19419e-05','-5.80163e-07','5.84774e-09','2.25368e-08','0','0','0','0','0','-5.80163e-07','0.0093235','-2.80147e-07','2.36487e-07','0','0','0','0','0','5.84774e-09','-2.80147e-07','4.98003e-08','5.69046e-10','0','0','0','0','0','2.25368e-08','2.36487e-07','5.69046e-10','3.59694e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029456, ("CSC", 1, 4, 1, 2), "MEp41_02"))
reports[-1].posNum = 3958
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0014833, 0.0085481, 0), \
                           ValErr(0.0875129, 0.0985461, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.00579e-05, 0.000222947, 0), \
                           -3159.36, 3958, 3958, -nan)
reports[-1].sigmaresid = ValErr(0.537559, 0.00604191, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00942536, None, -0.00221774, None, -0.0013124, None, -0.00211808, None, -0.0013124, None, -0.00211808, None, -0.00426184, None, -0.00230885, None, -0.00426184, None, -0.00230885, None, 0.53762, None, 0.0103058, None, 0.53762, None, 0.0103058, None)
reports[-1].CovMatrix = ['7.307e-05','-2.25444e-05','2.02872e-08','2.21076e-08','0','0','0','0','0','-2.25444e-05','0.00971134','1.29769e-07','2.5508e-07','0','0','0','0','0','2.02872e-08','1.29769e-07','4.97055e-08','5.9666e-10','0','0','0','0','0','2.21076e-08','2.5508e-07','5.9666e-10','3.65047e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029472, ("CSC", 1, 4, 1, 4), "MEp41_04"))
reports[-1].posNum = 3854
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00293098, 0.0087024, 0), \
                           ValErr(-0.0687635, 0.0988665, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.0726e-05, 0.000228712, 0), \
                           -3092.99, 3854, 3854, -nan)
reports[-1].sigmaresid = ValErr(0.539886, 0.00614939, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00628598, None, -0.000850946, None, -0.00314334, None, -0.000664184, None, -0.00314334, None, -0.000664184, None, -0.00621238, None, -0.000705992, None, -0.00621238, None, -0.000705992, None, 0.53992, None, 0.0105317, None, 0.53992, None, 0.0105317, None)
reports[-1].CovMatrix = ['7.57318e-05','-2.94161e-05','-2.73666e-08','2.24315e-08','0','0','0','0','0','-2.94161e-05','0.00977459','2.8328e-07','2.6012e-07','0','0','0','0','0','-2.73666e-08','2.8328e-07','5.23091e-08','6.13084e-10','0','0','0','0','0','2.24315e-08','2.6012e-07','6.13084e-10','3.78151e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029488, ("CSC", 1, 4, 1, 6), "MEp41_06"))
reports[-1].posNum = 3818
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00695155, 0.00866139, 0), \
                           ValErr(0.0483958, 0.102647, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000109728, 0.000231366, 0), \
                           -2997.7, 3818, 3818, -nan)
reports[-1].sigmaresid = ValErr(0.530584, 0.00607193, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.012759, None, 0.00229983, None, -0.00702376, None, 0.00240675, None, -0.00702376, None, 0.00240675, None, -0.00542821, None, 0.00260125, None, -0.00542821, None, 0.00260125, None, 0.530614, None, 0.0107521, None, 0.530614, None, 0.0107521, None)
reports[-1].CovMatrix = ['7.50197e-05','9.36513e-05','-1.84539e-07','2.50542e-08','0','0','0','0','0','9.36513e-05','0.0105363','-3.43374e-06','2.91375e-07','0','0','0','0','0','-1.84539e-07','-3.43374e-06','5.35303e-08','4.45438e-10','0','0','0','0','0','2.50542e-08','2.91375e-07','4.45438e-10','3.68684e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029504, ("CSC", 1, 4, 1, 8), "MEp41_08"))
reports[-1].posNum = 3840
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0108014, 0.00868053, 0), \
                           ValErr(-0.0259956, 0.100685, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.34535e-05, 0.00023033, 0), \
                           -3067.6, 3840, 3840, -nan)
reports[-1].sigmaresid = ValErr(0.5379, 0.00613792, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0199613, None, 0.00179308, None, -0.0108013, None, 0.00190668, None, -0.0108013, None, 0.00190668, None, -0.00508315, None, 0.00193775, None, -0.00508315, None, 0.00193775, None, 0.537907, None, 0.0102789, None, 0.537907, None, 0.0102789, None)
reports[-1].CovMatrix = ['7.53517e-05','3.60609e-06','1.14055e-08','2.3416e-08','0','0','0','0','0','3.60609e-06','0.0101375','6.73585e-07','2.78194e-07','0','0','0','0','0','1.14055e-08','6.73585e-07','5.3052e-08','6.3606e-10','0','0','0','0','0','2.3416e-08','2.78194e-07','6.3606e-10','3.76742e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029520, ("CSC", 1, 4, 1, 10), "MEp41_10"))
reports[-1].posNum = 3879
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00515805, 0.00864392, 0), \
                           ValErr(-0.0382251, 0.0981388, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000122995, 0.000225082, 0), \
                           -3102.08, 3879, 3879, -nan)
reports[-1].sigmaresid = ValErr(0.538353, 0.00611202, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00449866, None, -0.00497897, None, -0.00517563, None, -0.00510528, None, -0.00517563, None, -0.00510528, None, -0.00297579, None, -0.00509306, None, -0.00297579, None, -0.00509306, None, 0.538392, None, 0.00976902, None, 0.538392, None, 0.00976902, None)
reports[-1].CovMatrix = ['7.47174e-05','-1.93226e-06','-6.0469e-09','2.21393e-08','0','0','0','0','0','-1.93226e-06','0.00963123','-2.92138e-07','2.63197e-07','0','0','0','0','0','-6.0469e-09','-2.92138e-07','5.06618e-08','5.90751e-10','0','0','0','0','0','2.21393e-08','2.63197e-07','5.90751e-10','3.73569e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029536, ("CSC", 1, 4, 1, 12), "MEp41_12"))
reports[-1].posNum = 3835
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00246499, 0.00830575, 0), \
                           ValErr(-0.0469783, 0.0949454, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000196955, 0.000220569, 0), \
                           -2880.14, 3835, 3835, -nan)
reports[-1].sigmaresid = ValErr(0.512772, 0.005855, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00217303, None, 0.00178061, None, -0.00199933, None, 0.00144924, None, -0.00199933, None, 0.00144924, None, 0.00862308, None, 0.00145525, None, 0.00862308, None, 0.00145525, None, 0.51284, None, 0.0113003, None, 0.51284, None, 0.0113003, None)
reports[-1].CovMatrix = ['6.89854e-05','-1.65299e-05','-1.37439e-07','1.88679e-08','0','0','0','0','0','-1.65299e-05','0.00901463','-4.46827e-07','2.25166e-07','0','0','0','0','0','-1.37439e-07','-4.46827e-07','4.86507e-08','4.92243e-10','0','0','0','0','0','1.88679e-08','2.25166e-07','4.92243e-10','3.42812e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029552, ("CSC", 1, 4, 1, 14), "MEp41_14"))
reports[-1].posNum = 3912
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0084445, 0.00867604, 0), \
                           ValErr(-0.0492694, 0.0998082, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000127012, 0.000226041, 0), \
                           -3159.18, 3912, 3912, -nan)
reports[-1].sigmaresid = ValErr(0.542604, 0.00613437, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0150781, None, 0.000323832, None, -0.0083652, None, 0.00029574, None, -0.0083652, None, 0.00029574, None, 0.00211917, None, 0.000170015, None, 0.00211917, None, 0.000170015, None, 0.542641, None, 0.00970586, None, 0.542641, None, 0.00970586, None)
reports[-1].CovMatrix = ['7.52736e-05','1.02034e-05','-1.167e-08','2.34176e-08','0','0','0','0','0','1.02034e-05','0.00996168','-1.70397e-07','2.6856e-07','0','0','0','0','0','-1.167e-08','-1.70397e-07','5.10945e-08','6.01584e-10','0','0','0','0','0','2.34176e-08','2.6856e-07','6.01584e-10','3.76306e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029568, ("CSC", 1, 4, 1, 16), "MEp41_16"))
reports[-1].posNum = 4006
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00105705, 0.00839409, 0), \
                           ValErr(-0.0831935, 0.0949624, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.18433e-05, 0.000221137, 0), \
                           -3150.11, 4006, 4006, -nan)
reports[-1].sigmaresid = ValErr(0.531212, 0.00593464, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00301043, None, 0.0030865, None, 0.00092034, None, 0.00341076, None, 0.00092034, None, 0.00341076, None, -0.012873, None, 0.00373221, None, -0.012873, None, 0.00373221, None, 0.53127, None, 0.0107568, None, 0.53127, None, 0.0107568, None)
reports[-1].CovMatrix = ['7.04607e-05','-1.33584e-05','1.27738e-09','2.27691e-08','0','0','0','0','0','-1.33584e-05','0.00901786','-8.01272e-08','2.27929e-07','0','0','0','0','0','1.27738e-09','-8.01272e-08','4.89014e-08','5.80988e-10','0','0','0','0','0','2.27691e-08','2.27929e-07','5.80988e-10','3.52201e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029584, ("CSC", 1, 4, 1, 18), "MEp41_18"))
reports[-1].posNum = 3856
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00368843, 0.00880126, 0), \
                           ValErr(0.0167909, 0.101248, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000234348, 0.000226622, 0), \
                           -3136.69, 3856, 3856, -nan)
reports[-1].sigmaresid = ValErr(0.545812, 0.00621526, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00848186, None, 0.00197549, None, -0.00353283, None, 0.00214024, None, -0.00353283, None, 0.00214024, None, -0.0213033, None, 0.00208391, None, -0.0213033, None, 0.00208391, None, 0.54589, None, 0.0103525, None, 0.54589, None, 0.0103525, None)
reports[-1].CovMatrix = ['7.74622e-05','4.02044e-05','4.88754e-08','2.56914e-08','0','0','0','0','0','4.02044e-05','0.0102511','1.39134e-07','2.91273e-07','0','0','0','0','0','4.88754e-08','1.39134e-07','5.13575e-08','6.42275e-10','0','0','0','0','0','2.56914e-08','2.91273e-07','6.42275e-10','3.86296e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029960, ("CSC", 1, 4, 2, 1), "MEp42_01"))
reports[-1].posNum = 1883
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00830446, 0.0246766, 0), \
                           ValErr(-0.39828, 0.648201, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.94942e-05, 0.000273445, 0), \
                           -2600.95, 1883, 1883, -nan)
reports[-1].sigmaresid = ValErr(0.96305, 0.0156933, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0313464, None, -0.00170595, None, -0.00942936, None, -0.00153358, None, -0.00942936, None, -0.00153358, None, 0.00242169, None, -0.0015802, None, 0.00242169, None, -0.0015802, None, 0.963148, None, 0.0107067, None, 0.963148, None, 0.0107067, None)
reports[-1].CovMatrix = ['0.000608935','-0.00333459','-2.65762e-06','7.96967e-08','0','0','0','0','0','-0.00333459','0.420165','8.51714e-06','5.79553e-06','0','0','0','0','0','-2.65762e-06','8.51714e-06','7.4772e-08','1.70091e-09','0','0','0','0','0','7.96967e-08','5.79553e-06','1.70091e-09','0.000246281','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029976, ("CSC", 1, 4, 2, 3), "MEp42_03"))
reports[-1].posNum = 1810
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00919993, 0.0260769, 0), \
                           ValErr(0.00580586, 0.581039, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00015953, 0.00029466, 0), \
                           -2378.92, 1810, 1810, -nan)
reports[-1].sigmaresid = ValErr(0.900688, 0.0149703, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0179985, None, -0.00134709, None, -0.0174402, None, -0.000763708, None, -0.0174402, None, -0.000763708, None, -0.0268172, None, -0.00110616, None, -0.0268172, None, -0.00110616, None, 0.900743, None, 0.0115843, None, 0.900743, None, 0.0115843, None)
reports[-1].CovMatrix = ['0.000680006','6.76373e-05','-4.48541e-06','1.03505e-07','0','0','0','0','0','6.76373e-05','0.337607','2.0473e-06','4.84755e-06','0','0','0','0','0','-4.48541e-06','2.0473e-06','8.68246e-08','1.41743e-09','0','0','0','0','0','1.03505e-07','4.84755e-06','1.41743e-09','0.000224111','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029992, ("CSC", 1, 4, 2, 5), "MEp42_05"))
reports[-1].posNum = 1887
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00308509, 0.024321, 0), \
                           ValErr(0.313353, 0.580499, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000182053, 0.000270271, 0), \
                           -2511.84, 1887, 1887, -nan)
reports[-1].sigmaresid = ValErr(0.915936, 0.0149095, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0334088, None, 0.00100286, None, -0.0108767, None, 0.00125343, None, -0.0108767, None, 0.00125343, None, 0.0183098, None, 0.00124851, None, 0.0183098, None, 0.00124851, None, 0.916111, None, 0.0106192, None, 0.916111, None, 0.0106192, None)
reports[-1].CovMatrix = ['0.000591509','-0.000203773','-3.27068e-06','1.147e-07','0','0','0','0','0','-0.000203773','0.33698','-4.37365e-06','4.63059e-06','0','0','0','0','0','-3.27068e-06','-4.37365e-06','7.30465e-08','1.25598e-09','0','0','0','0','0','1.147e-07','4.63059e-06','1.25598e-09','0.000222295','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030008, ("CSC", 1, 4, 2, 7), "MEp42_07"))
reports[-1].posNum = 2027
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00478079, 0.0236574, 0), \
                           ValErr(0.252172, 0.570286, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000145364, 0.000264122, 0), \
                           -2778.3, 2027, 2027, -nan)
reports[-1].sigmaresid = ValErr(0.952861, 0.0149655, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00580023, None, 0.00094886, None, 0.0106684, None, 0.00126475, None, 0.0106684, None, 0.00126475, None, 0.0166678, None, 0.00122267, None, 0.0166678, None, 0.00122267, None, 0.952968, None, 0.011747, None, 0.952968, None, 0.011747, None)
reports[-1].CovMatrix = ['0.000559675','-0.000195036','-2.79188e-06','1.11753e-07','0','0','0','0','0','-0.000195036','0.325227','3.08612e-06','4.22952e-06','0','0','0','0','0','-2.79188e-06','3.08612e-06','6.97604e-08','1.51905e-09','0','0','0','0','0','1.11753e-07','4.22952e-06','1.51905e-09','0.000223968','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030024, ("CSC", 1, 4, 2, 9), "MEp42_09"))
reports[-1].posNum = 1920
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0104371, 0.0255636, 0), \
                           ValErr(0.288105, 0.604601, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.12119e-05, 0.000282704, 0), \
                           -2692.61, 1920, 1920, -nan)
reports[-1].sigmaresid = ValErr(0.9836, 0.0158727, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0304372, None, 0.00446021, None, -0.0090616, None, 0.00446622, None, -0.0090616, None, 0.00446622, None, -0.0342949, None, 0.00440531, None, -0.0342949, None, 0.00440531, None, 0.983661, None, 0.010691, None, 0.983661, None, 0.010691, None)
reports[-1].CovMatrix = ['0.0006535','0.000124839','-3.45786e-06','1.41267e-07','0','0','0','0','0','0.000124839','0.365542','-3.61893e-06','5.46641e-06','0','0','0','0','0','-3.45786e-06','-3.61893e-06','7.99216e-08','1.48341e-09','0','0','0','0','0','1.41267e-07','5.46641e-06','1.48341e-09','0.000251946','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030040, ("CSC", 1, 4, 2, 11), "MEp42_11"))
reports[-1].posNum = 2026
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0091141, 0.0236778, 0), \
                           ValErr(0.0499477, 0.321314, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000164694, 0.000264395, 0), \
                           -2749.62, 2026, 2026, -nan)
reports[-1].sigmaresid = ValErr(0.940099, 0.0147287, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-8.65567e-05, None, 0.000280057, None, 0.00232333, None, 0.000546641, None, 0.00232333, None, 0.000546641, None, -0.00331257, None, 2.05381e-05, None, -0.00331257, None, 2.05381e-05, None, 0.940189, None, 0.0116315, None, 0.940189, None, 0.0116315, None)
reports[-1].CovMatrix = ['0.000560637','-0.000766813','-2.92932e-06','2.11713e-07','0','0','0','0','0','-0.000766813','0.103243','5.39628e-06','0.0005258','0','0','0','0','0','-2.92932e-06','5.39628e-06','6.99047e-08','-6.63445e-10','0','0','0','0','0','2.11713e-07','0.0005258','-6.63445e-10','0.000216936','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030056, ("CSC", 1, 4, 2, 13), "MEp42_13"))
reports[-1].posNum = 2038
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00697355, 0.0234676, 0), \
                           ValErr(0.00341093, 0.586678, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.68605e-05, 0.000259609, 0), \
                           -2782.36, 2038, 2038, -nan)
reports[-1].sigmaresid = ValErr(0.947723, 0.0148445, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0169258, None, -0.00396173, None, 0.00879719, None, -0.00384503, None, 0.00879719, None, -0.00384503, None, -0.0166684, None, -0.00395088, None, -0.0166684, None, -0.00395088, None, 0.947725, None, 0.0113412, None, 0.947725, None, 0.0113412, None)
reports[-1].CovMatrix = ['0.000550727','-0.000309789','-2.72275e-06','1.7445e-07','0','0','0','0','0','-0.000309789','0.344192','9.50777e-06','5.29977e-06','0','0','0','0','0','-2.72275e-06','9.50777e-06','6.73971e-08','9.15173e-10','0','0','0','0','0','1.7445e-07','5.29977e-06','9.15173e-10','0.000220361','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030072, ("CSC", 1, 4, 2, 15), "MEp42_15"))
reports[-1].posNum = 2182
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0062818, 0.0230846, 0), \
                           ValErr(-0.039576, 0.557966, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000200681, 0.000259266, 0), \
                           -3004.36, 2182, 2182, -nan)
reports[-1].sigmaresid = ValErr(0.958804, 0.0145137, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00782679, None, 0.00252072, None, 0.00195071, None, 0.00271757, None, 0.00195071, None, 0.00271757, None, 0.00429579, None, 0.00279062, None, 0.00429579, None, 0.00279062, None, 0.95895, None, 0.01095, None, 0.95895, None, 0.01095, None)
reports[-1].CovMatrix = ['0.000532897','0.000505415','-2.72335e-06','1.22248e-07','0','0','0','0','0','0.000505415','0.311326','2.9116e-06','4.94342e-06','0','0','0','0','0','-2.72335e-06','2.9116e-06','6.72189e-08','1.37747e-09','0','0','0','0','0','1.22248e-07','4.94342e-06','1.37747e-09','0.000210649','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030088, ("CSC", 1, 4, 2, 17), "MEp42_17"))
reports[-1].posNum = 1999
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0314768, 0.0242797, 0), \
                           ValErr(-0.0435426, 0.310176, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000183757, 0.000273671, 0), \
                           -2704.42, 1999, 1999, -nan)
reports[-1].sigmaresid = ValErr(0.936081, 0.0148014, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.019738, None, -0.00228882, None, -0.0232131, None, -0.00218428, None, -0.0232131, None, -0.00218428, None, -0.0393311, None, -0.0022053, None, -0.0393311, None, -0.0022053, None, 0.936188, None, 0.0107679, None, 0.936188, None, 0.0107679, None)
reports[-1].CovMatrix = ['0.000589506','6.18716e-05','-3.35973e-06','1.02025e-07','0','0','0','0','0','6.18716e-05','0.0962092','-1.96841e-06','-0.000138225','0','0','0','0','0','-3.35973e-06','-1.96841e-06','7.48958e-08','-1.10888e-09','0','0','0','0','0','1.02025e-07','-0.000138225','-1.10888e-09','0.000219084','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030104, ("CSC", 1, 4, 2, 19), "MEp42_19"))
reports[-1].posNum = 2047
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00265144, 0.0232236, 0), \
                           ValErr(-0.213157, 0.579812, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.82499e-05, 0.000256523, 0), \
                           -2823.85, 2047, 2047, -nan)
reports[-1].sigmaresid = ValErr(0.961313, 0.0150236, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0145213, None, 0.000348528, None, 0.000600263, None, 0.00021439, None, 0.000600263, None, 0.00021439, None, 0.00558542, None, 0.000356726, None, 0.00558542, None, 0.000356726, None, 0.961382, None, 0.0113332, None, 0.961382, None, 0.0113332, None)
reports[-1].CovMatrix = ['0.000539338','0.000258951','-2.40371e-06','1.52435e-07','0','0','0','0','0','0.000258951','0.336182','-2.5457e-06','5.71115e-06','0','0','0','0','0','-2.40371e-06','-2.5457e-06','6.58041e-08','1.29592e-09','0','0','0','0','0','1.52435e-07','5.71115e-06','1.29592e-09','0.000225712','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030120, ("CSC", 1, 4, 2, 21), "MEp42_21"))
reports[-1].posNum = 1599
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0166641, 0.025562, 0), \
                           ValErr(0.236469, 0.597869, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.65357e-05, 0.00026909, 0), \
                           -2105.28, 1599, 1599, -nan)
reports[-1].sigmaresid = ValErr(0.902753, 0.0159637, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00544737, None, -0.00407905, None, -0.014869, None, -0.00346909, None, -0.014869, None, -0.00346909, None, -0.0327451, None, -0.00362266, None, -0.0327451, None, -0.00362266, None, 0.902792, None, 0.0124278, None, 0.902792, None, 0.0124278, None)
reports[-1].CovMatrix = ['0.000653417','-0.000462201','-3.22462e-06','1.17427e-07','0','0','0','0','0','-0.000462201','0.357447','5.2841e-06','4.41145e-06','0','0','0','0','0','-3.22462e-06','5.2841e-06','7.24094e-08','1.58555e-09','0','0','0','0','0','1.17427e-07','4.41145e-06','1.58555e-09','0.000254842','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030136, ("CSC", 1, 4, 2, 23), "MEp42_23"))
reports[-1].posNum = 2121
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00263135, 0.0218492, 0), \
                           ValErr(-0.370175, 0.521323, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000242539, 0.000243071, 0), \
                           -2827.15, 2121, 2121, -nan)
reports[-1].sigmaresid = ValErr(0.917583, 0.0140882, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0284199, None, 0.00257715, None, 0.006556, None, 0.00255897, None, 0.006556, None, 0.00255897, None, 0.00471176, None, 0.00270484, None, 0.00471176, None, 0.00270484, None, 0.917909, None, 0.0119153, None, 0.917909, None, 0.0119153, None)
reports[-1].CovMatrix = ['0.000477388','0.000252139','-2.17828e-06','1.1157e-07','0','0','0','0','0','0.000252139','0.271778','-1.99733e-06','5.19794e-06','0','0','0','0','0','-2.17828e-06','-1.99733e-06','5.90836e-08','1.26594e-09','0','0','0','0','0','1.1157e-07','5.19794e-06','1.26594e-09','0.000198478','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030152, ("CSC", 1, 4, 2, 25), "MEp42_25"))
reports[-1].posNum = 2145
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0200957, 0.0234108, 0), \
                           ValErr(-0.190132, 0.560345, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000230625, 0.000264193, 0), \
                           -2942.29, 2145, 2145, -nan)
reports[-1].sigmaresid = ValErr(0.953828, 0.0145621, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00549489, None, -0.000443379, None, -0.0102685, None, 5.34111e-05, None, -0.0102685, None, 5.34111e-05, None, -0.0129868, None, -0.000124648, None, -0.0129868, None, -0.000124648, None, 0.954053, None, 0.0119718, None, 0.954053, None, 0.0119718, None)
reports[-1].CovMatrix = ['0.000548067','0.000105047','-2.94054e-06','9.85212e-08','0','0','0','0','0','0.000105047','0.313986','1.60661e-07','5.65475e-06','0','0','0','0','0','-2.94054e-06','1.60661e-07','6.97978e-08','1.3209e-09','0','0','0','0','0','9.85212e-08','5.65475e-06','1.3209e-09','0.000212055','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030168, ("CSC", 1, 4, 2, 27), "MEp42_27"))
reports[-1].posNum = 1895
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00313592, 0.0254122, 0), \
                           ValErr(-0.193506, 0.608602, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.61893e-05, 0.00027092, 0), \
                           -2606.3, 1895, 1895, -nan)
reports[-1].sigmaresid = ValErr(0.957333, 0.0155499, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00852678, None, 0.000254138, None, 0.000686507, None, 0.000853385, None, 0.000686507, None, 0.000853385, None, 0.0232922, None, 0.000773577, None, 0.0232922, None, 0.000773577, None, 0.957384, None, 0.0104014, None, 0.957384, None, 0.0104014, None)
reports[-1].CovMatrix = ['0.000645782','-0.0018984','-3.38915e-06','1.37388e-07','0','0','0','0','0','-0.0018984','0.370396','9.8284e-06','5.82452e-06','0','0','0','0','0','-3.38915e-06','9.8284e-06','7.33978e-08','1.21982e-09','0','0','0','0','0','1.37388e-07','5.82452e-06','1.21982e-09','0.000241803','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030184, ("CSC", 1, 4, 2, 29), "MEp42_29"))
reports[-1].posNum = 2053
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00641344, 0.0234899, 0), \
                           ValErr(0.118914, 0.333283, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000182156, 0.000259733, 0), \
                           -2759.15, 2053, 2053, -nan)
reports[-1].sigmaresid = ValErr(0.927769, 0.0144505, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0314836, None, 0.000196654, None, 0.00136972, None, 0.000779218, None, 0.00136972, None, 0.000779218, None, -0.002869, None, 0.000461642, None, -0.002869, None, 0.000461642, None, 0.927891, None, 0.0123891, None, 0.927891, None, 0.0123891, None)
reports[-1].CovMatrix = ['0.000551775','0.000700221','-2.98651e-06','1.34728e-07','0','0','0','0','0','0.000700221','0.111077','3.57433e-06','0.000427303','0','0','0','0','0','-2.98651e-06','3.57433e-06','6.74612e-08','-3.0829e-08','0','0','0','0','0','1.34728e-07','0.000427303','-3.0829e-08','0.00020882','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030200, ("CSC", 1, 4, 2, 31), "MEp42_31"))
reports[-1].posNum = 1810
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00398436, 0.0255071, 0), \
                           ValErr(-0.0380091, 0.618266, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.82513e-05, 0.000279953, 0), \
                           -2487.24, 1810, 1810, -nan)
reports[-1].sigmaresid = ValErr(0.956222, 0.015893, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0134586, None, 0.00164305, None, 0.00746958, None, 0.00171644, None, 0.00746958, None, 0.00171644, None, 0.00267897, None, 0.00165018, None, 0.00267897, None, 0.00165018, None, 0.956238, None, 0.0110356, None, 0.956238, None, 0.0110356, None)
reports[-1].CovMatrix = ['0.000650613','0.000863986','-3.36241e-06','8.06948e-08','0','0','0','0','0','0.000863986','0.382253','-4.4495e-06','5.41055e-06','0','0','0','0','0','-3.36241e-06','-4.4495e-06','7.83736e-08','2.26195e-09','0','0','0','0','0','8.06948e-08','5.41055e-06','2.26195e-09','0.000252589','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030216, ("CSC", 1, 4, 2, 33), "MEp42_33"))
reports[-1].posNum = 2130
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00210788, 0.0234942, 0), \
                           ValErr(-0.112831, 0.560031, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.81188e-05, 0.000269898, 0), \
                           -2937.23, 2130, 2130, -nan)
reports[-1].sigmaresid = ValErr(0.960822, 0.0147208, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00888419, None, -0.00102662, None, -0.00134711, None, -0.00039229, None, -0.00134711, None, -0.00039229, None, -0.00569539, None, -0.000452027, None, -0.00569539, None, -0.000452027, None, 0.960841, None, 0.0124552, None, 0.960841, None, 0.0124552, None)
reports[-1].CovMatrix = ['0.00055198','4.98972e-05','-2.93857e-06','1.11925e-07','0','0','0','0','0','4.98972e-05','0.313635','7.5909e-07','5.17411e-06','0','0','0','0','0','-2.93857e-06','7.5909e-07','7.28451e-08','1.60207e-09','0','0','0','0','0','1.11925e-07','5.17411e-06','1.60207e-09','0.000216703','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030232, ("CSC", 1, 4, 2, 35), "MEp42_35"))
reports[-1].posNum = 1831
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00475639, 0.0252092, 0), \
                           ValErr(-0.063014, 0.586453, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.5681e-05, 0.000265332, 0), \
                           -2456.71, 1831, 1831, -nan)
reports[-1].sigmaresid = ValErr(0.925706, 0.0152974, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0312901, None, 0.00112893, None, -0.00592172, None, 0.00140501, None, -0.00592172, None, 0.00140501, None, 0.00715022, None, 0.000784812, None, 0.00715022, None, 0.000784812, None, 0.925703, None, 0.00991006, None, 0.925703, None, 0.00991006, None)
reports[-1].CovMatrix = ['0.000635505','0.000693628','-3.43199e-06','9.83203e-08','0','0','0','0','0','0.000693628','0.343927','-9.05637e-06','4.44133e-06','0','0','0','0','0','-3.43199e-06','-9.05637e-06','7.04011e-08','1.50112e-09','0','0','0','0','0','9.83203e-08','4.44133e-06','1.50112e-09','0.000234012','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029968, ("CSC", 1, 4, 2, 2), "MEp42_02"))
reports[-1].posNum = 2066
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0111859, 0.023376, 0), \
                           ValErr(-0.0796229, 0.573468, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000146214, 0.000258488, 0), \
                           -2841.17, 2066, 2066, -nan)
reports[-1].sigmaresid = ValErr(0.957206, 0.0148909, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0405016, None, -0.00022806, None, -0.00534923, None, 0.000214266, None, -0.00534923, None, 0.000214266, None, -0.000239837, None, 3.26495e-05, None, -0.000239837, None, 3.26495e-05, None, 0.957286, None, 0.0108953, None, 0.957286, None, 0.0108953, None)
reports[-1].CovMatrix = ['0.000546438','0.000782669','-2.61082e-06','1.31898e-07','0','0','0','0','0','0.000782669','0.328866','-5.85807e-06','5.17588e-06','0','0','0','0','0','-2.61082e-06','-5.85807e-06','6.68163e-08','1.31831e-09','0','0','0','0','0','1.31898e-07','5.17588e-06','1.31831e-09','0.000221742','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029984, ("CSC", 1, 4, 2, 4), "MEp42_04"))
reports[-1].posNum = 2060
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0112953, 0.0249613, 0), \
                           ValErr(0.293207, 0.571053, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000246678, 0.000285593, 0), \
                           -2845.39, 2060, 2060, -nan)
reports[-1].sigmaresid = ValErr(0.963019, 0.0150032, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00121341, None, -0.00199993, None, 0.000545857, None, -0.00162686, None, 0.000545857, None, -0.00162686, None, -0.00100444, None, -0.00141763, None, -0.00100444, None, -0.00141763, None, 0.963244, None, 0.00927492, None, 0.963244, None, 0.00927492, None)
reports[-1].CovMatrix = ['0.000623066','-0.00104665','-3.74116e-06','1.04524e-07','0','0','0','0','0','-0.00104665','0.326102','8.81426e-06','4.8199e-06','0','0','0','0','0','-3.74116e-06','8.81426e-06','8.15633e-08','1.50204e-09','0','0','0','0','0','1.04524e-07','4.8199e-06','1.50204e-09','0.000225099','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030000, ("CSC", 1, 4, 2, 6), "MEp42_06"))
reports[-1].posNum = 1583
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00879896, 0.0261281, 0), \
                           ValErr(-0.222051, 0.547955, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.13144e-05, 0.000299056, 0), \
                           -2171.07, 1583, 1583, -nan)
reports[-1].sigmaresid = ValErr(0.953629, 0.0169474, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0312556, None, -0.00228521, None, 0.0104716, None, -0.00208335, None, 0.0104716, None, -0.00208335, None, 0.00537249, None, -0.00220483, None, 0.00537249, None, -0.00220483, None, 0.953726, None, 0.00977181, None, 0.953726, None, 0.00977181, None)
reports[-1].CovMatrix = ['0.000682675','-0.000755892','-3.09525e-06','1.78674e-07','0','0','0','0','0','-0.000755892','0.300254','5.49704e-06','5.58253e-06','0','0','0','0','0','-3.09525e-06','5.49704e-06','8.94348e-08','1.65447e-09','0','0','0','0','0','1.78674e-07','5.58253e-06','1.65447e-09','0.000287218','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030016, ("CSC", 1, 4, 2, 8), "MEp42_08"))
reports[-1].posNum = 2146
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0216312, 0.0240768, 0), \
                           ValErr(0.0382867, 0.571703, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000165467, 0.000265967, 0), \
                           -3007.48, 2146, 2146, -nan)
reports[-1].sigmaresid = ValErr(0.982643, 0.0149989, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00896613, None, -0.00199284, None, -0.0145352, None, -0.00142336, None, -0.0145352, None, -0.00142336, None, -0.0256171, None, -0.00183854, None, -0.0256171, None, -0.00183854, None, 0.982739, None, 0.0115723, None, 0.982739, None, 0.0115723, None)
reports[-1].CovMatrix = ['0.000579694','3.24871e-05','-3.02832e-06','1.0025e-07','0','0','0','0','0','3.24871e-05','0.326844','3.53389e-06','4.96699e-06','0','0','0','0','0','-3.02832e-06','3.53389e-06','7.07386e-08','1.70305e-09','0','0','0','0','0','1.0025e-07','4.96699e-06','1.70305e-09','0.000224969','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030032, ("CSC", 1, 4, 2, 10), "MEp42_10"))
reports[-1].posNum = 2100
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00623527, 0.0237752, 0), \
                           ValErr(0.0957902, 0.5638, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000104988, 0.000268744, 0), \
                           -2958.19, 2100, 2100, -nan)
reports[-1].sigmaresid = ValErr(0.989767, 0.0152722, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0161598, None, -0.00231848, None, -0.00221672, None, -0.00231023, None, -0.00221672, None, -0.00231023, None, 0.0200241, None, -0.00262411, None, 0.0200241, None, -0.00262411, None, 0.989819, None, 0.0100966, None, 0.989819, None, 0.0100966, None)
reports[-1].CovMatrix = ['0.000565258','-0.000513021','-2.66257e-06','1.1376e-07','0','0','0','0','0','-0.000513021','0.317871','2.02306e-06','4.42917e-06','0','0','0','0','0','-2.66257e-06','2.02306e-06','7.22232e-08','1.67734e-09','0','0','0','0','0','1.1376e-07','4.42917e-06','1.67734e-09','0.000233242','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030048, ("CSC", 1, 4, 2, 12), "MEp42_12"))
reports[-1].posNum = 1892
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0103884, 0.0244291, 0), \
                           ValErr(0.226702, 0.586706, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.67244e-05, 0.000294557, 0), \
                           -2633.6, 1892, 1892, -nan)
reports[-1].sigmaresid = ValErr(0.973348, 0.0158222, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.031441, None, -0.00225986, None, -0.00974594, None, -0.00158524, None, -0.00974594, None, -0.00158524, None, 0.00362532, None, -0.00180378, None, 0.00362532, None, -0.00180378, None, 0.97343, None, 0.0121836, None, 0.97343, None, 0.0121836, None)
reports[-1].CovMatrix = ['0.000596779','0.000557412','-2.84938e-06','1.29246e-07','0','0','0','0','0','0.000557412','0.344224','1.09945e-05','4.76954e-06','0','0','0','0','0','-2.84938e-06','1.09945e-05','8.67636e-08','2.14958e-09','0','0','0','0','0','1.29246e-07','4.76954e-06','2.14958e-09','0.000250344','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030064, ("CSC", 1, 4, 2, 14), "MEp42_14"))
reports[-1].posNum = 2366
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0049714, 0.021162, 0), \
                           ValErr(-0.193517, 0.521077, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000154886, 0.000243613, 0), \
                           -3286.16, 2366, 2366, -nan)
reports[-1].sigmaresid = ValErr(0.970392, 0.0141062, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00158795, None, -8.46833e-05, None, -0.000320156, None, 0.000179354, None, -0.000320156, None, 0.000179354, None, 0.0255922, None, 0.000481289, None, 0.0255922, None, 0.000481289, None, 0.970528, None, 0.0119725, None, 0.970528, None, 0.0119725, None)
reports[-1].CovMatrix = ['0.000447831','0.00019522','-1.71688e-06','1.1621e-07','0','0','0','0','0','0.00019522','0.271521','5.81075e-07','4.76477e-06','0','0','0','0','0','-1.71688e-06','5.81075e-07','5.93471e-08','1.4493e-09','0','0','0','0','0','1.1621e-07','4.76477e-06','1.4493e-09','0.000198985','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030080, ("CSC", 1, 4, 2, 16), "MEp42_16"))
reports[-1].posNum = 2126
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.020122, 0.0226597, 0), \
                           ValErr(0.0803764, 0.540706, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000262035, 0.000255779, 0), \
                           -2897.01, 2126, 2126, -nan)
reports[-1].sigmaresid = ValErr(0.945259, 0.0144959, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0171149, None, -0.00363895, None, -0.0102137, None, -0.0032803, None, -0.0102137, None, -0.0032803, None, -0.0224366, None, -0.00377657, None, -0.0224366, None, -0.00377657, None, 0.945511, None, 0.0113542, None, 0.945511, None, 0.0113542, None)
reports[-1].CovMatrix = ['0.000513463','0.000103057','-2.46906e-06','1.12733e-07','0','0','0','0','0','0.000103057','0.292363','-3.0617e-06','3.82941e-06','0','0','0','0','0','-2.46906e-06','-3.0617e-06','6.54227e-08','1.3174e-09','0','0','0','0','0','1.12733e-07','3.82941e-06','1.3174e-09','0.000210133','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030096, ("CSC", 1, 4, 2, 18), "MEp42_18"))
reports[-1].posNum = 2214
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00501906, 0.0224926, 0), \
                           ValErr(-0.202743, 0.550965, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000124922, 0.000259391, 0), \
                           -3098.78, 2214, 2214, -nan)
reports[-1].sigmaresid = ValErr(0.980841, 0.0147392, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00522327, None, -0.00210392, None, -0.00119603, None, -0.00211219, None, -0.00119603, None, -0.00211219, None, 0.00768527, None, -0.00211183, None, 0.00768527, None, -0.00211183, None, 0.980958, None, 0.00938258, None, 0.980958, None, 0.00938258, None)
reports[-1].CovMatrix = ['0.000505917','-0.00047448','-2.18427e-06','1.07769e-07','0','0','0','0','0','-0.00047448','0.303562','2.89255e-06','5.29415e-06','0','0','0','0','0','-2.18427e-06','2.89255e-06','6.72835e-08','1.55225e-09','0','0','0','0','0','1.07769e-07','5.29415e-06','1.55225e-09','0.000217247','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030112, ("CSC", 1, 4, 2, 20), "MEp42_20"))
reports[-1].posNum = 1997
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00251047, 0.0254386, 0), \
                           ValErr(0.199256, 0.589706, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.45461e-05, 0.000273665, 0), \
                           -2831.2, 1997, 1997, -nan)
reports[-1].sigmaresid = ValErr(0.998783, 0.0158038, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00741639, None, 0.00225262, None, -0.00287529, None, 0.00212636, None, -0.00287529, None, 0.00212636, None, -0.0204879, None, 0.0020717, None, -0.0204879, None, 0.0020717, None, 0.998819, None, 0.0102493, None, 0.998819, None, 0.0102493, None)
reports[-1].CovMatrix = ['0.000647121','-0.00039823','-3.31737e-06','1.19811e-07','0','0','0','0','0','-0.00039823','0.347753','-1.69609e-06','5.17398e-06','0','0','0','0','0','-3.31737e-06','-1.69609e-06','7.48925e-08','1.67028e-09','0','0','0','0','0','1.19811e-07','5.17398e-06','1.67028e-09','0.000249763','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030128, ("CSC", 1, 4, 2, 22), "MEp42_22"))
reports[-1].posNum = 2162
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00446321, 0.0231261, 0), \
                           ValErr(-0.149989, 0.56868, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.82165e-06, 0.000255756, 0), \
                           -2986.17, 2162, 2162, -nan)
reports[-1].sigmaresid = ValErr(0.962959, 0.0146438, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.015599, None, 0.00134789, None, -0.00430209, None, 0.00110773, None, -0.00430209, None, 0.00110773, None, -0.00260986, None, 0.0014711, None, -0.00260986, None, 0.0014711, None, 0.962989, None, 0.00991821, None, 0.962989, None, 0.00991821, None)
reports[-1].CovMatrix = ['0.000534815','0.000357888','-2.62366e-06','1.07256e-07','0','0','0','0','0','0.000357888','0.323397','2.72398e-06','5.49635e-06','0','0','0','0','0','-2.62366e-06','2.72398e-06','6.54112e-08','1.66281e-09','0','0','0','0','0','1.07256e-07','5.49635e-06','1.66281e-09','0.000214444','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030144, ("CSC", 1, 4, 2, 24), "MEp42_24"))
reports[-1].posNum = 2402
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0177152, 0.0218127, 0), \
                           ValErr(-0.221433, 0.310653, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000109494, 0.000248049, 0), \
                           -3421.68, 2402, 2402, -nan)
reports[-1].sigmaresid = ValErr(1.00559, 0.0144246, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00464932, None, -0.000649796, None, -0.0144759, None, -0.000411971, None, -0.0144759, None, -0.000411971, None, -0.0202226, None, -0.000578709, None, -0.0202226, None, -0.000578709, None, 1.00566, None, 0.0108871, None, 1.00566, None, 0.0108871, None)
reports[-1].CovMatrix = ['0.000475795','0.000638481','-1.90497e-06','-2.22261e-06','0','0','0','0','0','0.000638481','0.0965051','7.30044e-06','0.000721601','0','0','0','0','0','-1.90497e-06','7.30044e-06','6.15285e-08','-3.91484e-08','0','0','0','0','0','-2.22261e-06','0.000721601','-3.91484e-08','0.000208072','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030160, ("CSC", 1, 4, 2, 26), "MEp42_26"))
reports[-1].posNum = 1999
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00522859, 0.025328, 0), \
                           ValErr(-0.438264, 0.57935, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.58304e-05, 0.000277625, 0), \
                           -2720.78, 1999, 1999, -nan)
reports[-1].sigmaresid = ValErr(0.943753, 0.0149253, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0101807, None, 0.000394396, None, -0.00222523, None, 0.000565216, None, -0.00222523, None, 0.000565216, None, 0.0269922, None, 0.000479938, None, 0.0269922, None, 0.000479938, None, 0.943922, None, 0.0108862, None, 0.943922, None, 0.0108862, None)
reports[-1].CovMatrix = ['0.000641508','-1.64941e-05','-3.88596e-06','6.77546e-08','0','0','0','0','0','-1.64941e-05','0.335646','2.30103e-06','5.33535e-06','0','0','0','0','0','-3.88596e-06','2.30103e-06','7.70757e-08','1.70141e-09','0','0','0','0','0','6.77546e-08','5.33535e-06','1.70141e-09','0.000222765','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030176, ("CSC", 1, 4, 2, 28), "MEp42_28"))
reports[-1].posNum = 2322
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.023182, 0.0220892, 0), \
                           ValErr(-0.326845, 0.547588, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.08605e-05, 0.000250935, 0), \
                           -3277.62, 2322, 2322, -nan)
reports[-1].sigmaresid = ValErr(0.992622, 0.0145656, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00268382, None, -0.00100369, None, -0.0205473, None, -0.000620935, None, -0.0205473, None, -0.000620935, None, -0.0368506, None, -0.00107983, None, -0.0368506, None, -0.00107983, None, 0.992732, None, 0.0124374, None, 0.992732, None, 0.0124374, None)
reports[-1].CovMatrix = ['0.000487934','0.000293359','-1.99444e-06','1.35088e-07','0','0','0','0','0','0.000293359','0.299852','2.09136e-06','5.72677e-06','0','0','0','0','0','-1.99444e-06','2.09136e-06','6.29686e-08','1.50404e-09','0','0','0','0','0','1.35088e-07','5.72677e-06','1.50404e-09','0.000212158','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030192, ("CSC", 1, 4, 2, 30), "MEp42_30"))
reports[-1].posNum = 1855
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00875028, 0.0269604, 0), \
                           ValErr(0.0979119, 0.584173, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.22396e-05, 0.000292554, 0), \
                           -2489.35, 1855, 1855, -nan)
reports[-1].sigmaresid = ValErr(0.925928, 0.0152018, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0132735, None, 0.000655577, None, -0.00624929, None, 0.000777101, None, -0.00624929, None, 0.000777101, None, -0.0104576, None, 0.000780277, None, -0.0104576, None, 0.000780277, None, 0.92593, None, 0.0103948, None, 0.92593, None, 0.0103948, None)
reports[-1].CovMatrix = ['0.000726862','-0.0012857','-4.74678e-06','1.43135e-07','0','0','0','0','0','-0.0012857','0.341258','1.06482e-05','5.48156e-06','0','0','0','0','0','-4.74678e-06','1.06482e-05','8.55877e-08','8.3455e-10','0','0','0','0','0','1.43135e-07','5.48156e-06','8.3455e-10','0.000231095','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030208, ("CSC", 1, 4, 2, 32), "MEp42_32"))
reports[-1].posNum = 2085
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00776618, 0.0242316, 0), \
                           ValErr(-0.231363, 0.573995, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.86504e-05, 0.000270918, 0), \
                           -2928.42, 2085, 2085, -nan)
reports[-1].sigmaresid = ValErr(0.985647, 0.0152627, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0346387, None, -0.00177161, None, 0.00339644, None, -0.00140902, None, 0.00339644, None, -0.00140902, None, 0.031202, None, -0.00160848, None, 0.031202, None, -0.00160848, None, 0.985752, None, 0.0112866, None, 0.985752, None, 0.0112866, None)
reports[-1].CovMatrix = ['0.000587168','-0.000630408','-2.97417e-06','1.44677e-07','0','0','0','0','0','-0.000630408','0.32947','3.69553e-06','6.03992e-06','0','0','0','0','0','-2.97417e-06','3.69553e-06','7.33965e-08','1.403e-09','0','0','0','0','0','1.44677e-07','6.03992e-06','1.403e-09','0.000232952','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030224, ("CSC", 1, 4, 2, 34), "MEp42_34"))
reports[-1].posNum = 2070
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00963577, 0.0233271, 0), \
                           ValErr(-0.170663, 0.5679, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.37154e-05, 0.000254764, 0), \
                           -2890.35, 2070, 2070, -nan)
reports[-1].sigmaresid = ValErr(0.977602, 0.0151933, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-9.16519e-05, None, 0.000239474, None, -0.00797168, None, 0.000579416, None, -0.00797168, None, 0.000579416, None, 0.0135183, None, 0.000498595, None, 0.0135183, None, 0.000498595, None, 0.977647, None, 0.0103576, None, 0.977647, None, 0.0103576, None)
reports[-1].CovMatrix = ['0.000544155','0.000352438','-2.3124e-06','1.20716e-07','0','0','0','0','0','0.000352438','0.322511','-5.525e-06','5.46262e-06','0','0','0','0','0','-2.3124e-06','-5.525e-06','6.49046e-08','1.62804e-09','0','0','0','0','0','1.20716e-07','5.46262e-06','1.62804e-09','0.000230837','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030240, ("CSC", 1, 4, 2, 36), "MEp42_36"))
reports[-1].posNum = 1874
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0245764, 0.0250101, 0), \
                           ValErr(-0.377966, 0.603243, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000147981, 0.000260471, 0), \
                           -2568.69, 1874, 1874, -nan)
reports[-1].sigmaresid = ValErr(0.952906, 0.015565, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0225443, None, -0.000578735, None, -0.0186231, None, -0.000402285, None, -0.0186231, None, -0.000402285, None, -0.0191732, None, -0.000472373, None, -0.0191732, None, -0.000472373, None, 0.953097, None, 0.0104515, None, 0.953097, None, 0.0104515, None)
reports[-1].CovMatrix = ['0.000625504','-0.00103482','-3.07768e-06','1.18246e-07','0','0','0','0','0','-0.00103482','0.363902','7.38352e-06','5.24621e-06','0','0','0','0','0','-3.07768e-06','7.38352e-06','6.78453e-08','1.49266e-09','0','0','0','0','0','1.18246e-07','5.24621e-06','1.49266e-09','0.000242271','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050440, ("CSC", 2, 1, 1, 1), "MEm11_01"))
reports[-1].posNum = 3009
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00168225, 0.0032329, 0), \
                           ValErr(0.051979, 0.0811768, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000135125, 8.71327e-05, 0), \
                           997.028, 3009, 3009, -nan)
reports[-1].sigmaresid = ValErr(0.173724, 0.00223941, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.003977, None, -3.97423e-05, None, 0.000621757, None, 6.90153e-05, None, 0.000621757, None, 6.90153e-05, None, 0.00431327, None, 3.16026e-06, None, 0.00431327, None, 3.16026e-06, None, 0.173804, None, 0.0065559, None, 0.173804, None, 0.0065559, None)
reports[-1].CovMatrix = ['1.04516e-05','1.03037e-05','-5.57119e-08','1.73855e-09','0','0','0','0','0','1.03037e-05','0.00658968','-1.48318e-07','5.15286e-08','0','0','0','0','0','-5.57119e-08','-1.48318e-07','7.5921e-09','4.38965e-11','0','0','0','0','0','1.73855e-09','5.15286e-08','4.38965e-11','5.01495e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050456, ("CSC", 2, 1, 1, 3), "MEm11_03"))
reports[-1].posNum = 2661
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00380697, 0.00344195, 0), \
                           ValErr(0.0366687, 0.0860647, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000128865, 9.30815e-05, 0), \
                           884.298, 2661, 2661, -nan)
reports[-1].sigmaresid = ValErr(0.173556, 0.00237903, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00058296, None, 0.000232186, None, 0.00277838, None, 0.000411005, None, 0.00277838, None, 0.000411005, None, -0.00109469, None, 0.000460705, None, -0.00109469, None, 0.000460705, None, 0.173625, None, 0.00619539, None, 0.173625, None, 0.00619539, None)
reports[-1].CovMatrix = ['1.1847e-05','4.55682e-06','-6.73553e-08','1.87732e-09','0','0','0','0','0','4.55682e-06','0.00740714','9.17759e-08','5.8693e-08','0','0','0','0','0','-6.73553e-08','9.17759e-08','8.66417e-09','5.13138e-11','0','0','0','0','0','1.87732e-09','5.8693e-08','5.13138e-11','5.6598e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050472, ("CSC", 2, 1, 1, 5), "MEm11_05"))
reports[-1].posNum = 2944
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00331113, 0.00322543, 0), \
                           ValErr(0.0605408, 0.0812816, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00012693, 8.6081e-05, 0), \
                           994.511, 2944, 2944, -nan)
reports[-1].sigmaresid = ValErr(0.172605, 0.00224942, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000416466, None, -6.79426e-05, None, 0.00258903, None, 3.47575e-05, None, 0.00258903, None, 3.47575e-05, None, 0.00451441, None, -0.00015918, None, 0.00451441, None, -0.00015918, None, 0.172685, None, 0.00564097, None, 0.172685, None, 0.00564097, None)
reports[-1].CovMatrix = ['1.04034e-05','-5.69627e-06','-4.53855e-08','1.6809e-09','0','0','0','0','0','-5.69627e-06','0.0066067','-6.97217e-08','4.95067e-08','0','0','0','0','0','-4.53855e-08','-6.97217e-08','7.40994e-09','4.63462e-11','0','0','0','0','0','1.6809e-09','4.95067e-08','4.63462e-11','5.05988e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050488, ("CSC", 2, 1, 1, 7), "MEm11_07"))
reports[-1].posNum = 2264
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00408325, 0.00384297, 0), \
                           ValErr(-0.0972082, 0.0949541, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000187368, 0.000105259, 0), \
                           647.096, 2264, 2264, -nan)
reports[-1].sigmaresid = ValErr(0.181819, 0.00270204, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00467856, None, 0.000440488, None, 0.00328146, None, -0.000139037, None, 0.00328146, None, -0.000139037, None, 0.0086681, None, 8.10328e-05, None, 0.0086681, None, 8.10328e-05, None, 0.181981, None, 0.00575076, None, 0.181981, None, 0.00575076, None)
reports[-1].CovMatrix = ['1.47685e-05','-1.0639e-05','-4.16741e-08','2.31423e-09','0','0','0','0','0','-1.0639e-05','0.00901628','2.90892e-07','6.64663e-08','0','0','0','0','0','-4.16741e-08','2.90892e-07','1.10795e-08','6.71406e-11','0','0','0','0','0','2.31423e-09','6.64663e-08','6.71406e-11','7.30102e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050504, ("CSC", 2, 1, 1, 9), "MEm11_09"))
reports[-1].posNum = 2783
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00545351, 0.00324724, 0), \
                           ValErr(0.0110937, 0.0815387, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000169187, 8.72521e-05, 0), \
                           1027.89, 2783, 2783, -nan)
reports[-1].sigmaresid = ValErr(0.167246, 0.00224173, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00422734, None, 0.000338404, None, 0.00411461, None, 0.000440406, None, 0.00411461, None, 0.000440406, None, 0.00383306, None, 0.000254961, None, 0.00383306, None, 0.000254961, None, 0.167361, None, 0.0057359, None, 0.167361, None, 0.0057359, None)
reports[-1].CovMatrix = ['1.05446e-05','-8.20773e-06','-6.10122e-08','1.58357e-09','0','0','0','0','0','-8.20773e-06','0.00664856','3.21561e-07','5.16215e-08','0','0','0','0','0','-6.10122e-08','3.21561e-07','7.61292e-09','4.87646e-11','0','0','0','0','0','1.58357e-09','5.16215e-08','4.87646e-11','5.02537e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050520, ("CSC", 2, 1, 1, 11), "MEm11_11"))
reports[-1].posNum = 2738
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00476944, 0.00329695, 0), \
                           ValErr(-0.000714336, 0.0818439, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000112482, 8.67637e-05, 0), \
                           1023.36, 2738, 2738, -nan)
reports[-1].sigmaresid = ValErr(0.16651, 0.00225012, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00266299, None, -0.00186734, None, 0.00365215, None, -0.00203655, None, 0.00365215, None, -0.00203655, None, 0.0028626, None, -0.00185018, None, 0.0028626, None, -0.00185018, None, 0.166561, None, 0.00585705, None, 0.166561, None, 0.00585705, None)
reports[-1].CovMatrix = ['1.08699e-05','3.06116e-06','-7.48074e-08','1.7318e-09','0','0','0','0','0','3.06116e-06','0.00669843','-1.50681e-07','5.60969e-08','0','0','0','0','0','-7.48074e-08','-1.50681e-07','7.52795e-09','4.34544e-11','0','0','0','0','0','1.7318e-09','5.60969e-08','4.34544e-11','5.06305e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050536, ("CSC", 2, 1, 1, 13), "MEm11_13"))
reports[-1].posNum = 2600
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00189239, 0.00355535, 0), \
                           ValErr(0.0184883, 0.0887901, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000136565, 9.57832e-05, 0), \
                           791.504, 2600, 2600, -nan)
reports[-1].sigmaresid = ValErr(0.178465, 0.00247485, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00765603, None, -0.002079, None, 0.00099112, None, -0.00210784, None, 0.00099112, None, -0.00210784, None, -0.00411562, None, -0.00204177, None, -0.00411562, None, -0.00204177, None, 0.178536, None, 0.0060059, None, 0.178536, None, 0.0060059, None)
reports[-1].CovMatrix = ['1.26405e-05','6.05418e-06','-5.94602e-08','2.06138e-09','0','0','0','0','0','6.05418e-06','0.00788369','6.26329e-08','6.09195e-08','0','0','0','0','0','-5.94602e-08','6.26329e-08','9.17443e-09','5.25163e-11','0','0','0','0','0','2.06138e-09','6.09195e-08','5.25163e-11','6.12489e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050552, ("CSC", 2, 1, 1, 15), "MEm11_15"))
reports[-1].posNum = 2250
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00432, 0.00374848, 0), \
                           ValErr(-0.014836, 0.0931954, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000178084, 9.96979e-05, 0), \
                           799.922, 2250, 2250, -nan)
reports[-1].sigmaresid = ValErr(0.169572, 0.00252779, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00256373, None, 0.000371193, None, 0.00230679, None, 0.000196768, None, 0.00230679, None, 0.000196768, None, -0.00565584, None, 0.000214969, None, -0.00565584, None, 0.000214969, None, 0.169696, None, 0.0055431, None, 0.169696, None, 0.0055431, None)
reports[-1].CovMatrix = ['1.40511e-05','-1.48872e-06','-1.12392e-07','2.20321e-09','0','0','0','0','0','-1.48872e-06','0.00868539','2.8394e-07','7.54249e-08','0','0','0','0','0','-1.12392e-07','2.8394e-07','9.93968e-09','4.89612e-11','0','0','0','0','0','2.20321e-09','7.54249e-08','4.89612e-11','6.38971e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050568, ("CSC", 2, 1, 1, 17), "MEm11_17"))
reports[-1].posNum = 2010
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00330476, 0.00379056, 0), \
                           ValErr(0.112208, 0.0936198, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.00749e-05, 0.000100578, 0), \
                           731.41, 2010, 2010, -nan)
reports[-1].sigmaresid = ValErr(0.168163, 0.00265226, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00447456, None, -0.000998694, None, 0.00281369, None, -0.000935287, None, 0.00281369, None, -0.000935287, None, 0.000150355, None, -0.000934436, None, 0.000150355, None, -0.000934436, None, 0.168252, None, 0.00555485, None, 0.168252, None, 0.00555485, None)
reports[-1].CovMatrix = ['1.43684e-05','2.88299e-06','-5.48319e-08','2.58094e-09','0','0','0','0','0','2.88299e-06','0.00876466','2.74358e-07','7.57469e-08','0','0','0','0','0','-5.48319e-08','2.74358e-07','1.01158e-08','7.03922e-11','0','0','0','0','0','2.58094e-09','7.57469e-08','7.03922e-11','7.03448e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050584, ("CSC", 2, 1, 1, 19), "MEm11_19"))
reports[-1].posNum = 2540
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00105092, 0.00338065, 0), \
                           ValErr(-0.0336022, 0.0866193, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.03735e-05, 9.51825e-05, 0), \
                           909.64, 2540, 2540, -nan)
reports[-1].sigmaresid = ValErr(0.169134, 0.00237301, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(9.39137e-06, None, -0.00529498, None, 0.000730482, None, -0.00514523, None, 0.000730482, None, -0.00514523, None, 0.00112328, None, -0.00526652, None, 0.00112328, None, -0.00526652, None, 0.169154, None, 0.00476693, None, 0.169154, None, 0.00476693, None)
reports[-1].CovMatrix = ['1.14288e-05','-1.77157e-05','-3.11698e-08','1.99269e-09','0','0','0','0','0','-1.77157e-05','0.00750291','-9.36938e-07','4.98813e-08','0','0','0','0','0','-3.11698e-08','-9.36938e-07','9.05971e-09','5.28141e-11','0','0','0','0','0','1.99269e-09','4.98813e-08','5.28141e-11','5.63117e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050600, ("CSC", 2, 1, 1, 21), "MEm11_21"))
reports[-1].posNum = 2772
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00388837, 0.00330843, 0), \
                           ValErr(-0.0443632, 0.0831325, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000145371, 8.94969e-05, 0), \
                           945.743, 2772, 2772, -nan)
reports[-1].sigmaresid = ValErr(0.172025, 0.00231036, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00302985, None, -0.00471159, None, 0.00304091, None, -0.00452618, None, 0.00304091, None, -0.00452618, None, 0.00341027, None, -0.0044695, None, 0.00341027, None, -0.0044695, None, 0.172116, None, 0.00639095, None, 0.172116, None, 0.00639095, None)
reports[-1].CovMatrix = ['1.09457e-05','-4.86378e-07','-4.65127e-08','1.83397e-09','0','0','0','0','0','-4.86378e-07','0.00691101','-1.22906e-08','5.52114e-08','0','0','0','0','0','-4.65127e-08','-1.22906e-08','8.0097e-09','5.07098e-11','0','0','0','0','0','1.83397e-09','5.52114e-08','5.07098e-11','5.33776e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050616, ("CSC", 2, 1, 1, 23), "MEm11_23"))
reports[-1].posNum = 2641
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00265401, 0.00340246, 0), \
                           ValErr(-0.0337025, 0.0859525, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000108811, 9.24207e-05, 0), \
                           892.915, 2641, 2641, -nan)
reports[-1].sigmaresid = ValErr(0.172555, 0.00237426, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00139229, None, -0.00122294, None, 0.00201314, None, -0.00126547, None, 0.00201314, None, -0.00126547, None, -0.00352917, None, -0.00126055, None, -0.00352917, None, -0.00126055, None, 0.172605, None, 0.00541866, None, 0.172605, None, 0.00541866, None)
reports[-1].CovMatrix = ['1.15768e-05','3.68146e-07','-5.08052e-08','1.94125e-09','0','0','0','0','0','3.68146e-07','0.00738783','1.83958e-07','5.98238e-08','0','0','0','0','0','-5.08052e-08','1.83958e-07','8.54158e-09','5.46657e-11','0','0','0','0','0','1.94125e-09','5.98238e-08','5.46657e-11','5.63713e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050632, ("CSC", 2, 1, 1, 25), "MEm11_25"))
reports[-1].posNum = 2890
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00443616, 0.00319553, 0), \
                           ValErr(0.0250312, 0.080757, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.98477e-05, 8.54013e-05, 0), \
                           1058.84, 2890, 2890, -nan)
reports[-1].sigmaresid = ValErr(0.167743, 0.00220637, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00567063, None, 0.00368576, None, 0.00371941, None, 0.00378939, None, 0.00371941, None, 0.00378939, None, 0.00563393, None, 0.00379228, None, 0.00563393, None, 0.00379228, None, 0.167779, None, 0.0050626, None, 0.167779, None, 0.0050626, None)
reports[-1].CovMatrix = ['1.02114e-05','-3.89165e-06','-5.88339e-08','1.65608e-09','0','0','0','0','0','-3.89165e-06','0.00652169','2.40609e-07','5.08602e-08','0','0','0','0','0','-5.88339e-08','2.40609e-07','7.29337e-09','4.75678e-11','0','0','0','0','0','1.65608e-09','5.08602e-08','4.75678e-11','4.86808e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050648, ("CSC", 2, 1, 1, 27), "MEm11_27"))
reports[-1].posNum = 2612
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00156862, 0.00334665, 0), \
                           ValErr(0.00963283, 0.084159, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000113048, 8.9769e-05, 0), \
                           963.288, 2612, 2612, -nan)
reports[-1].sigmaresid = ValErr(0.167339, 0.00231524, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0031857, None, -9.03666e-05, None, 0.000694313, None, 6.58176e-05, None, 0.000694313, None, 6.58176e-05, None, 0.000805512, None, 9.45423e-05, None, 0.000805512, None, 9.45423e-05, None, 0.16739, None, 0.00611069, None, 0.16739, None, 0.00611069, None)
reports[-1].CovMatrix = ['1.12e-05','5.58412e-06','-6.19575e-08','1.91052e-09','0','0','0','0','0','5.58412e-06','0.00708273','-1.25453e-07','5.81104e-08','0','0','0','0','0','-6.19575e-08','-1.25453e-07','8.05847e-09','4.87779e-11','0','0','0','0','0','1.91052e-09','5.81104e-08','4.87779e-11','5.36033e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050664, ("CSC", 2, 1, 1, 29), "MEm11_29"))
reports[-1].posNum = 2805
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00129471, 0.00332566, 0), \
                           ValErr(0.0686555, 0.0828786, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000101875, 8.6739e-05, 0), \
                           936.973, 2805, 2805, -nan)
reports[-1].sigmaresid = ValErr(0.173258, 0.00231319, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00416176, None, 0.000776118, None, 0.000533556, None, 0.000844386, None, 0.000533556, None, 0.000844386, None, -0.0111946, None, 0.000761432, None, -0.0111946, None, 0.000761432, None, 0.173321, None, 0.00535934, None, 0.173321, None, 0.00535934, None)
reports[-1].CovMatrix = ['1.106e-05','6.65658e-06','-5.14782e-08','1.85573e-09','0','0','0','0','0','6.65658e-06','0.00686886','-2.8225e-08','5.43993e-08','0','0','0','0','0','-5.14782e-08','-2.8225e-08','7.52366e-09','4.71181e-11','0','0','0','0','0','1.85573e-09','5.43993e-08','4.71181e-11','5.35085e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050680, ("CSC", 2, 1, 1, 31), "MEm11_31"))
reports[-1].posNum = 2731
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(2.47875e-05, 0.00328758, 0), \
                           ValErr(0.0476149, 0.0821182, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000133293, 8.90287e-05, 0), \
                           1004.42, 2731, 2731, -nan)
reports[-1].sigmaresid = ValErr(0.167508, 0.00226651, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00322673, None, -0.000301637, None, -0.00108158, None, -0.000324354, None, -0.00108158, None, -0.000324354, None, 0.00359293, None, -0.000271048, None, 0.00359293, None, -0.000271048, None, 0.167585, None, 0.00563929, None, 0.167585, None, 0.00563929, None)
reports[-1].CovMatrix = ['1.08082e-05','4.33224e-06','-6.50227e-08','1.79836e-09','0','0','0','0','0','4.33224e-06','0.0067434','-2.8233e-07','5.04165e-08','0','0','0','0','0','-6.50227e-08','-2.8233e-07','7.92612e-09','4.52412e-11','0','0','0','0','0','1.79836e-09','5.04165e-08','4.52412e-11','5.13705e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050696, ("CSC", 2, 1, 1, 33), "MEm11_33"))
reports[-1].posNum = 2814
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00147568, 0.00329763, 0), \
                           ValErr(0.0419441, 0.0830332, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000175792, 8.80841e-05, 0), \
                           975.034, 2814, 2814, -nan)
reports[-1].sigmaresid = ValErr(0.171113, 0.0022809, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00191974, None, 0.000589696, None, 9.27267e-05, None, 0.000747479, None, 9.27267e-05, None, 0.000747479, None, 0.00362361, None, 0.000705302, None, 0.00362361, None, 0.000705302, None, 0.171239, None, 0.00579425, None, 0.171239, None, 0.00579425, None)
reports[-1].CovMatrix = ['1.08744e-05','6.32231e-06','-6.02186e-08','1.79712e-09','0','0','0','0','0','6.32231e-06','0.00689451','-3.34972e-07','5.23801e-08','0','0','0','0','0','-6.02186e-08','-3.34972e-07','7.7588e-09','4.46218e-11','0','0','0','0','0','1.79712e-09','5.23801e-08','4.46218e-11','5.20249e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050712, ("CSC", 2, 1, 1, 35), "MEm11_35"))
reports[-1].posNum = 2632
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00391142, 0.00336497, 0), \
                           ValErr(0.00194317, 0.0832212, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00017788, 8.98261e-05, 0), \
                           946.82, 2632, 2632, -nan)
reports[-1].sigmaresid = ValErr(0.168862, 0.00232742, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00196295, None, -0.000493217, None, 0.00252663, None, -0.000334907, None, 0.00252663, None, -0.000334907, None, -0.00401667, None, -0.000162384, None, -0.00401667, None, -0.000162384, None, 0.168988, None, 0.00573173, None, 0.168988, None, 0.00573173, None)
reports[-1].CovMatrix = ['1.1323e-05','-1.06231e-06','-6.28311e-08','1.82889e-09','0','0','0','0','0','-1.06231e-06','0.00692577','1.08233e-07','5.68403e-08','0','0','0','0','0','-6.28311e-08','1.08233e-07','8.06872e-09','5.1103e-11','0','0','0','0','0','1.82889e-09','5.68403e-08','5.1103e-11','5.41687e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050448, ("CSC", 2, 1, 1, 2), "MEm11_02"))
reports[-1].posNum = 2958
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00449689, 0.00354584, 0), \
                           ValErr(0.048273, 0.0722837, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.75288e-05, 9.34313e-05, 0), \
                           1392.12, 2958, 2958, -nan)
reports[-1].sigmaresid = ValErr(0.151137, 0.00196758, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00417311, None, 0.00171465, None, 0.00371449, None, 0.00204004, None, 0.00371449, None, 0.00204004, None, 0.00408298, None, 0.00188978, None, 0.00408298, None, 0.00188978, None, 0.15119, None, 0.00866751, None, 0.15119, None, 0.00866751, None)
reports[-1].CovMatrix = ['1.2573e-05','-1.58928e-05','-1.646e-07','1.94301e-07','0','0','0','0','0','-1.58928e-05','0.00522493','1.98101e-07','-5.08755e-07','0','0','0','0','0','-1.646e-07','1.98101e-07','8.7294e-09','-5.06871e-09','0','0','0','0','0','1.94301e-07','-5.08755e-07','-5.06871e-09','3.87139e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050464, ("CSC", 2, 1, 1, 4), "MEm11_04"))
reports[-1].posNum = 2557
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00269613, 0.00319448, 0), \
                           ValErr(-0.011899, 0.112322, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.1567e-05, 8.56907e-05, 0), \
                           1143.07, 2557, 2557, -nan)
reports[-1].sigmaresid = ValErr(0.154745, 0.00217582, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00648922, None, 0.00208149, None, 0.00195587, None, 0.0020789, None, 0.00195587, None, 0.0020789, None, 0.0018959, None, 0.00212598, None, 0.0018959, None, 0.00212598, None, 0.154781, None, 0.00528417, None, 0.154781, None, 0.00528417, None)
reports[-1].CovMatrix = ['1.02047e-05','-4.84446e-05','-6.4859e-08','-1.33954e-07','0','0','0','0','0','-4.84446e-05','0.0126162','8.48549e-07','1.83476e-05','0','0','0','0','0','-6.4859e-08','8.48549e-07','7.3429e-09','2.37098e-09','0','0','0','0','0','-1.33954e-07','1.83476e-05','2.37098e-09','4.7342e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050480, ("CSC", 2, 1, 1, 6), "MEm11_06"))
reports[-1].posNum = 2870
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00215034, 0.00293634, 0), \
                           ValErr(0.0593617, 0.110888, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000138165, 7.94613e-05, 0), \
                           1300.42, 2870, 2870, -nan)
reports[-1].sigmaresid = ValErr(0.153809, 0.00203563, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00258183, None, 0.00128004, None, 0.00126804, None, 0.00148455, None, 0.00126804, None, 0.00148455, None, 0.00274501, None, 0.00166073, None, 0.00274501, None, 0.00166073, None, 0.153908, None, 0.00615217, None, 0.153908, None, 0.00615217, None)
reports[-1].CovMatrix = ['8.62208e-06','-2.26652e-05','-4.12089e-08','5.04624e-09','0','0','0','0','0','-2.26652e-05','0.0122962','1.06736e-06','1.31255e-06','0','0','0','0','0','-4.12089e-08','1.06736e-06','6.3141e-09','3.28132e-10','0','0','0','0','0','5.04624e-09','1.31255e-06','3.28132e-10','4.1438e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050496, ("CSC", 2, 1, 1, 8), "MEm11_08"))
reports[-1].posNum = 2761
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00521161, 0.00292682, 0), \
                           ValErr(0.0714774, 0.116153, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000183952, 8.07613e-05, 0), \
                           1332.12, 2761, 2761, -nan)
reports[-1].sigmaresid = ValErr(0.149356, 0.00202437, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000506595, None, 0.000506599, None, 0.00348696, None, 0.000408712, None, 0.00348696, None, 0.000408712, None, -0.00236641, None, 0.000489414, None, -0.00236641, None, 0.000489414, None, 0.149537, None, 0.00672423, None, 0.149537, None, 0.00672423, None)
reports[-1].CovMatrix = ['8.56629e-06','-1.07908e-06','-5.39121e-08','-3.11426e-09','0','0','0','0','0','-1.07908e-06','0.0134916','2.29147e-06','2.64728e-07','0','0','0','0','0','-5.39121e-08','2.29147e-06','6.52239e-09','-4.17823e-11','0','0','0','0','0','-3.11426e-09','2.64728e-07','-4.17823e-11','4.09807e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050512, ("CSC", 2, 1, 1, 10), "MEm11_10"))
reports[-1].posNum = 2805
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00241506, 0.00293459, 0), \
                           ValErr(0.0419281, 0.111489, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.82848e-05, 7.99599e-05, 0), \
                           1290.37, 2805, 2805, -nan)
reports[-1].sigmaresid = ValErr(0.152747, 0.00206438, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000149675, None, 0.000495713, None, 0.00179512, None, 0.000723542, None, 0.00179512, None, 0.000723542, None, 0.00581986, None, 0.000381926, None, 0.00581986, None, 0.000381926, None, 0.152792, None, 0.00935244, None, 0.152792, None, 0.00935244, None)
reports[-1].CovMatrix = ['8.61185e-06','3.66749e-06','-4.25619e-08','-1.22917e-10','0','0','0','0','0','3.66749e-06','0.0124297','9.85354e-07','2.3205e-06','0','0','0','0','0','-4.25619e-08','9.85354e-07','6.39358e-09','7.16189e-10','0','0','0','0','0','-1.22917e-10','2.3205e-06','7.16189e-10','4.26169e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050528, ("CSC", 2, 1, 1, 12), "MEm11_12"))
reports[-1].posNum = 2934
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00302264, 0.00290031, 0), \
                           ValErr(0.0156242, 0.110141, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000123689, 7.56303e-05, 0), \
                           1356.92, 2934, 2934, -nan)
reports[-1].sigmaresid = ValErr(0.152371, 0.00203891, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00255266, None, -0.000539838, None, 0.00211526, None, -0.000350811, None, 0.00211526, None, -0.000350811, None, 0.00390938, None, -0.00043942, None, 0.00390938, None, -0.00043942, None, 0.152444, None, 0.00776664, None, 0.152444, None, 0.00776664, None)
reports[-1].CovMatrix = ['8.4118e-06','-3.84255e-05','-4.1132e-08','-2.6766e-08','0','0','0','0','0','-3.84255e-05','0.0121311','-2.66629e-07','3.67381e-07','0','0','0','0','0','-4.1132e-08','-2.66629e-07','5.71994e-09','1.49691e-09','0','0','0','0','0','-2.6766e-08','3.67381e-07','1.49691e-09','4.15716e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050544, ("CSC", 2, 1, 1, 14), "MEm11_14"))
reports[-1].posNum = 2950
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000471887, 0.00293601, 0), \
                           ValErr(-0.0347122, 0.0724201, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.14199e-05, 7.77484e-05, 0), \
                           1303.93, 2950, 2950, -nan)
reports[-1].sigmaresid = ValErr(0.155525, 0.00202477, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00279078, None, -0.000838141, None, -0.00120007, None, -0.000697262, None, -0.00120007, None, -0.000697262, None, 0.0078857, None, -0.000632886, None, 0.0078857, None, -0.000632886, None, 0.155568, None, 0.00616737, None, 0.155568, None, 0.00616737, None)
reports[-1].CovMatrix = ['8.62015e-06','5.18526e-06','-5.02105e-08','1.54249e-09','0','0','0','0','0','5.18526e-06','0.00524467','-9.16977e-08','4.88536e-08','0','0','0','0','0','-5.02105e-08','-9.16977e-08','6.04481e-09','4.12533e-11','0','0','0','0','0','1.54249e-09','4.88536e-08','4.12533e-11','4.09969e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050560, ("CSC", 2, 1, 1, 16), "MEm11_16"))
reports[-1].posNum = 2586
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00432139, 0.00310737, 0), \
                           ValErr(0.0456492, 0.117696, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000138114, 7.96805e-05, 0), \
                           1195.28, 2586, 2586, -nan)
reports[-1].sigmaresid = ValErr(0.152414, 0.00214111, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000463445, None, -0.0010522, None, 0.0029784, None, -0.00113781, None, 0.0029784, None, -0.00113781, None, 0.000708142, None, -0.00111586, None, 0.000708142, None, -0.00111586, None, 0.152514, None, 0.00572119, None, 0.152514, None, 0.00572119, None)
reports[-1].CovMatrix = ['9.65573e-06','-2.41178e-05','-6.27011e-08','-7.02787e-09','0','0','0','0','0','-2.41178e-05','0.0138524','4.68986e-07','2.54394e-06','0','0','0','0','0','-6.27011e-08','4.68986e-07','6.34899e-09','5.07936e-10','0','0','0','0','0','-7.02787e-09','2.54394e-06','5.07936e-10','4.58434e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050576, ("CSC", 2, 1, 1, 18), "MEm11_18"))
reports[-1].posNum = 3071
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00381964, 0.00282575, 0), \
                           ValErr(0.00747259, 0.109051, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.51493e-05, 7.5427e-05, 0), \
                           1396.51, 3071, 3071, -nan)
reports[-1].sigmaresid = ValErr(0.153557, 0.00197426, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00079894, None, -0.00204476, None, 0.00311958, None, -0.00188603, None, 0.00311958, None, -0.00188603, None, 0.0049934, None, -0.00200906, None, 0.0049934, None, -0.00200906, None, 0.153598, None, 0.0066506, None, 0.153598, None, 0.0066506, None)
reports[-1].CovMatrix = ['7.98488e-06','8.56564e-06','-4.0641e-08','-1.83475e-09','0','0','0','0','0','8.56564e-06','0.011892','6.34195e-07','7.61796e-08','0','0','0','0','0','-4.0641e-08','6.34195e-07','5.68923e-09','-1.41657e-10','0','0','0','0','0','-1.83475e-09','7.61796e-08','-1.41657e-10','3.89772e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050592, ("CSC", 2, 1, 1, 20), "MEm11_20"))
reports[-1].posNum = 2872
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00620042, 0.00367432, 0), \
                           ValErr(-0.0206642, 0.0756728, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000134476, 9.18532e-05, 0), \
                           1356.59, 2872, 2872, -nan)
reports[-1].sigmaresid = ValErr(0.150877, 0.00199174, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00602865, None, 0.00144423, None, 0.00505592, None, 0.00137527, None, 0.00505592, None, 0.00137527, None, 0.00351003, None, 0.0014683, None, 0.00351003, None, 0.0014683, None, 0.150962, None, 0.00538397, None, 0.150962, None, 0.00538397, None)
reports[-1].CovMatrix = ['1.35006e-05','-2.47006e-05','-1.66537e-07','7.43328e-08','0','0','0','0','0','-2.47006e-05','0.00572637','4.35561e-07','-3.71771e-07','0','0','0','0','0','-1.66537e-07','4.35561e-07','8.43701e-09','-1.6486e-09','0','0','0','0','0','7.43328e-08','-3.71771e-07','-1.6486e-09','3.96705e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050608, ("CSC", 2, 1, 1, 22), "MEm11_22"))
reports[-1].posNum = 2905
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000755999, 0.0029653, 0), \
                           ValErr(0.00480497, 0.110462, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.22301e-05, 7.98862e-05, 0), \
                           1349.7, 2905, 2905, -nan)
reports[-1].sigmaresid = ValErr(0.152047, 0.00214597, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00130701, None, -0.00167079, None, 0.000245654, None, -0.00138685, None, 0.000245654, None, -0.00138685, None, -0.00582312, None, -0.0015034, None, -0.00582312, None, -0.0015034, None, 0.152066, None, 0.00623662, None, 0.152066, None, 0.00623662, None)
reports[-1].CovMatrix = ['8.793e-06','-2.67211e-06','-6.22701e-08','-5.12323e-07','0','0','0','0','0','-2.67211e-06','0.0122018','3.76245e-07','2.20226e-07','0','0','0','0','0','-6.22701e-08','3.76245e-07','6.3818e-09','1.63157e-08','0','0','0','0','0','-5.12323e-07','2.20226e-07','1.63157e-08','4.60519e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050624, ("CSC", 2, 1, 1, 24), "MEm11_24"))
reports[-1].posNum = 2972
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0035056, 0.0029178, 0), \
                           ValErr(-0.00743113, 0.10793, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000129615, 7.59002e-05, 0), \
                           1335.49, 2972, 2972, -nan)
reports[-1].sigmaresid = ValErr(0.154386, 0.00200544, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00663255, None, -0.000452017, None, 0.00264505, None, -0.000234371, None, 0.00264505, None, -0.000234371, None, 0.00162514, None, -0.000405323, None, 0.00162514, None, -0.000405323, None, 0.154463, None, 0.00632151, None, 0.154463, None, 0.00632151, None)
reports[-1].CovMatrix = ['8.51357e-06','3.50125e-05','-4.13959e-08','9.75243e-09','0','0','0','0','0','3.50125e-05','0.0116489','-5.01428e-07','3.45589e-07','0','0','0','0','0','-4.13959e-08','-5.01428e-07','5.76084e-09','-4.71678e-11','0','0','0','0','0','9.75243e-09','3.45589e-07','-4.71678e-11','4.0218e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050640, ("CSC", 2, 1, 1, 26), "MEm11_26"))
reports[-1].posNum = 2927
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000194312, 0.00297499, 0), \
                           ValErr(0.0336421, 0.0748145, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.46961e-05, 7.89226e-05, 0), \
                           1251.03, 2927, 2927, -nan)
reports[-1].sigmaresid = ValErr(0.15781, 0.00206252, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00147578, None, -0.000969337, None, -0.000291833, None, -0.000911635, None, -0.000291833, None, -0.000911635, None, -0.00382269, None, -0.00104251, None, -0.00382269, None, -0.00104251, None, 0.157836, None, 0.00657959, None, 0.157836, None, 0.00657959, None)
reports[-1].CovMatrix = ['8.85058e-06','1.84932e-06','-4.61545e-08','1.62666e-09','0','0','0','0','0','1.84932e-06','0.00559721','-9.79623e-08','5.2006e-08','0','0','0','0','0','-4.61545e-08','-9.79623e-08','6.22878e-09','4.24865e-11','0','0','0','0','0','1.62666e-09','5.2006e-08','4.24865e-11','4.25399e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050656, ("CSC", 2, 1, 1, 28), "MEm11_28"))
reports[-1].posNum = 2847
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00172316, 0.00309892, 0), \
                           ValErr(-0.0384081, 0.105464, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000101985, 7.97083e-05, 0), \
                           1291.23, 2847, 2847, -nan)
reports[-1].sigmaresid = ValErr(0.153742, 0.00204353, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00249138, None, 0.000967511, None, 0.000883073, None, 0.00105752, None, 0.000883073, None, 0.00105752, None, 0.00753204, None, 0.000897467, None, 0.00753204, None, 0.000897467, None, 0.153798, None, 0.00585212, None, 0.153798, None, 0.00585212, None)
reports[-1].CovMatrix = ['9.60332e-06','-6.50021e-05','-6.96248e-08','4.31901e-08','0','0','0','0','0','-6.50021e-05','0.0111227','1.43928e-06','-2.70242e-06','0','0','0','0','0','-6.96248e-08','1.43928e-06','6.35341e-09','-6.08901e-10','0','0','0','0','0','4.31901e-08','-2.70242e-06','-6.08901e-10','4.17603e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050672, ("CSC", 2, 1, 1, 30), "MEm11_30"))
reports[-1].posNum = 2550
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00274121, 0.00318612, 0), \
                           ValErr(0.0236455, 0.0819235, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000185528, 8.27507e-05, 0), \
                           1126.11, 2550, 2550, -nan)
reports[-1].sigmaresid = ValErr(0.155586, 0.00217863, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000361562, None, 0.00155354, None, 0.00103628, None, 0.001697, None, 0.00103628, None, 0.001697, None, 0.0091127, None, 0.00150617, None, 0.0091127, None, 0.00150617, None, 0.155741, None, 0.00609525, None, 0.155741, None, 0.00609525, None)
reports[-1].CovMatrix = ['1.01513e-05','3.13421e-05','-6.10647e-08','2.06588e-09','0','0','0','0','0','3.13421e-05','0.00671146','-4.21621e-07','6.20082e-08','0','0','0','0','0','-6.10647e-08','-4.21621e-07','6.84767e-09','4.27477e-11','0','0','0','0','0','2.06588e-09','6.20082e-08','4.27477e-11','4.74644e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050688, ("CSC", 2, 1, 1, 32), "MEm11_32"))
reports[-1].posNum = 2697
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00343578, 0.00294622, 0), \
                           ValErr(0.00307131, 0.116634, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000224113, 7.66065e-05, 0), \
                           1300.26, 2697, 2697, -nan)
reports[-1].sigmaresid = ValErr(0.14941, 0.00204764, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00131427, None, 0.00103969, None, 0.00179987, None, 0.00120652, None, 0.00179987, None, 0.00120652, None, -0.00247969, None, 0.00129342, None, -0.00247969, None, 0.00129342, None, 0.149648, None, 0.00594135, None, 0.149648, None, 0.00594135, None)
reports[-1].CovMatrix = ['8.6802e-06','-2.55477e-05','-4.34181e-08','-3.02431e-09','0','0','0','0','0','-2.55477e-05','0.0136036','1.02169e-07','-6.20674e-07','0','0','0','0','0','-4.34181e-08','1.02169e-07','5.86855e-09','-1.35191e-10','0','0','0','0','0','-3.02431e-09','-6.20674e-07','-1.35191e-10','4.19284e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050704, ("CSC", 2, 1, 1, 34), "MEm11_34"))
reports[-1].posNum = 2731
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00242631, 0.00295522, 0), \
                           ValErr(0.0110271, 0.112682, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000194875, 7.78645e-05, 0), \
                           1275.6, 2731, 2731, -nan)
reports[-1].sigmaresid = ValErr(0.151671, 0.00211404, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(6.56113e-05, None, 0.00156092, None, 0.00118852, None, 0.00166303, None, 0.00118852, None, 0.00166303, None, -0.00675242, None, 0.00164299, None, -0.00675242, None, 0.00164299, None, 0.151851, None, 0.00661125, None, 0.151851, None, 0.00661125, None)
reports[-1].CovMatrix = ['8.73333e-06','2.38356e-05','-3.65165e-08','-2.38129e-08','0','0','0','0','0','2.38356e-05','0.0126973','6.24685e-07','5.49803e-08','0','0','0','0','0','-3.65165e-08','6.24685e-07','6.06288e-09','2.09402e-09','0','0','0','0','0','-2.38129e-08','5.49803e-08','2.09402e-09','4.46918e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050720, ("CSC", 2, 1, 1, 36), "MEm11_36"))
reports[-1].posNum = 2702
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00420978, 0.0030376, 0), \
                           ValErr(0.017858, 0.0761711, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.64271e-05, 8.04685e-05, 0), \
                           1199.93, 2702, 2702, -nan)
reports[-1].sigmaresid = ValErr(0.155206, 0.00211136, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000541783, None, 0.00139841, None, 0.00360876, None, 0.00145731, None, 0.00360876, None, 0.00145731, None, 0.00287437, None, 0.00154019, None, 0.00287437, None, 0.00154019, None, 0.155237, None, 0.0055345, None, 0.155237, None, 0.0055345, None)
reports[-1].CovMatrix = ['9.22702e-06','2.00479e-06','-4.49183e-08','1.6379e-09','0','0','0','0','0','2.00479e-06','0.00580203','-1.24153e-07','5.16861e-08','0','0','0','0','0','-4.49183e-08','-1.24153e-07','6.47518e-09','4.67912e-11','0','0','0','0','0','1.6379e-09','5.16861e-08','4.67912e-11','4.45786e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050952, ("CSC", 2, 1, 2, 1), "MEm12_01"))
reports[-1].posNum = 1743
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0173825, 0.0129809, 0), \
                           ValErr(0.168827, 0.318982, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000106668, 0.00027373, 0), \
                           -1293.48, 1743, 1743, -nan)
reports[-1].sigmaresid = ValErr(0.508217, 0.00860753, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0133114, None, -0.000872822, None, 0.0156557, None, -0.000715468, None, 0.0156557, None, -0.000715468, None, 0.0191381, None, -0.000823936, None, 0.0191381, None, -0.000823936, None, 0.508284, None, 0.00553682, None, 0.508284, None, 0.00553682, None)
reports[-1].CovMatrix = ['0.000168505','1.06145e-05','-1.23391e-06','3.00608e-08','0','0','0','0','0','1.06145e-05','0.10175','-1.30258e-06','1.03659e-06','0','0','0','0','0','-1.23391e-06','-1.30258e-06','7.49281e-08','6.33574e-10','0','0','0','0','0','3.00608e-08','1.03659e-06','6.33574e-10','7.409e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050968, ("CSC", 2, 1, 2, 3), "MEm12_03"))
reports[-1].posNum = 1637
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00226132, 0.0125857, 0), \
                           ValErr(0.225329, 0.309226, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.89123e-05, 0.000268108, 0), \
                           -1110.58, 1637, 1637, -nan)
reports[-1].sigmaresid = ValErr(0.476862, 0.00833383, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00154085, None, 0.000729275, None, 0.000457559, None, 0.000521908, None, 0.000457559, None, 0.000521908, None, -0.00647673, None, 0.000555284, None, -0.00647673, None, 0.000555284, None, 0.476964, None, 0.00577539, None, 0.476964, None, 0.00577539, None)
reports[-1].CovMatrix = ['0.000158401','9.79848e-05','-1.1817e-06','2.88042e-08','0','0','0','0','0','9.79848e-05','0.0956206','-1.22878e-06','1.04273e-06','0','0','0','0','0','-1.1817e-06','-1.22878e-06','7.18818e-08','6.26907e-10','0','0','0','0','0','2.88042e-08','1.04273e-06','6.26907e-10','6.94531e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050984, ("CSC", 2, 1, 2, 5), "MEm12_05"))
reports[-1].posNum = 1531
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00718306, 0.0138029, 0), \
                           ValErr(0.296557, 0.32382, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000215039, 0.000295431, 0), \
                           -1026.42, 1531, 1531, -nan)
reports[-1].sigmaresid = ValErr(0.473071, 0.0085492, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0017223, None, -0.00132032, None, 0.00234419, None, -0.00148095, None, 0.00234419, None, -0.00148095, None, -0.0103718, None, -0.00139036, None, -0.0103718, None, -0.00139036, None, 0.473284, None, 0.00605824, None, 0.473284, None, 0.00605824, None)
reports[-1].CovMatrix = ['0.000190519','-4.72532e-05','-1.96728e-06','2.85113e-08','0','0','0','0','0','-4.72532e-05','0.104859','1.9301e-06','1.10156e-06','0','0','0','0','0','-1.96728e-06','1.9301e-06','8.72795e-08','6.03658e-10','0','0','0','0','0','2.85113e-08','1.10156e-06','6.03658e-10','7.30891e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051000, ("CSC", 2, 1, 2, 7), "MEm12_07"))
reports[-1].posNum = 1783
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00710211, 0.0128335, 0), \
                           ValErr(-0.0866453, 0.317428, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000106746, 0.000271296, 0), \
                           -1311.94, 1783, 1783, -nan)
reports[-1].sigmaresid = ValErr(0.505041, 0.00845756, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0161405, None, -0.000572931, None, 0.00530707, None, -0.000507924, None, 0.00530707, None, -0.000507924, None, 0.00411705, None, -0.000542812, None, 0.00411705, None, -0.000542812, None, 0.505066, None, 0.00561563, None, 0.505066, None, 0.00561563, None)
reports[-1].CovMatrix = ['0.0001647','0.000125174','-1.26165e-06','3.42513e-08','0','0','0','0','0','0.000125174','0.100761','-4.80246e-06','1.11305e-06','0','0','0','0','0','-1.26165e-06','-4.80246e-06','7.36013e-08','5.87263e-10','0','0','0','0','0','3.42513e-08','1.11305e-06','5.87263e-10','7.15306e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051016, ("CSC", 2, 1, 2, 9), "MEm12_09"))
reports[-1].posNum = 1717
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00977358, 0.0129006, 0), \
                           ValErr(0.0513562, 0.311966, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000176116, 0.00027908, 0), \
                           -1237.35, 1717, 1717, -nan)
reports[-1].sigmaresid = ValErr(0.497438, 0.00848868, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0145725, None, -0.000120931, None, 0.00684262, None, -9.14238e-05, None, 0.00684262, None, -9.14238e-05, None, 0.014556, None, -0.000152229, None, 0.014556, None, -0.000152229, None, 0.497497, None, 0.00585042, None, 0.497497, None, 0.00585042, None)
reports[-1].CovMatrix = ['0.000166427','-5.59129e-05','-1.31619e-06','2.8376e-08','0','0','0','0','0','-5.59129e-05','0.0973226','-1.57182e-06','1.0566e-06','0','0','0','0','0','-1.31619e-06','-1.57182e-06','7.78858e-08','6.84313e-10','0','0','0','0','0','2.8376e-08','1.0566e-06','6.84313e-10','7.2058e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051032, ("CSC", 2, 1, 2, 11), "MEm12_11"))
reports[-1].posNum = 1740
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00359252, 0.0124998, 0), \
                           ValErr(0.106722, 0.303797, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.09663e-05, 0.000270678, 0), \
                           -1248.66, 1740, 1740, -nan)
reports[-1].sigmaresid = ValErr(0.495934, 0.00840691, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00358266, None, -7.45114e-05, None, -0.00433132, None, -0.000284334, None, -0.00433132, None, -0.000284334, None, 0.0103807, None, -0.000213341, None, 0.0103807, None, -0.000213341, None, 0.495957, None, 0.00571034, None, 0.495957, None, 0.00571034, None)
reports[-1].CovMatrix = ['0.000156245','-0.000137305','-1.03999e-06','3.0801e-08','0','0','0','0','0','-0.000137305','0.0922926','1.90734e-06','1.03486e-06','0','0','0','0','0','-1.03999e-06','1.90734e-06','7.32664e-08','7.1281e-10','0','0','0','0','0','3.0801e-08','1.03486e-06','7.1281e-10','7.06765e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051048, ("CSC", 2, 1, 2, 13), "MEm12_13"))
reports[-1].posNum = 1646
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00373968, 0.0124993, 0), \
                           ValErr(0.0245869, 0.310836, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000176454, 0.000269959, 0), \
                           -1107.51, 1646, 1646, -nan)
reports[-1].sigmaresid = ValErr(0.474219, 0.00826509, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00654418, None, -0.000480108, None, 0.000972237, None, -0.000516913, None, 0.000972237, None, -0.000516913, None, 0.0235194, None, -0.00067373, None, 0.0235194, None, -0.00067373, None, 0.474281, None, 0.00574768, None, 0.474281, None, 0.00574768, None)
reports[-1].CovMatrix = ['0.000156232','-0.000291623','-1.17594e-06','2.58449e-08','0','0','0','0','0','-0.000291623','0.0966193','2.7517e-06','9.82815e-07','0','0','0','0','0','-1.17594e-06','2.7517e-06','7.28777e-08','6.48669e-10','0','0','0','0','0','2.58449e-08','9.82815e-07','6.48669e-10','6.83121e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051064, ("CSC", 2, 1, 2, 15), "MEm12_15"))
reports[-1].posNum = 1842
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0113257, 0.0120881, 0), \
                           ValErr(0.096799, 0.298627, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000338385, 0.000257504, 0), \
                           -1343.65, 1842, 1842, -nan)
reports[-1].sigmaresid = ValErr(0.501829, 0.00826784, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00151901, None, -0.00108007, None, 0.00720595, None, -0.00129429, None, 0.00720595, None, -0.00129429, None, -0.00762395, None, -0.00107884, None, -0.00762395, None, -0.00107884, None, 0.502084, None, 0.00625758, None, 0.502084, None, 0.00625758, None)
reports[-1].CovMatrix = ['0.000146122','7.46842e-05','-7.85508e-07','3.3715e-08','0','0','0','0','0','7.46842e-05','0.089178','1.6396e-06','1.06874e-06','0','0','0','0','0','-7.85508e-07','1.6396e-06','6.63082e-08','6.53088e-10','0','0','0','0','0','3.3715e-08','1.06874e-06','6.53088e-10','6.83576e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051080, ("CSC", 2, 1, 2, 17), "MEm12_17"))
reports[-1].posNum = 1440
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00774282, 0.0139598, 0), \
                           ValErr(0.15868, 0.327322, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.23951e-05, 0.000301109, 0), \
                           -957.281, 1440, 1440, -nan)
reports[-1].sigmaresid = ValErr(0.470406, 0.00876549, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0056708, None, -0.00128347, None, 0.00569484, None, -0.00149162, None, 0.00569484, None, -0.00149162, None, 0.00484583, None, -0.00128996, None, 0.00484583, None, -0.00128996, None, 0.470455, None, 0.00669021, None, 0.470455, None, 0.00669021, None)
reports[-1].CovMatrix = ['0.000194877','0.000264907','-1.92344e-06','3.15565e-08','0','0','0','0','0','0.000264907','0.107139','-2.67698e-06','1.17698e-06','0','0','0','0','0','-1.92344e-06','-2.67698e-06','9.06668e-08','6.04285e-10','0','0','0','0','0','3.15565e-08','1.17698e-06','6.04285e-10','7.68342e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051096, ("CSC", 2, 1, 2, 19), "MEm12_19"))
reports[-1].posNum = 1581
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00855995, 0.0129252, 0), \
                           ValErr(-0.101644, 0.319115, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000171709, 0.000277856, 0), \
                           -1102.3, 1581, 1581, -nan)
reports[-1].sigmaresid = ValErr(0.485915, 0.00864128, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00131869, None, -0.00164984, None, 0.006878, None, -0.0016321, None, 0.006878, None, -0.0016321, None, 0.00155322, None, -0.00153369, None, 0.00155322, None, -0.00153369, None, 0.485992, None, 0.00586268, None, 0.485992, None, 0.00586268, None)
reports[-1].CovMatrix = ['0.000167061','0.000650841','-1.04794e-06','4.15559e-08','0','0','0','0','0','0.000650841','0.101835','-4.05507e-06','1.27327e-06','0','0','0','0','0','-1.04794e-06','-4.05507e-06','7.72037e-08','6.7567e-10','0','0','0','0','0','4.15559e-08','1.27327e-06','6.7567e-10','7.4672e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051112, ("CSC", 2, 1, 2, 21), "MEm12_21"))
reports[-1].posNum = 1715
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0109864, 0.0119415, 0), \
                           ValErr(-0.0395919, 0.292148, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00019513, 0.000252066, 0), \
                           -1102.32, 1715, 1715, -nan)
reports[-1].sigmaresid = ValErr(0.460159, 0.00785706, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00470005, None, 0.000501767, None, 0.00762477, None, 0.000614095, None, 0.00762477, None, 0.000614095, None, 0.0106757, None, 0.000737291, None, 0.0106757, None, 0.000737291, None, 0.460244, None, 0.00674607, None, 0.460244, None, 0.00674607, None)
reports[-1].CovMatrix = ['0.0001426','0.000119787','-1.1021e-06','2.6343e-08','0','0','0','0','0','0.000119787','0.0853506','-4.81652e-06','8.77585e-07','0','0','0','0','0','-1.1021e-06','-4.81652e-06','6.35371e-08','4.75828e-10','0','0','0','0','0','2.6343e-08','8.77585e-07','4.75828e-10','6.17337e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051128, ("CSC", 2, 1, 2, 23), "MEm12_23"))
reports[-1].posNum = 1755
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0114177, 0.0120137, 0), \
                           ValErr(-0.173261, 0.293234, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000316553, 0.000258298, 0), \
                           -1187.42, 1755, 1755, -nan)
reports[-1].sigmaresid = ValErr(0.475995, 0.0080343, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0190682, None, -0.00138046, None, 0.00666301, None, -0.00118826, None, 0.00666301, None, -0.00118826, None, -0.0278243, None, -0.00127144, None, -0.0278243, None, -0.00127144, None, 0.476243, None, 0.00618728, None, 0.476243, None, 0.00618728, None)
reports[-1].CovMatrix = ['0.00014433','-5.44566e-06','-1.00792e-06','2.76094e-08','0','0','0','0','0','-5.44566e-06','0.0859863','1.29802e-06','9.62426e-07','0','0','0','0','0','-1.00792e-06','1.29802e-06','6.67179e-08','6.09091e-10','0','0','0','0','0','2.76094e-08','9.62426e-07','6.09091e-10','6.45503e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051144, ("CSC", 2, 1, 2, 25), "MEm12_25"))
reports[-1].posNum = 1419
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00540061, 0.0141767, 0), \
                           ValErr(-0.226885, 0.322179, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.03751e-05, 0.000290473, 0), \
                           -941.644, 1419, 1419, -nan)
reports[-1].sigmaresid = ValErr(0.469851, 0.00881971, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0341585, None, -0.00138087, None, -0.00571651, None, -0.00128224, None, -0.00571651, None, -0.00128224, None, 0.00600857, None, -0.00142793, None, 0.00600857, None, -0.00142793, None, 0.469934, None, 0.00652616, None, 0.469934, None, 0.00652616, None)
reports[-1].CovMatrix = ['0.000200978','0.000164936','-1.95621e-06','3.1488e-08','0','0','0','0','0','0.000164936','0.103799','-4.03448e-06','1.14162e-06','0','0','0','0','0','-1.95621e-06','-4.03448e-06','8.43745e-08','5.71514e-10','0','0','0','0','0','3.1488e-08','1.14162e-06','5.71514e-10','7.77877e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051160, ("CSC", 2, 1, 2, 27), "MEm12_27"))
reports[-1].posNum = 1245
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.017911, 0.0146981, 0), \
                           ValErr(0.0953726, 0.391418, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00038722, 0.000301025, 0), \
                           -794.399, 1245, 1245, -nan)
reports[-1].sigmaresid = ValErr(0.458008, 0.0091785, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0138772, None, 0.000586399, None, 0.00912833, None, 0.00055978, None, 0.00912833, None, 0.00055978, None, 0.0285499, None, 0.000622902, None, 0.0285499, None, 0.000622902, None, 0.45832, None, 0.00706422, None, 0.45832, None, 0.00706422, None)
reports[-1].CovMatrix = ['0.000216035','0.00103069','-1.94913e-06','4.37714e-08','0','0','0','0','0','0.00103069','0.153208','-4.82059e-06','1.62007e-06','0','0','0','0','0','-1.94913e-06','-4.82059e-06','9.06162e-08','5.99411e-10','0','0','0','0','0','4.37714e-08','1.62007e-06','5.99411e-10','8.42455e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051176, ("CSC", 2, 1, 2, 29), "MEm12_29"))
reports[-1].posNum = 1554
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00854584, 0.0136642, 0), \
                           ValErr(-0.0878525, 0.324753, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000250465, 0.00027636, 0), \
                           -1074.09, 1554, 1554, -nan)
reports[-1].sigmaresid = ValErr(0.482989, 0.00866355, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00662448, None, -0.00129963, None, 0.00318994, None, -0.00128887, None, 0.00318994, None, -0.00128887, None, 0.0143426, None, -0.00134647, None, 0.0143426, None, -0.00134647, None, 0.483132, None, 0.00698748, None, 0.483132, None, 0.00698748, None)
reports[-1].CovMatrix = ['0.00018671','0.000220892','-1.66873e-06','3.23837e-08','0','0','0','0','0','0.000220892','0.105465','-4.66263e-06','1.14413e-06','0','0','0','0','0','-1.66873e-06','-4.66263e-06','7.63747e-08','5.52863e-10','0','0','0','0','0','3.23837e-08','1.14413e-06','5.52863e-10','7.50575e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051192, ("CSC", 2, 1, 2, 31), "MEm12_31"))
reports[-1].posNum = 1088
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00257669, 0.0198968, 0), \
                           ValErr(-0.362458, 0.355946, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000190157, 0.000381361, 0), \
                           -615.061, 1088, 1088, -nan)
reports[-1].sigmaresid = ValErr(0.425871, 0.00912957, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00641048, None, -0.00172662, None, -0.00580916, None, -0.00149007, None, -0.00580916, None, -0.00149007, None, -0.0238567, None, -0.00159279, None, -0.0238567, None, -0.00159279, None, 0.426098, None, 0.00625277, None, 0.426098, None, 0.00625277, None)
reports[-1].CovMatrix = ['0.000395882','-0.0009776','-5.76339e-06','1.81898e-08','0','0','0','0','0','-0.0009776','0.126698','1.6741e-05','1.02439e-06','0','0','0','0','0','-5.76339e-06','1.6741e-05','1.45436e-07','4.99293e-10','0','0','0','0','0','1.81898e-08','1.02439e-06','4.99293e-10','8.33497e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051208, ("CSC", 2, 1, 2, 33), "MEm12_33"))
reports[-1].posNum = 1481
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00756317, 0.0139325, 0), \
                           ValErr(0.0205201, 0.361516, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000185412, 0.000290057, 0), \
                           -999.01, 1481, 1481, -nan)
reports[-1].sigmaresid = ValErr(0.475026, 0.00872821, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00766519, None, -0.000935602, None, 0.00355971, None, -0.00112761, None, 0.00355971, None, -0.00112761, None, 0.0180424, None, -0.001088, None, 0.0180424, None, -0.001088, None, 0.475091, None, 0.00705802, None, 0.475091, None, 0.00705802, None)
reports[-1].CovMatrix = ['0.000194115','0.000822652','-1.74008e-06','4.01604e-08','0','0','0','0','0','0.000822652','0.130694','2.17734e-06','1.51884e-06','0','0','0','0','0','-1.74008e-06','2.17734e-06','8.41332e-08','6.37798e-10','0','0','0','0','0','4.01604e-08','1.51884e-06','6.37798e-10','7.6182e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051224, ("CSC", 2, 1, 2, 35), "MEm12_35"))
reports[-1].posNum = 1651
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00037988, 0.0131843, 0), \
                           ValErr(-0.181757, 0.311657, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.56907e-05, 0.000277632, 0), \
                           -1129.73, 1651, 1651, -nan)
reports[-1].sigmaresid = ValErr(0.479664, 0.00834734, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00659344, None, -0.000851323, None, -0.000463089, None, -0.000726045, None, -0.000463089, None, -0.000726045, None, 0.00973, None, -0.000816566, None, 0.00973, None, -0.000816566, None, 0.479717, None, 0.0061492, None, 0.479717, None, 0.0061492, None)
reports[-1].CovMatrix = ['0.000173827','8.71197e-05','-1.62897e-06','2.85818e-08','0','0','0','0','0','8.71197e-05','0.0971299','-1.02369e-06','1.06513e-06','0','0','0','0','0','-1.62897e-06','-1.02369e-06','7.70797e-08','5.69132e-10','0','0','0','0','0','2.85818e-08','1.06513e-06','5.69132e-10','6.96784e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050960, ("CSC", 2, 1, 2, 2), "MEm12_02"))
reports[-1].posNum = 1696
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00531958, 0.0125346, 0), \
                           ValErr(0.164192, 0.301214, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000216669, 0.000267067, 0), \
                           -1178.2, 1696, 1696, -nan)
reports[-1].sigmaresid = ValErr(0.484691, 0.00832216, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0151295, None, -0.000555684, None, 0.00157433, None, -0.000699523, None, 0.00157433, None, -0.000699523, None, -0.010031, None, -0.000539743, None, -0.010031, None, -0.000539743, None, 0.484826, None, 0.00685754, None, 0.484826, None, 0.00685754, None)
reports[-1].CovMatrix = ['0.000157115','0.000162871','-1.14389e-06','3.16621e-08','0','0','0','0','0','0.000162871','0.0907301','-7.20254e-07','1.05798e-06','0','0','0','0','0','-1.14389e-06','-7.20254e-07','7.1325e-08','6.24241e-10','0','0','0','0','0','3.16621e-08','1.05798e-06','6.24241e-10','6.92587e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050976, ("CSC", 2, 1, 2, 4), "MEm12_04"))
reports[-1].posNum = 1138
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0173365, 0.0157958, 0), \
                           ValErr(0.151884, 0.370107, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00016427, 0.000359735, 0), \
                           -775.492, 1138, 1138, -nan)
reports[-1].sigmaresid = ValErr(0.478315, 0.010026, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0143656, None, 0.000538959, None, 0.0137817, None, 0.00075317, None, 0.0137817, None, 0.00075317, None, 1.40976e-05, None, 0.000801715, None, 1.40976e-05, None, 0.000801715, None, 0.478386, None, 0.00642326, None, 0.478386, None, 0.00642326, None)
reports[-1].CovMatrix = ['0.000249507','0.000671679','-2.47048e-06','4.80823e-08','0','0','0','0','0','0.000671679','0.136979','-1.31624e-05','1.53561e-06','0','0','0','0','0','-2.47048e-06','-1.31624e-05','1.29409e-07','7.41155e-10','0','0','0','0','0','4.80823e-08','1.53561e-06','7.41155e-10','0.000100521','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050992, ("CSC", 2, 1, 2, 6), "MEm12_06"))
reports[-1].posNum = 1578
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0128235, 0.0128582, 0), \
                           ValErr(0.176097, 0.31693, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000169245, 0.000276575, 0), \
                           -1066.21, 1578, 1578, -nan)
reports[-1].sigmaresid = ValErr(0.475559, 0.00846517, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00242374, None, 0.000868244, None, 0.010565, None, 0.000947568, None, 0.010565, None, 0.000947568, None, 0.0399593, None, 0.000882748, None, 0.0399593, None, 0.000882748, None, 0.475662, None, 0.00543703, None, 0.475662, None, 0.00543703, None)
reports[-1].CovMatrix = ['0.000165335','-0.00032031','-1.26882e-06','2.75513e-08','0','0','0','0','0','-0.00032031','0.100444','4.91901e-07','9.98293e-07','0','0','0','0','0','-1.26882e-06','4.91901e-07','7.64939e-08','6.39192e-10','0','0','0','0','0','2.75513e-08','9.98293e-07','6.39192e-10','7.16594e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051008, ("CSC", 2, 1, 2, 8), "MEm12_08"))
reports[-1].posNum = 1537
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0112245, 0.012687, 0), \
                           ValErr(-0.0860774, 0.2914, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000275798, 0.000266326, 0), \
                           -920.177, 1537, 1537, -nan)
reports[-1].sigmaresid = ValErr(0.44032, 0.00794175, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0043097, None, -0.00343036, None, 0.00506148, None, -0.00352771, None, 0.00506148, None, -0.00352771, None, -0.0132013, None, -0.00337872, None, -0.0132013, None, -0.00337872, None, 0.440485, None, 0.00634346, None, 0.440485, None, 0.00634346, None)
reports[-1].CovMatrix = ['0.000160959','-7.06131e-05','-1.57063e-06','2.28097e-08','0','0','0','0','0','-7.06131e-05','0.084914','6.65729e-07','8.86566e-07','0','0','0','0','0','-1.57063e-06','6.65729e-07','7.09294e-08','4.77014e-10','0','0','0','0','0','2.28097e-08','8.86566e-07','4.77014e-10','6.30716e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051024, ("CSC", 2, 1, 2, 10), "MEm12_10"))
reports[-1].posNum = 1780
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0116469, 0.0118292, 0), \
                           ValErr(0.0839522, 0.293296, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00032007, 0.000258448, 0), \
                           -1210.47, 1780, 1780, -nan)
reports[-1].sigmaresid = ValErr(0.47764, 0.00800525, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.012313, None, -0.000123471, None, 0.00741311, None, -9.67825e-05, None, 0.00741311, None, -9.67825e-05, None, 0.00516418, None, -0.000111965, None, 0.00516418, None, -0.000111965, None, 0.477858, None, 0.00560944, None, 0.477858, None, 0.00560944, None)
reports[-1].CovMatrix = ['0.000139931','-1.83706e-05','-8.86296e-07','2.8043e-08','0','0','0','0','0','-1.83706e-05','0.0860226','4.00064e-07','9.45017e-07','0','0','0','0','0','-8.86296e-07','4.00064e-07','6.67955e-08','6.22907e-10','0','0','0','0','0','2.8043e-08','9.45017e-07','6.22907e-10','6.40843e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051040, ("CSC", 2, 1, 2, 12), "MEm12_12"))
reports[-1].posNum = 1613
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00595097, 0.0124107, 0), \
                           ValErr(-0.00631899, 0.302646, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000147966, 0.000276022, 0), \
                           -1055.86, 1613, 1613, -nan)
reports[-1].sigmaresid = ValErr(0.465639, 0.00819814, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00395089, None, 0.000278279, None, 0.00357307, None, 0.000292456, None, 0.00357307, None, 0.000292456, None, -0.0023823, None, 0.000275661, None, -0.0023823, None, 0.000275661, None, 0.465682, None, 0.00556055, None, 0.465682, None, 0.00556055, None)
reports[-1].CovMatrix = ['0.000154026','4.99641e-05','-1.22199e-06','2.8534e-08','0','0','0','0','0','4.99641e-05','0.0915948','-4.61745e-06','9.40246e-07','0','0','0','0','0','-1.22199e-06','-4.61745e-06','7.6188e-08','5.56688e-10','0','0','0','0','0','2.8534e-08','9.40246e-07','5.56688e-10','6.72099e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051056, ("CSC", 2, 1, 2, 14), "MEm12_14"))
reports[-1].posNum = 1851
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00759405, 0.0111928, 0), \
                           ValErr(0.0363037, 0.270292, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000146217, 0.000239624, 0), \
                           -1176.98, 1851, 1851, -nan)
reports[-1].sigmaresid = ValErr(0.456995, 0.00751086, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00131449, None, -0.00358411, None, 0.00548952, None, -0.00379363, None, 0.00548952, None, -0.00379363, None, 0.00920737, None, -0.00374514, None, 0.00920737, None, -0.00374514, None, 0.457046, None, 0.0071922, None, 0.457046, None, 0.0071922, None)
reports[-1].CovMatrix = ['0.000125279','-0.000100381','-8.42783e-07','2.31162e-08','0','0','0','0','0','-0.000100381','0.0730576','1.59422e-06','7.74551e-07','0','0','0','0','0','-8.42783e-07','1.59422e-06','5.74197e-08','5.02556e-10','0','0','0','0','0','2.31162e-08','7.74551e-07','5.02556e-10','5.64132e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051072, ("CSC", 2, 1, 2, 16), "MEm12_16"))
reports[-1].posNum = 1697
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00443087, 0.0121408, 0), \
                           ValErr(-0.289684, 0.296926, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.35097e-06, 0.000261951, 0), \
                           -1138.64, 1697, 1697, -nan)
reports[-1].sigmaresid = ValErr(0.47333, 0.00812471, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00297194, None, -0.000844214, None, -0.00424878, None, -0.000778091, None, -0.00424878, None, -0.000778091, None, -0.000995813, None, -0.000742157, None, -0.000995813, None, -0.000742157, None, 0.473462, None, 0.00630575, None, 0.473462, None, 0.00630575, None)
reports[-1].CovMatrix = ['0.0001474','2.21179e-05','-1.02392e-06','2.85435e-08','0','0','0','0','0','2.21179e-05','0.0881652','4.76222e-06','1.03693e-06','0','0','0','0','0','-1.02392e-06','4.76222e-06','6.86184e-08','6.58996e-10','0','0','0','0','0','2.85435e-08','1.03693e-06','6.58996e-10','6.60112e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051088, ("CSC", 2, 1, 2, 18), "MEm12_18"))
reports[-1].posNum = 1631
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00767876, 0.0122909, 0), \
                           ValErr(0.0583832, 0.30933, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000196747, 0.000254753, 0), \
                           -1070.5, 1631, 1631, -nan)
reports[-1].sigmaresid = ValErr(0.466455, 0.00816708, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00293145, None, -0.00131349, None, 0.00460219, None, -0.00116875, None, 0.00460219, None, -0.00116875, None, 0.0145242, None, -0.00138349, None, 0.0145242, None, -0.00138349, None, 0.466545, None, 0.00607803, None, 0.466545, None, 0.00607803, None)
reports[-1].CovMatrix = ['0.000151067','-0.000217703','-1.05756e-06','2.58101e-08','0','0','0','0','0','-0.000217703','0.0956851','8.97887e-07','9.49531e-07','0','0','0','0','0','-1.05756e-06','8.97887e-07','6.48993e-08','5.86551e-10','0','0','0','0','0','2.58101e-08','9.49531e-07','5.86551e-10','6.67015e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051104, ("CSC", 2, 1, 2, 20), "MEm12_20"))
reports[-1].posNum = 1595
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0024625, 0.0127367, 0), \
                           ValErr(0.0126733, 0.297044, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.95741e-05, 0.000270266, 0), \
                           -1022.56, 1595, 1595, -nan)
reports[-1].sigmaresid = ValErr(0.459399, 0.00813381, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00320407, None, 0.000317879, None, -0.00205645, None, 0.000306547, None, -0.00205645, None, 0.000306547, None, -0.00425065, None, 0.000426122, None, -0.00425065, None, 0.000426122, None, 0.459399, None, 0.00587166, None, 0.459399, None, 0.00587166, None)
reports[-1].CovMatrix = ['0.000162223','-6.98605e-05','-1.47651e-06','2.48402e-08','0','0','0','0','0','-6.98605e-05','0.0882349','-1.18473e-07','9.22259e-07','0','0','0','0','0','-1.47651e-06','-1.18473e-07','7.30436e-08','5.43397e-10','0','0','0','0','0','2.48402e-08','9.22259e-07','5.43397e-10','6.61591e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051120, ("CSC", 2, 1, 2, 22), "MEm12_22"))
reports[-1].posNum = 1692
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000704883, 0.012182, 0), \
                           ValErr(-0.0191892, 0.293547, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.39013e-05, 0.000259849, 0), \
                           -1134.36, 1692, 1692, -nan)
reports[-1].sigmaresid = ValErr(0.47307, 0.00813222, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.015489, None, 0.000419, None, -0.000947694, None, 0.000201964, None, -0.000947694, None, 0.000201964, None, 0.00448048, None, 0.000260812, None, 0.00448048, None, 0.000260812, None, 0.473071, None, 0.00651031, None, 0.473071, None, 0.00651031, None)
reports[-1].CovMatrix = ['0.000148401','-0.000201404','-1.03526e-06','2.49649e-08','0','0','0','0','0','-0.000201404','0.0861699','3.35545e-06','9.47084e-07','0','0','0','0','0','-1.03526e-06','3.35545e-06','6.75214e-08','6.58699e-10','0','0','0','0','0','2.49649e-08','9.47084e-07','6.58699e-10','6.61333e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051136, ("CSC", 2, 1, 2, 24), "MEm12_24"))
reports[-1].posNum = 1869
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00377815, 0.0113917, 0), \
                           ValErr(-0.107273, 0.286901, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000222895, 0.000243836, 0), \
                           -1253.65, 1869, 1869, -nan)
reports[-1].sigmaresid = ValErr(0.473229, 0.00774018, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00517043, None, -0.00258894, None, 0.00118126, None, -0.0025904, None, 0.00118126, None, -0.0025904, None, -0.0105999, None, -0.00266413, None, -0.0105999, None, -0.00266413, None, 0.47336, None, 0.00567696, None, 0.47336, None, 0.00567696, None)
reports[-1].CovMatrix = ['0.000129772','0.000224773','-7.5758e-07','2.91122e-08','0','0','0','0','0','0.000224773','0.0823121','-5.39004e-06','8.90226e-07','0','0','0','0','0','-7.5758e-07','-5.39004e-06','5.94562e-08','5.14025e-10','0','0','0','0','0','2.91122e-08','8.90226e-07','5.14025e-10','5.99107e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051152, ("CSC", 2, 1, 2, 26), "MEm12_26"))
reports[-1].posNum = 1229
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00344557, 0.0141164, 0), \
                           ValErr(-0.113627, 0.334045, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000128834, 0.000280514, 0), \
                           -738.015, 1229, 1229, -nan)
reports[-1].sigmaresid = ValErr(0.441122, 0.00889751, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00347326, None, -0.00112629, None, -0.000514097, None, -0.00108991, None, -0.000514097, None, -0.00108991, None, 0.00210765, None, -0.00132153, None, 0.00210765, None, -0.00132153, None, 0.441179, None, 0.00625071, None, 0.441179, None, 0.00625071, None)
reports[-1].CovMatrix = ['0.000199273','-2.42834e-05','-1.79489e-06','2.85802e-08','0','0','0','0','0','-2.42834e-05','0.111586','7.28131e-07','1.17619e-06','0','0','0','0','0','-1.79489e-06','7.28131e-07','7.8688e-08','5.90815e-10','0','0','0','0','0','2.85802e-08','1.17619e-06','5.90815e-10','7.91662e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051168, ("CSC", 2, 1, 2, 28), "MEm12_28"))
reports[-1].posNum = 1496
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0108346, 0.0134001, 0), \
                           ValErr(-0.116139, 0.312966, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000239237, 0.000266548, 0), \
                           -973.625, 1496, 1496, -nan)
reports[-1].sigmaresid = ValErr(0.463885, 0.00848064, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00168824, None, 0.00130094, None, 0.00526774, None, 0.00153512, None, 0.00526774, None, 0.00153512, None, 0.00394704, None, 0.0016378, None, 0.00394704, None, 0.0016378, None, 0.464032, None, 0.00673051, None, 0.464032, None, 0.00673051, None)
reports[-1].CovMatrix = ['0.000179562','-0.000174118','-1.58482e-06','2.6417e-08','0','0','0','0','0','-0.000174118','0.0979474','-7.00593e-07','9.88865e-07','0','0','0','0','0','-1.58482e-06','-7.00593e-07','7.10476e-08','5.36583e-10','0','0','0','0','0','2.6417e-08','9.88865e-07','5.36583e-10','7.19217e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051184, ("CSC", 2, 1, 2, 30), "MEm12_30"))
reports[-1].posNum = 1052
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0159135, 0.0159837, 0), \
                           ValErr(0.00178332, 0.344269, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00021456, 0.000295367, 0), \
                           -538.802, 1052, 1052, -nan)
reports[-1].sigmaresid = ValErr(0.403828, 0.0088039, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00842731, None, -0.000259786, None, 0.00885299, None, -0.000226299, None, 0.00885299, None, -0.000226299, None, -0.00408346, None, -0.000123329, None, -0.00408346, None, -0.000123329, None, 0.403929, None, 0.00478902, None, 0.403929, None, 0.00478902, None)
reports[-1].CovMatrix = ['0.000255478','0.000928028','-2.92155e-06','2.97595e-08','0','0','0','0','0','0.000928028','0.118521','-1.11563e-05','1.1131e-06','0','0','0','0','0','-2.92155e-06','-1.11563e-05','8.72417e-08','3.82476e-10','0','0','0','0','0','2.97595e-08','1.1131e-06','3.82476e-10','7.75091e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051200, ("CSC", 2, 1, 2, 32), "MEm12_32"))
reports[-1].posNum = 1268
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00609975, 0.0153432, 0), \
                           ValErr(0.0292275, 0.321334, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.15235e-05, 0.000319506, 0), \
                           -717.919, 1268, 1268, -nan)
reports[-1].sigmaresid = ValErr(0.42624, 0.00846409, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000283141, None, -0.00108974, None, -0.00847462, None, -0.00104568, None, -0.00847462, None, -0.00104568, None, -0.0042065, None, -0.00103433, None, -0.0042065, None, -0.00103433, None, 0.426251, None, 0.00645306, None, 0.426251, None, 0.00645306, None)
reports[-1].CovMatrix = ['0.000235414','-0.00016807','-3.05603e-06','2.18326e-08','0','0','0','0','0','-0.00016807','0.103255','-3.00945e-06','8.61527e-07','0','0','0','0','0','-3.05603e-06','-3.00945e-06','1.02084e-07','4.57497e-10','0','0','0','0','0','2.18326e-08','8.61527e-07','4.57497e-10','7.16412e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051216, ("CSC", 2, 1, 2, 34), "MEm12_34"))
reports[-1].posNum = 1687
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00254608, 0.0122184, 0), \
                           ValErr(0.117556, 0.297633, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.61747e-05, 0.000264319, 0), \
                           -1139.9, 1687, 1687, -nan)
reports[-1].sigmaresid = ValErr(0.475569, 0.00818729, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0122276, None, -0.000765601, None, -0.00219321, None, -0.000671002, None, -0.00219321, None, -0.000671002, None, 0.0150743, None, -0.000665129, None, 0.0150743, None, -0.000665129, None, 0.475592, None, 0.00697661, None, 0.475592, None, 0.00697661, None)
reports[-1].CovMatrix = ['0.000149289','-0.000112875','-1.02842e-06','2.80041e-08','0','0','0','0','0','-0.000112875','0.0885853','1.7129e-06','9.65092e-07','0','0','0','0','0','-1.02842e-06','1.7129e-06','6.98644e-08','6.41352e-10','0','0','0','0','0','2.80041e-08','9.65092e-07','6.41352e-10','6.7032e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051232, ("CSC", 2, 1, 2, 36), "MEm12_36"))
reports[-1].posNum = 1652
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0121559, 0.012922, 0), \
                           ValErr(-0.0224792, 0.321486, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000257001, 0.000273082, 0), \
                           -1168.14, 1652, 1652, -nan)
reports[-1].sigmaresid = ValErr(0.490741, 0.00853745, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000278806, None, 0.000572914, None, 0.00781966, None, 0.000526968, None, 0.00781966, None, 0.000526968, None, -0.00755964, None, 0.000667077, None, -0.00755964, None, 0.000667077, None, 0.490876, None, 0.00549042, None, 0.490876, None, 0.00549042, None)
reports[-1].CovMatrix = ['0.000166978','-1.4484e-05','-1.25733e-06','3.20327e-08','0','0','0','0','0','-1.4484e-05','0.103353','6.38242e-07','1.13185e-06','0','0','0','0','0','-1.25733e-06','6.38242e-07','7.45735e-08','6.49872e-10','0','0','0','0','0','3.20327e-08','1.13185e-06','6.49872e-10','7.28885e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051464, ("CSC", 2, 1, 3, 1), "MEm13_01"))
reports[-1].posNum = 753
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0226724, 0.0507259, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000281269, 0.00115103, 0), \
                           -1285.76, 753, 753, -nan)
reports[-1].sigmaresid = ValErr(1.33452, 0.0343879, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0211271, None, -0.00184173, None, 0.0191474, None, -0.00200574, None, 0.0191474, None, -0.00200574, None, 0.0283021, None, -0.00187896, None, 0.0283021, None, -0.00187896, None, 1.33458, None, 0.0108302, None, 1.33458, None, 0.0108302, None)
reports[-1].CovMatrix = ['0.00257311','-1.65993e-05','8.31967e-07','0','0','0','0','0','0','-1.65993e-05','1.32488e-06','1.88338e-08','0','0','0','0','0','0','8.31967e-07','1.88338e-08','0.00118257','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051472, ("CSC", 2, 1, 3, 2), "MEm13_02"))
reports[-1].posNum = 675
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00961446, 0.051547, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.09602e-06, 0.00122007, 0), \
                           -1139.75, 675, 675, -nan)
reports[-1].sigmaresid = ValErr(1.30941, 0.0356369, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0574583, None, -0.00163537, None, 0.00959565, None, -0.00138026, None, 0.00959565, None, -0.00138026, None, 0.080007, None, -0.00183097, None, 0.080007, None, -0.00183097, None, 1.30941, None, 0.0109219, None, 1.30941, None, 0.0109219, None)
reports[-1].CovMatrix = ['0.0026571','-1.31984e-05','9.41966e-07','0','0','0','0','0','0','-1.31984e-05','1.48857e-06','2.22532e-08','0','0','0','0','0','0','9.41966e-07','2.22532e-08','0.00127004','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051480, ("CSC", 2, 1, 3, 3), "MEm13_03"))
reports[-1].posNum = 620
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00108844, 0.0518634, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.18666e-05, 0.00128959, 0), \
                           -1038.17, 620, 620, -nan)
reports[-1].sigmaresid = ValErr(1.29116, 0.0366657, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0414765, None, 0.00286679, None, 0.00100539, None, 0.00273686, None, 0.00100539, None, 0.00273686, None, 0.0165363, None, 0.00266291, None, 0.0165363, None, 0.00266291, None, 1.29115, None, 0.00864858, None, 1.29115, None, 0.00864858, None)
reports[-1].CovMatrix = ['0.00268981','-1.26322e-06','1.33377e-06','0','0','0','0','0','0','-1.26322e-06','1.66303e-06','2.60146e-08','0','0','0','0','0','0','1.33377e-06','2.60146e-08','0.00134443','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051488, ("CSC", 2, 1, 3, 4), "MEm13_04"))
reports[-1].posNum = 449
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051496, ("CSC", 2, 1, 3, 5), "MEm13_05"))
reports[-1].posNum = 389
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051504, ("CSC", 2, 1, 3, 6), "MEm13_06"))
reports[-1].posNum = 290
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051512, ("CSC", 2, 1, 3, 7), "MEm13_07"))
reports[-1].posNum = 484
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051520, ("CSC", 2, 1, 3, 8), "MEm13_08"))
reports[-1].posNum = 596
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00549923, 0.04883, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.72938e-05, 0.00117576, 0), \
                           -948.908, 596, 596, -nan)
reports[-1].sigmaresid = ValErr(1.1891, 0.0344409, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.043195, None, -0.00143015, None, 0.00539982, None, -0.00106813, None, 0.00539982, None, -0.00106813, None, -0.0322872, None, -0.000873715, None, -0.0322872, None, -0.000873715, None, 1.18909, None, 0.00906995, None, 1.18909, None, 0.00906995, None)
reports[-1].CovMatrix = ['0.00238437','-4.067e-06','1.00097e-06','0','0','0','0','0','0','-4.067e-06','1.38241e-06','2.39161e-08','0','0','0','0','0','0','1.00097e-06','2.39161e-08','0.00118622','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051528, ("CSC", 2, 1, 3, 9), "MEm13_09"))
reports[-1].posNum = 356
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051536, ("CSC", 2, 1, 3, 10), "MEm13_10"))
reports[-1].posNum = 773
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00426491, 0.0475771, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000444107, 0.00111108, 0), \
                           -1294.08, 773, 773, -nan)
reports[-1].sigmaresid = ValErr(1.29066, 0.0328244, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0501318, None, 0.000460614, None, 9.36599e-05, None, 0.000160216, None, 9.36599e-05, None, 0.000160216, None, 0.0874491, None, -0.000695772, None, 0.0874491, None, -0.000695772, None, 1.2908, None, 0.00964496, None, 1.2908, None, 0.00964496, None)
reports[-1].CovMatrix = ['0.00226358','-1.15785e-05','8.01663e-07','0','0','0','0','0','0','-1.15785e-05','1.23451e-06','1.81511e-08','0','0','0','0','0','0','8.01663e-07','1.81511e-08','0.00107748','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051544, ("CSC", 2, 1, 3, 11), "MEm13_11"))
reports[-1].posNum = 692
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00545479, 0.049671, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000651926, 0.00115234, 0), \
                           -1157.94, 692, 692, -nan)
reports[-1].sigmaresid = ValErr(1.28967, 0.0346658, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0234628, None, 0.00116463, None, -0.0099708, None, 0.00109448, None, -0.0099708, None, 0.00109448, None, 0.0773928, None, 0.000783974, None, 0.0773928, None, 0.000783974, None, 1.28996, None, 0.0101756, None, 1.28996, None, 0.0101756, None)
reports[-1].CovMatrix = ['0.0024672','-9.19565e-06','9.26966e-07','0','0','0','0','0','0','-9.19565e-06','1.32788e-06','2.14234e-08','0','0','0','0','0','0','9.26966e-07','2.14234e-08','0.00120176','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051552, ("CSC", 2, 1, 3, 12), "MEm13_12"))
reports[-1].posNum = 515
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0192937, 0.0571234, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.29022e-05, 0.00152634, 0), \
                           -863.148, 515, 515, -nan)
reports[-1].sigmaresid = ValErr(1.29321, 0.0402963, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.139768, None, 0.000423509, None, -0.0189948, None, 0.000169821, None, -0.0189948, None, 0.000169821, None, -0.0330475, None, 0.000658598, None, -0.0330475, None, 0.000658598, None, 1.29315, None, 0.00759525, None, 1.29315, None, 0.00759525, None)
reports[-1].CovMatrix = ['0.00326308','6.05548e-06','1.3567e-06','0','0','0','0','0','0','6.05548e-06','2.32971e-06','4.40499e-08','0','0','0','0','0','0','1.3567e-06','4.40499e-08','0.00162387','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051560, ("CSC", 2, 1, 3, 13), "MEm13_13"))
reports[-1].posNum = 632
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0454312, 0.0547393, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00078721, 0.00128161, 0), \
                           -1098.01, 632, 632, -nan)
reports[-1].sigmaresid = ValErr(1.37498, 0.0386743, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0860237, None, -0.000731562, None, -0.0467314, None, -0.00133364, None, -0.0467314, None, -0.00133364, None, -0.105695, None, -0.000947637, None, -0.105695, None, -0.000947637, None, 1.37537, None, 0.00835831, None, 1.37537, None, 0.00835831, None)
reports[-1].CovMatrix = ['0.00299639','-2.8632e-06','1.14446e-06','0','0','0','0','0','0','-2.8632e-06','1.64251e-06','3.41988e-08','0','0','0','0','0','0','1.14446e-06','3.41988e-08','0.00149576','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051568, ("CSC", 2, 1, 3, 14), "MEm13_14"))
reports[-1].posNum = 707
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0249824, 0.0497429, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000570152, 0.00118473, 0), \
                           -1186.89, 707, 707, -nan)
reports[-1].sigmaresid = ValErr(1.29674, 0.0344852, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0071504, None, -0.00153655, None, -0.0297182, None, -0.001609, None, -0.0297182, None, -0.001609, None, 0.0265888, None, -0.00167695, None, 0.0265888, None, -0.00167695, None, 1.29692, None, 0.00835048, None, 1.29692, None, 0.00835048, None)
reports[-1].CovMatrix = ['0.00247435','-1.16047e-05','8.84158e-07','0','0','0','0','0','0','-1.16047e-05','1.40358e-06','2.61875e-08','0','0','0','0','0','0','8.84158e-07','2.61875e-08','0.00118927','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051576, ("CSC", 2, 1, 3, 15), "MEm13_15"))
reports[-1].posNum = 632
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00862888, 0.0505298, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.42504e-05, 0.00125026, 0), \
                           -1043.42, 632, 632, -nan)
reports[-1].sigmaresid = ValErr(1.26122, 0.0354755, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0413194, None, -0.00245974, None, 0.00871755, None, -0.00265114, None, 0.00871755, None, -0.00265114, None, 0.0298853, None, -0.00269251, None, 0.0298853, None, -0.00269251, None, 1.26117, None, 0.0102509, None, 1.26117, None, 0.0102509, None)
reports[-1].CovMatrix = ['0.00255326','-7.54071e-06','1.3582e-06','0','0','0','0','0','0','-7.54071e-06','1.56315e-06','2.13223e-08','0','0','0','0','0','0','1.3582e-06','2.13223e-08','0.00125856','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051584, ("CSC", 2, 1, 3, 16), "MEm13_16"))
reports[-1].posNum = 655
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0193906, 0.05013, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000394236, 0.0012528, 0), \
                           -1090.75, 655, 655, -nan)
reports[-1].sigmaresid = ValErr(1.27938, 0.0353491, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0322722, None, -0.00131789, None, -0.0181833, None, -0.00158359, None, -0.0181833, None, -0.00158359, None, -0.14223, None, -0.000555089, None, -0.14223, None, -0.000555089, None, 1.27942, None, 0.00973944, None, 1.27942, None, 0.00973944, None)
reports[-1].CovMatrix = ['0.00251301','-4.70018e-06','9.83411e-07','0','0','0','0','0','0','-4.70018e-06','1.5695e-06','2.63111e-08','0','0','0','0','0','0','9.83411e-07','2.63111e-08','0.0012496','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051592, ("CSC", 2, 1, 3, 17), "MEm13_17"))
reports[-1].posNum = 711
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0150541, 0.0493728, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000705486, 0.00119299, 0), \
                           -1196.51, 711, 711, -nan)
reports[-1].sigmaresid = ValErr(1.30202, 0.0345272, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00347395, None, 0.00243496, None, -0.0193748, None, 0.00258635, None, -0.0193748, None, 0.00258635, None, -0.00760258, None, 0.00287068, None, -0.00760258, None, 0.00287068, None, 1.30234, None, 0.00866071, None, 1.30234, None, 0.00866071, None)
reports[-1].CovMatrix = ['0.00243767','-8.71209e-06','9.33783e-07','0','0','0','0','0','0','-8.71209e-06','1.42323e-06','2.24402e-08','0','0','0','0','0','0','9.33783e-07','2.24402e-08','0.00119217','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051600, ("CSC", 2, 1, 3, 18), "MEm13_18"))
reports[-1].posNum = 695
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00460311, 0.0468253, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00042619, 0.00114293, 0), \
                           -1121.19, 695, 695, -nan)
reports[-1].sigmaresid = ValErr(1.21444, 0.0325734, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0122428, None, -0.000235027, None, -0.00773402, None, -0.000244043, None, -0.00773402, None, -0.000244043, None, -0.0284656, None, -0.000322533, None, -0.0284656, None, -0.000322533, None, 1.21457, None, 0.00868306, None, 1.21457, None, 0.00868306, None)
reports[-1].CovMatrix = ['0.00219261','-9.59535e-06','7.89294e-07','0','0','0','0','0','0','-9.59535e-06','1.30628e-06','1.92333e-08','0','0','0','0','0','0','7.89294e-07','1.92333e-08','0.00106106','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051608, ("CSC", 2, 1, 3, 19), "MEm13_19"))
reports[-1].posNum = 741
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0286787, 0.0453795, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000743215, 0.00108398, 0), \
                           -1194.55, 741, 741, -nan)
reports[-1].sigmaresid = ValErr(1.2131, 0.0315128, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0448793, None, -8.64802e-05, None, -0.0228146, None, -0.000244329, None, -0.0228146, None, -0.000244329, None, -0.0305435, None, -0.000168156, None, -0.0305435, None, -0.000168156, None, 1.21344, None, 0.00833736, None, 1.21344, None, 0.00833736, None)
reports[-1].CovMatrix = ['0.0020593','-9.28134e-06','7.04028e-07','0','0','0','0','0','0','-9.28134e-06','1.17501e-06','2.23675e-08','0','0','0','0','0','0','7.04028e-07','2.23675e-08','0.00099309','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051616, ("CSC", 2, 1, 3, 20), "MEm13_20"))
reports[-1].posNum = 737
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.028158, 0.0484444, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000552714, 0.00113162, 0), \
                           -1242.25, 737, 737, -nan)
reports[-1].sigmaresid = ValErr(1.30564, 0.0340105, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0748008, None, -0.001059, None, -0.0252249, None, -0.0012011, None, -0.0252249, None, -0.0012011, None, -0.0590409, None, -0.00119276, None, -0.0590409, None, -0.00119276, None, 1.30575, None, 0.00843035, None, 1.30575, None, 0.00843035, None)
reports[-1].CovMatrix = ['0.00234686','-6.58312e-06','7.82603e-07','0','0','0','0','0','0','-6.58312e-06','1.28057e-06','1.8316e-08','0','0','0','0','0','0','7.82603e-07','1.8316e-08','0.00115676','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051624, ("CSC", 2, 1, 3, 21), "MEm13_21"))
reports[-1].posNum = 638
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000431418, 0.054343, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000262896, 0.00126459, 0), \
                           -1100.12, 638, 638, -nan)
reports[-1].sigmaresid = ValErr(1.35716, 0.0379924, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00291967, None, 0.00347637, None, -0.00126092, None, 0.0033925, None, -0.00126092, None, 0.0033925, None, -0.0708762, None, 0.00393859, None, -0.0708762, None, 0.00393859, None, 1.3572, None, 0.00974407, None, 1.3572, None, 0.00974407, None)
reports[-1].CovMatrix = ['0.00295317','-1.02898e-05','1.1395e-06','0','0','0','0','0','0','-1.02898e-05','1.59918e-06','2.64365e-08','0','0','0','0','0','0','1.1395e-06','2.64365e-08','0.00144348','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051632, ("CSC", 2, 1, 3, 22), "MEm13_22"))
reports[-1].posNum = 686
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00771335, 0.0503421, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000871549, 0.00121115, 0), \
                           -1157.83, 686, 686, -nan)
reports[-1].sigmaresid = ValErr(1.30848, 0.035325, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00673511, None, 0.00071184, None, -0.0121826, None, 0.00103965, None, -0.0121826, None, 0.00103965, None, -0.0370446, None, 0.000840372, None, -0.0370446, None, 0.000840372, None, 1.30897, None, 0.0095361, None, 1.30897, None, 0.0095361, None)
reports[-1].CovMatrix = ['0.00253433','-7.51732e-06','1.00153e-06','0','0','0','0','0','0','-7.51732e-06','1.46687e-06','2.39357e-08','0','0','0','0','0','0','1.00153e-06','2.39357e-08','0.0012479','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051640, ("CSC", 2, 1, 3, 23), "MEm13_23"))
reports[-1].posNum = 454
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051648, ("CSC", 2, 1, 3, 24), "MEm13_24"))
reports[-1].posNum = 564
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00568486, 0.0509842, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000341232, 0.00120589, 0), \
                           -908.111, 564, 564, -nan)
reports[-1].sigmaresid = ValErr(1.21069, 0.0360469, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0113666, None, -0.00186046, None, -0.00590454, None, -0.00144472, None, -0.00590454, None, -0.00144472, None, 0.125767, None, -0.00187916, None, 0.125767, None, -0.00187916, None, 1.21077, None, 0.00719036, None, 1.21077, None, 0.00719036, None)
reports[-1].CovMatrix = ['0.00259939','-8.73016e-07','1.15402e-06','0','0','0','0','0','0','-8.73016e-07','1.45418e-06','2.67108e-08','0','0','0','0','0','0','1.15402e-06','2.67108e-08','0.00129943','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051656, ("CSC", 2, 1, 3, 25), "MEm13_25"))
reports[-1].posNum = 395
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051664, ("CSC", 2, 1, 3, 26), "MEm13_26"))
reports[-1].posNum = 429
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051672, ("CSC", 2, 1, 3, 27), "MEm13_27"))
reports[-1].posNum = 298
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051680, ("CSC", 2, 1, 3, 28), "MEm13_28"))
reports[-1].posNum = 380
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051688, ("CSC", 2, 1, 3, 29), "MEm13_29"))
reports[-1].posNum = 379
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051696, ("CSC", 2, 1, 3, 30), "MEm13_30"))
reports[-1].posNum = 126
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051704, ("CSC", 2, 1, 3, 31), "MEm13_31"))
reports[-1].posNum = 64
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051712, ("CSC", 2, 1, 3, 32), "MEm13_32"))
reports[-1].posNum = 193
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051720, ("CSC", 2, 1, 3, 33), "MEm13_33"))
reports[-1].posNum = 493
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051728, ("CSC", 2, 1, 3, 34), "MEm13_34"))
reports[-1].posNum = 706
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0215148, 0.0477287, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000322767, 0.00111603, 0), \
                           -1160.75, 706, 706, -nan)
reports[-1].sigmaresid = ValErr(1.25255, 0.0333326, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0301635, None, -0.00117133, None, -0.0193535, None, -0.000636445, None, -0.0193535, None, -0.000636445, None, -0.0228155, None, -0.000405476, None, -0.0228155, None, -0.000405476, None, 1.25262, None, 0.00948196, None, 1.25262, None, 0.00948196, None)
reports[-1].CovMatrix = ['0.00227803','-8.33882e-06','8.49646e-07','0','0','0','0','0','0','-8.33882e-06','1.24551e-06','1.98566e-08','0','0','0','0','0','0','8.49646e-07','1.98566e-08','0.0011111','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051736, ("CSC", 2, 1, 3, 35), "MEm13_35"))
reports[-1].posNum = 669
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.022824, 0.0516909, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000806001, 0.00124342, 0), \
                           -1133.05, 669, 669, -nan)
reports[-1].sigmaresid = ValErr(1.31615, 0.0359806, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0536697, None, 5.03966e-05, None, 0.0169347, None, 0.000183757, None, 0.0169347, None, 0.000183757, None, -0.0616323, None, 0.00064092, None, -0.0616323, None, 0.00064092, None, 1.31656, None, 0.00956149, None, 1.31656, None, 0.00956149, None)
reports[-1].CovMatrix = ['0.00267195','-1.13031e-05','9.83075e-07','0','0','0','0','0','0','-1.13031e-05','1.54609e-06','2.37489e-08','0','0','0','0','0','0','9.83075e-07','2.37489e-08','0.00129466','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051744, ("CSC", 2, 1, 3, 36), "MEm13_36"))
reports[-1].posNum = 625
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0604116, 0.0495697, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000581516, 0.00115725, 0), \
                           -1007.38, 625, 625, -nan)
reports[-1].sigmaresid = ValErr(1.21273, 0.0343007, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0826049, None, -0.00270609, None, -0.0552861, None, -0.00248994, None, -0.0552861, None, -0.00248994, None, -0.0121815, None, -0.00275103, None, -0.0121815, None, -0.00275103, None, 1.21298, None, 0.00894909, None, 1.21298, None, 0.00894909, None)
reports[-1].CovMatrix = ['0.00245716','-1.18015e-05','8.53368e-07','0','0','0','0','0','0','-1.18015e-05','1.33922e-06','1.9923e-08','0','0','0','0','0','0','8.53368e-07','1.9923e-08','0.00117658','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604049928, ("CSC", 2, 1, 4, 1), "MEm14_01"))
reports[-1].posNum = 3009
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00168225, 0.0032329, 0), \
                           ValErr(0.0519939, 0.0811996, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000135125, 8.71327e-05, 0), \
                           997.028, 3009, 3009, -nan)
reports[-1].sigmaresid = ValErr(0.173724, 0.00223941, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.003977, None, -3.97423e-05, None, 0.000621757, None, 6.90153e-05, None, 0.000621757, None, 6.90153e-05, None, 0.00431327, None, 3.16026e-06, None, 0.00431327, None, 3.16026e-06, None, 0.173804, None, 0.0065559, None, 0.173804, None, 0.0065559, None)
reports[-1].CovMatrix = ['1.04516e-05','1.03066e-05','-5.57119e-08','1.73852e-09','0','0','0','0','0','1.03066e-05','0.00659337','-1.48361e-07','5.15451e-08','0','0','0','0','0','-5.57119e-08','-1.48361e-07','7.5921e-09','4.38973e-11','0','0','0','0','0','1.73852e-09','5.15451e-08','4.38973e-11','5.01495e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604049944, ("CSC", 2, 1, 4, 3), "MEm14_03"))
reports[-1].posNum = 2661
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00380697, 0.00344195, 0), \
                           ValErr(0.0366758, 0.0860818, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000128865, 9.30815e-05, 0), \
                           884.298, 2661, 2661, -nan)
reports[-1].sigmaresid = ValErr(0.173556, 0.00237903, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00058296, None, 0.000232186, None, 0.00277838, None, 0.000411005, None, 0.00277838, None, 0.000411005, None, -0.00109469, None, 0.000460705, None, -0.00109469, None, 0.000460705, None, 0.173625, None, 0.00619539, None, 0.173625, None, 0.00619539, None)
reports[-1].CovMatrix = ['1.1847e-05','4.55772e-06','-6.73553e-08','1.87732e-09','0','0','0','0','0','4.55772e-06','0.00741007','9.17934e-08','5.87033e-08','0','0','0','0','0','-6.73553e-08','9.17934e-08','8.66417e-09','5.13151e-11','0','0','0','0','0','1.87732e-09','5.87033e-08','5.13151e-11','5.6598e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604049960, ("CSC", 2, 1, 4, 5), "MEm14_05"))
reports[-1].posNum = 2944
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00331113, 0.00322543, 0), \
                           ValErr(0.0605605, 0.0813082, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00012693, 8.6081e-05, 0), \
                           994.511, 2944, 2944, -nan)
reports[-1].sigmaresid = ValErr(0.172605, 0.00224942, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000416466, None, -6.79426e-05, None, 0.00258903, None, 3.47575e-05, None, 0.00258903, None, 3.47575e-05, None, 0.00451441, None, -0.00015918, None, 0.00451441, None, -0.00015918, None, 0.172685, None, 0.00564097, None, 0.172685, None, 0.00564097, None)
reports[-1].CovMatrix = ['1.04034e-05','-5.69812e-06','-4.53855e-08','1.68091e-09','0','0','0','0','0','-5.69812e-06','0.00661102','-6.97444e-08','4.9523e-08','0','0','0','0','0','-4.53855e-08','-6.97444e-08','7.40994e-09','4.63484e-11','0','0','0','0','0','1.68091e-09','4.9523e-08','4.63484e-11','5.05988e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604049976, ("CSC", 2, 1, 4, 7), "MEm14_07"))
reports[-1].posNum = 2264
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00408325, 0.00384297, 0), \
                           ValErr(-0.097156, 0.0949043, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000187368, 0.000105259, 0), \
                           647.096, 2264, 2264, -nan)
reports[-1].sigmaresid = ValErr(0.181819, 0.00270204, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00467856, None, 0.000440488, None, 0.00328146, None, -0.000139037, None, 0.00328146, None, -0.000139037, None, 0.0086681, None, 8.10328e-05, None, 0.0086681, None, 8.10328e-05, None, 0.181981, None, 0.00575076, None, 0.181981, None, 0.00575076, None)
reports[-1].CovMatrix = ['1.47685e-05','-1.06333e-05','-4.16741e-08','2.3143e-09','0','0','0','0','0','-1.06333e-05','0.00900683','2.90737e-07','6.64367e-08','0','0','0','0','0','-4.16741e-08','2.90737e-07','1.10795e-08','6.71437e-11','0','0','0','0','0','2.3143e-09','6.64367e-08','6.71437e-11','7.30102e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604049992, ("CSC", 2, 1, 4, 9), "MEm14_09"))
reports[-1].posNum = 2783
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00545351, 0.00324724, 0), \
                           ValErr(0.0110943, 0.0815436, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000169187, 8.72521e-05, 0), \
                           1027.89, 2783, 2783, -nan)
reports[-1].sigmaresid = ValErr(0.167246, 0.00224173, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00422734, None, 0.000338404, None, 0.00411461, None, 0.000440406, None, 0.00411461, None, 0.000440406, None, 0.00383306, None, 0.000254961, None, 0.00383306, None, 0.000254961, None, 0.167361, None, 0.0057359, None, 0.167361, None, 0.0057359, None)
reports[-1].CovMatrix = ['1.05446e-05','-8.20823e-06','-6.10122e-08','1.58354e-09','0','0','0','0','0','-8.20823e-06','0.00664936','3.21581e-07','5.1626e-08','0','0','0','0','0','-6.10122e-08','3.21581e-07','7.61292e-09','4.87656e-11','0','0','0','0','0','1.58354e-09','5.1626e-08','4.87656e-11','5.02537e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050008, ("CSC", 2, 1, 4, 11), "MEm14_11"))
reports[-1].posNum = 2738
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00476944, 0.00329695, 0), \
                           ValErr(-0.00071433, 0.0818436, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000112482, 8.67637e-05, 0), \
                           1023.36, 2738, 2738, -nan)
reports[-1].sigmaresid = ValErr(0.16651, 0.00225012, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00266299, None, -0.00186734, None, 0.00365215, None, -0.00203655, None, 0.00365215, None, -0.00203655, None, 0.0028626, None, -0.00185018, None, 0.0028626, None, -0.00185018, None, 0.166561, None, 0.00585705, None, 0.166561, None, 0.00585705, None)
reports[-1].CovMatrix = ['1.08699e-05','3.06115e-06','-7.48074e-08','1.73176e-09','0','0','0','0','0','3.06115e-06','0.00669838','-1.5068e-07','5.60959e-08','0','0','0','0','0','-7.48074e-08','-1.5068e-07','7.52795e-09','4.34533e-11','0','0','0','0','0','1.73176e-09','5.60959e-08','4.34533e-11','5.06305e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050024, ("CSC", 2, 1, 4, 13), "MEm14_13"))
reports[-1].posNum = 2600
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00189239, 0.00355535, 0), \
                           ValErr(0.01849, 0.088799, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000136565, 9.57832e-05, 0), \
                           791.504, 2600, 2600, -nan)
reports[-1].sigmaresid = ValErr(0.178465, 0.00247485, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00765603, None, -0.002079, None, 0.00099112, None, -0.00210784, None, 0.00099112, None, -0.00210784, None, -0.00411562, None, -0.00204177, None, -0.00411562, None, -0.00204177, None, 0.178536, None, 0.0060059, None, 0.178536, None, 0.0060059, None)
reports[-1].CovMatrix = ['1.26405e-05','6.05479e-06','-5.94602e-08','2.06142e-09','0','0','0','0','0','6.05479e-06','0.00788526','6.26388e-08','6.09268e-08','0','0','0','0','0','-5.94602e-08','6.26388e-08','9.17443e-09','5.25179e-11','0','0','0','0','0','2.06142e-09','6.09268e-08','5.25179e-11','6.12489e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050040, ("CSC", 2, 1, 4, 15), "MEm14_15"))
reports[-1].posNum = 2250
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00432, 0.00374848, 0), \
                           ValErr(-0.0148348, 0.093188, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000178085, 9.96979e-05, 0), \
                           799.922, 2250, 2250, -nan)
reports[-1].sigmaresid = ValErr(0.169572, 0.00252779, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00256373, None, 0.000371193, None, 0.00230679, None, 0.000196768, None, 0.00230679, None, 0.000196768, None, -0.00565584, None, 0.000214969, None, -0.00565584, None, 0.000214969, None, 0.169696, None, 0.0055431, None, 0.169696, None, 0.0055431, None)
reports[-1].CovMatrix = ['1.40511e-05','-1.48859e-06','-1.12392e-07','2.20327e-09','0','0','0','0','0','-1.48859e-06','0.008684','2.83917e-07','7.54188e-08','0','0','0','0','0','-1.12392e-07','2.83917e-07','9.93968e-09','4.89644e-11','0','0','0','0','0','2.20327e-09','7.54188e-08','4.89644e-11','6.38971e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050056, ("CSC", 2, 1, 4, 17), "MEm14_17"))
reports[-1].posNum = 2010
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00330476, 0.00379056, 0), \
                           ValErr(0.112278, 0.0936765, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.00748e-05, 0.000100578, 0), \
                           731.41, 2010, 2010, -nan)
reports[-1].sigmaresid = ValErr(0.168163, 0.00265226, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00447456, None, -0.000998694, None, 0.00281369, None, -0.000935287, None, 0.00281369, None, -0.000935287, None, 0.000150355, None, -0.000934436, None, 0.000150355, None, -0.000934436, None, 0.168252, None, 0.00555485, None, 0.168252, None, 0.00555485, None)
reports[-1].CovMatrix = ['1.43684e-05','2.88462e-06','-5.48319e-08','2.58089e-09','0','0','0','0','0','2.88462e-06','0.00877528','2.74526e-07','7.57921e-08','0','0','0','0','0','-5.48319e-08','2.74526e-07','1.01158e-08','7.03937e-11','0','0','0','0','0','2.58089e-09','7.57921e-08','7.03937e-11','7.03448e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050072, ("CSC", 2, 1, 4, 19), "MEm14_19"))
reports[-1].posNum = 2540
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00105092, 0.00338065, 0), \
                           ValErr(-0.033596, 0.0866036, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.03735e-05, 9.51825e-05, 0), \
                           909.64, 2540, 2540, -nan)
reports[-1].sigmaresid = ValErr(0.169134, 0.00237301, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(9.39137e-06, None, -0.00529498, None, 0.000730482, None, -0.00514523, None, 0.000730482, None, -0.00514523, None, 0.00112328, None, -0.00526652, None, 0.00112328, None, -0.00526652, None, 0.169154, None, 0.00476693, None, 0.169154, None, 0.00476693, None)
reports[-1].CovMatrix = ['1.14288e-05','-1.77125e-05','-3.11698e-08','1.99274e-09','0','0','0','0','0','-1.77125e-05','0.00750019','-9.3677e-07','4.98724e-08','0','0','0','0','0','-3.11698e-08','-9.3677e-07','9.05971e-09','5.28142e-11','0','0','0','0','0','1.99274e-09','4.98724e-08','5.28142e-11','5.63117e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050088, ("CSC", 2, 1, 4, 21), "MEm14_21"))
reports[-1].posNum = 2772
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00388837, 0.00330843, 0), \
                           ValErr(-0.0443521, 0.0831126, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000145371, 8.94969e-05, 0), \
                           945.743, 2772, 2772, -nan)
reports[-1].sigmaresid = ValErr(0.172025, 0.00231036, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00302985, None, -0.00471159, None, 0.00304091, None, -0.00452618, None, 0.00304091, None, -0.00452618, None, 0.00341027, None, -0.0044695, None, 0.00341027, None, -0.0044695, None, 0.172116, None, 0.00639095, None, 0.172116, None, 0.00639095, None)
reports[-1].CovMatrix = ['1.09457e-05','-4.86274e-07','-4.65127e-08','1.83408e-09','0','0','0','0','0','-4.86274e-07','0.0069077','-1.22876e-08','5.51989e-08','0','0','0','0','0','-4.65127e-08','-1.22876e-08','8.00969e-09','5.07103e-11','0','0','0','0','0','1.83408e-09','5.51989e-08','5.07103e-11','5.33776e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050104, ("CSC", 2, 1, 4, 23), "MEm14_23"))
reports[-1].posNum = 2641
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00265401, 0.00340246, 0), \
                           ValErr(-0.0336965, 0.0859368, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000108811, 9.24207e-05, 0), \
                           892.915, 2641, 2641, -nan)
reports[-1].sigmaresid = ValErr(0.172555, 0.00237426, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00139229, None, -0.00122294, None, 0.00201314, None, -0.00126547, None, 0.00201314, None, -0.00126547, None, -0.00352917, None, -0.00126055, None, -0.00352917, None, -0.00126055, None, 0.172605, None, 0.00541866, None, 0.172605, None, 0.00541866, None)
reports[-1].CovMatrix = ['1.15768e-05','3.68095e-07','-5.08052e-08','1.94138e-09','0','0','0','0','0','3.68095e-07','0.00738514','1.83925e-07','5.98165e-08','0','0','0','0','0','-5.08052e-08','1.83925e-07','8.54158e-09','5.46646e-11','0','0','0','0','0','1.94138e-09','5.98165e-08','5.46646e-11','5.63713e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050120, ("CSC", 2, 1, 4, 25), "MEm14_25"))
reports[-1].posNum = 2890
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00443616, 0.00319553, 0), \
                           ValErr(0.0250348, 0.0807679, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.98477e-05, 8.54013e-05, 0), \
                           1058.84, 2890, 2890, -nan)
reports[-1].sigmaresid = ValErr(0.167743, 0.00220637, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00567063, None, 0.00368576, None, 0.00371941, None, 0.00378939, None, 0.00371941, None, 0.00378939, None, 0.00563393, None, 0.00379228, None, 0.00563393, None, 0.00379228, None, 0.167779, None, 0.0050626, None, 0.167779, None, 0.0050626, None)
reports[-1].CovMatrix = ['1.02114e-05','-3.89217e-06','-5.88339e-08','1.65611e-09','0','0','0','0','0','-3.89217e-06','0.00652345','2.40642e-07','5.08685e-08','0','0','0','0','0','-5.88339e-08','2.40642e-07','7.29337e-09','4.75677e-11','0','0','0','0','0','1.65611e-09','5.08685e-08','4.75677e-11','4.86808e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050136, ("CSC", 2, 1, 4, 27), "MEm14_27"))
reports[-1].posNum = 2612
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00156862, 0.00334665, 0), \
                           ValErr(0.00963323, 0.0841634, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000113048, 8.9769e-05, 0), \
                           963.288, 2612, 2612, -nan)
reports[-1].sigmaresid = ValErr(0.167339, 0.00231524, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0031857, None, -9.03666e-05, None, 0.000694313, None, 6.58176e-05, None, 0.000694313, None, 6.58176e-05, None, 0.000805512, None, 9.45423e-05, None, 0.000805512, None, 9.45423e-05, None, 0.16739, None, 0.00611069, None, 0.16739, None, 0.00611069, None)
reports[-1].CovMatrix = ['1.12e-05','5.58441e-06','-6.19576e-08','1.91048e-09','0','0','0','0','0','5.58441e-06','0.00708347','-1.2546e-07','5.81112e-08','0','0','0','0','0','-6.19576e-08','-1.2546e-07','8.05847e-09','4.87763e-11','0','0','0','0','0','1.91048e-09','5.81112e-08','4.87763e-11','5.36033e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050152, ("CSC", 2, 1, 4, 29), "MEm14_29"))
reports[-1].posNum = 2805
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00129471, 0.00332566, 0), \
                           ValErr(0.0686816, 0.0829093, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000101875, 8.6739e-05, 0), \
                           936.973, 2805, 2805, -nan)
reports[-1].sigmaresid = ValErr(0.173258, 0.00231319, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00416176, None, 0.000776118, None, 0.000533556, None, 0.000844386, None, 0.000533556, None, 0.000844386, None, -0.0111946, None, 0.000761432, None, -0.0111946, None, 0.000761432, None, 0.173321, None, 0.00535934, None, 0.173321, None, 0.00535934, None)
reports[-1].CovMatrix = ['1.106e-05','6.65904e-06','-5.14782e-08','1.8557e-09','0','0','0','0','0','6.65904e-06','0.00687395','-2.8236e-08','5.44219e-08','0','0','0','0','0','-5.14782e-08','-2.8236e-08','7.52366e-09','4.71196e-11','0','0','0','0','0','1.8557e-09','5.44219e-08','4.71196e-11','5.35085e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050168, ("CSC", 2, 1, 4, 31), "MEm14_31"))
reports[-1].posNum = 2731
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(2.47875e-05, 0.00328758, 0), \
                           ValErr(0.047627, 0.0821393, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000133293, 8.90287e-05, 0), \
                           1004.42, 2731, 2731, -nan)
reports[-1].sigmaresid = ValErr(0.167508, 0.00226651, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00322673, None, -0.000301637, None, -0.00108158, None, -0.000324354, None, -0.00108158, None, -0.000324354, None, 0.00359293, None, -0.000271048, None, 0.00359293, None, -0.000271048, None, 0.167585, None, 0.00563929, None, 0.167585, None, 0.00563929, None)
reports[-1].CovMatrix = ['1.08082e-05','4.33336e-06','-6.50227e-08','1.79842e-09','0','0','0','0','0','4.33336e-06','0.00674687','-2.82403e-07','5.04297e-08','0','0','0','0','0','-6.50227e-08','-2.82403e-07','7.92612e-09','4.52392e-11','0','0','0','0','0','1.79842e-09','5.04297e-08','4.52392e-11','5.13705e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050184, ("CSC", 2, 1, 4, 33), "MEm14_33"))
reports[-1].posNum = 2814
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00147568, 0.00329763, 0), \
                           ValErr(0.0419533, 0.083052, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000175792, 8.80841e-05, 0), \
                           975.034, 2814, 2814, -nan)
reports[-1].sigmaresid = ValErr(0.171113, 0.0022809, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00191974, None, 0.000589696, None, 9.27267e-05, None, 0.000747479, None, 9.27267e-05, None, 0.000747479, None, 0.00362361, None, 0.000705302, None, 0.00362361, None, 0.000705302, None, 0.171239, None, 0.00579425, None, 0.171239, None, 0.00579425, None)
reports[-1].CovMatrix = ['1.08744e-05','6.32376e-06','-6.02186e-08','1.79709e-09','0','0','0','0','0','6.32376e-06','0.00689763','-3.35048e-07','5.239e-08','0','0','0','0','0','-6.02186e-08','-3.35048e-07','7.7588e-09','4.46189e-11','0','0','0','0','0','1.79709e-09','5.239e-08','4.46189e-11','5.20249e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050200, ("CSC", 2, 1, 4, 35), "MEm14_35"))
reports[-1].posNum = 2632
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00391142, 0.00336497, 0), \
                           ValErr(0.00194316, 0.0832221, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00017788, 8.98261e-05, 0), \
                           946.82, 2632, 2632, -nan)
reports[-1].sigmaresid = ValErr(0.168862, 0.00232742, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00196295, None, -0.000493217, None, 0.00252663, None, -0.000334907, None, 0.00252663, None, -0.000334907, None, -0.00401667, None, -0.000162384, None, -0.00401667, None, -0.000162384, None, 0.168988, None, 0.00573173, None, 0.168988, None, 0.00573173, None)
reports[-1].CovMatrix = ['1.1323e-05','-1.06232e-06','-6.28311e-08','1.82888e-09','0','0','0','0','0','-1.06232e-06','0.00692591','1.08234e-07','5.68403e-08','0','0','0','0','0','-6.28311e-08','1.08234e-07','8.06872e-09','5.11005e-11','0','0','0','0','0','1.82888e-09','5.68403e-08','5.11005e-11','5.41687e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604049936, ("CSC", 2, 1, 4, 2), "MEm14_02"))
reports[-1].posNum = 2958
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00449689, 0.00354584, 0), \
                           ValErr(0.0482856, 0.0723025, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.75287e-05, 9.34313e-05, 0), \
                           1392.12, 2958, 2958, -nan)
reports[-1].sigmaresid = ValErr(0.151137, 0.00196758, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00417311, None, 0.00171465, None, 0.00371449, None, 0.00204004, None, 0.00371449, None, 0.00204004, None, 0.00408298, None, 0.00188978, None, 0.00408298, None, 0.00188978, None, 0.15119, None, 0.00866751, None, 0.15119, None, 0.00866751, None)
reports[-1].CovMatrix = ['1.2573e-05','-1.5897e-05','-1.646e-07','1.94301e-07','0','0','0','0','0','-1.5897e-05','0.00522765','1.98154e-07','-5.08897e-07','0','0','0','0','0','-1.646e-07','1.98154e-07','8.7294e-09','-5.06872e-09','0','0','0','0','0','1.94301e-07','-5.08897e-07','-5.06872e-09','3.87139e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604049952, ("CSC", 2, 1, 4, 4), "MEm14_04"))
reports[-1].posNum = 2557
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00269613, 0.00319448, 0), \
                           ValErr(-0.0118983, 0.112315, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.1567e-05, 8.56907e-05, 0), \
                           1143.07, 2557, 2557, -nan)
reports[-1].sigmaresid = ValErr(0.154745, 0.00217582, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00648922, None, 0.00208149, None, 0.00195587, None, 0.0020789, None, 0.00195587, None, 0.0020789, None, 0.0018959, None, 0.00212598, None, 0.0018959, None, 0.00212598, None, 0.154781, None, 0.00528417, None, 0.154781, None, 0.00528417, None)
reports[-1].CovMatrix = ['1.02047e-05','-4.84414e-05','-6.4859e-08','-1.33953e-07','0','0','0','0','0','-4.84414e-05','0.0126146','8.48493e-07','1.83464e-05','0','0','0','0','0','-6.4859e-08','8.48493e-07','7.3429e-09','2.37097e-09','0','0','0','0','0','-1.33953e-07','1.83464e-05','2.37097e-09','4.7342e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604049968, ("CSC", 2, 1, 4, 6), "MEm14_06"))
reports[-1].posNum = 2870
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00215034, 0.00293634, 0), \
                           ValErr(0.0593807, 0.110924, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000138165, 7.94613e-05, 0), \
                           1300.42, 2870, 2870, -nan)
reports[-1].sigmaresid = ValErr(0.153809, 0.00203563, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00258183, None, 0.00128004, None, 0.00126804, None, 0.00148455, None, 0.00126804, None, 0.00148455, None, 0.00274501, None, 0.00166073, None, 0.00274501, None, 0.00166073, None, 0.153908, None, 0.00615217, None, 0.153908, None, 0.00615217, None)
reports[-1].CovMatrix = ['8.62208e-06','-2.26727e-05','-4.12089e-08','5.04632e-09','0','0','0','0','0','-2.26727e-05','0.0123041','1.06771e-06','1.31296e-06','0','0','0','0','0','-4.12089e-08','1.06771e-06','6.3141e-09','3.28127e-10','0','0','0','0','0','5.04632e-09','1.31296e-06','3.28127e-10','4.1438e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604049984, ("CSC", 2, 1, 4, 8), "MEm14_08"))
reports[-1].posNum = 2761
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00521161, 0.00292682, 0), \
                           ValErr(0.0715049, 0.116198, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000183952, 8.07613e-05, 0), \
                           1332.12, 2761, 2761, -nan)
reports[-1].sigmaresid = ValErr(0.149356, 0.00202437, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000506595, None, 0.000506599, None, 0.00348696, None, 0.000408712, None, 0.00348696, None, 0.000408712, None, -0.00236641, None, 0.000489414, None, -0.00236641, None, 0.000489414, None, 0.149537, None, 0.00672423, None, 0.149537, None, 0.00672423, None)
reports[-1].CovMatrix = ['8.56629e-06','-1.07969e-06','-5.39122e-08','-3.11418e-09','0','0','0','0','0','-1.07969e-06','0.013502','2.29235e-06','2.64822e-07','0','0','0','0','0','-5.39122e-08','2.29235e-06','6.52239e-09','-4.17853e-11','0','0','0','0','0','-3.11418e-09','2.64822e-07','-4.17853e-11','4.09807e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050000, ("CSC", 2, 1, 4, 10), "MEm14_10"))
reports[-1].posNum = 2805
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00241506, 0.00293459, 0), \
                           ValErr(0.0419377, 0.111514, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.82848e-05, 7.99599e-05, 0), \
                           1290.37, 2805, 2805, -nan)
reports[-1].sigmaresid = ValErr(0.152747, 0.00206438, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000149675, None, 0.000495713, None, 0.00179512, None, 0.000723542, None, 0.00179512, None, 0.000723542, None, 0.00581986, None, 0.000381926, None, 0.00581986, None, 0.000381926, None, 0.152792, None, 0.00935244, None, 0.152792, None, 0.00935244, None)
reports[-1].CovMatrix = ['8.61185e-06','3.6682e-06','-4.25619e-08','-1.22981e-10','0','0','0','0','0','3.6682e-06','0.0124354','9.85576e-07','2.32103e-06','0','0','0','0','0','-4.25619e-08','9.85576e-07','6.39358e-09','7.16192e-10','0','0','0','0','0','-1.22981e-10','2.32103e-06','7.16192e-10','4.26169e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050016, ("CSC", 2, 1, 4, 12), "MEm14_12"))
reports[-1].posNum = 2934
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00302264, 0.00290031, 0), \
                           ValErr(0.0156256, 0.110151, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000123688, 7.56303e-05, 0), \
                           1356.92, 2934, 2934, -nan)
reports[-1].sigmaresid = ValErr(0.152371, 0.00203891, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00255266, None, -0.000539838, None, 0.00211526, None, -0.000350811, None, 0.00211526, None, -0.000350811, None, 0.00390938, None, -0.00043942, None, 0.00390938, None, -0.00043942, None, 0.152444, None, 0.00776664, None, 0.152444, None, 0.00776664, None)
reports[-1].CovMatrix = ['8.4118e-06','-3.84288e-05','-4.1132e-08','-2.67661e-08','0','0','0','0','0','-3.84288e-05','0.0121332','-2.66651e-07','3.67414e-07','0','0','0','0','0','-4.1132e-08','-2.66651e-07','5.71994e-09','1.49691e-09','0','0','0','0','0','-2.67661e-08','3.67414e-07','1.49691e-09','4.15716e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050032, ("CSC", 2, 1, 4, 14), "MEm14_14"))
reports[-1].posNum = 2950
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000471887, 0.00293601, 0), \
                           ValErr(-0.0347057, 0.0724065, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.14199e-05, 7.77484e-05, 0), \
                           1303.93, 2950, 2950, -nan)
reports[-1].sigmaresid = ValErr(0.155525, 0.00202477, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00279078, None, -0.000838141, None, -0.00120007, None, -0.000697262, None, -0.00120007, None, -0.000697262, None, 0.0078857, None, -0.000632886, None, 0.0078857, None, -0.000632886, None, 0.155568, None, 0.00616737, None, 0.155568, None, 0.00616737, None)
reports[-1].CovMatrix = ['8.62015e-06','5.18429e-06','-5.02105e-08','1.54248e-09','0','0','0','0','0','5.18429e-06','0.00524271','-9.16807e-08','4.88463e-08','0','0','0','0','0','-5.02105e-08','-9.16807e-08','6.04481e-09','4.12523e-11','0','0','0','0','0','1.54248e-09','4.88463e-08','4.12523e-11','4.09969e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050048, ("CSC", 2, 1, 4, 16), "MEm14_16"))
reports[-1].posNum = 2586
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00432139, 0.00310737, 0), \
                           ValErr(0.0456609, 0.117725, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000138114, 7.96805e-05, 0), \
                           1195.28, 2586, 2586, -nan)
reports[-1].sigmaresid = ValErr(0.152414, 0.00214111, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000463445, None, -0.0010522, None, 0.0029784, None, -0.00113781, None, 0.0029784, None, -0.00113781, None, 0.000708142, None, -0.00111586, None, 0.000708142, None, -0.00111586, None, 0.152514, None, 0.00572119, None, 0.152514, None, 0.00572119, None)
reports[-1].CovMatrix = ['9.65573e-06','-2.4124e-05','-6.27011e-08','-7.02802e-09','0','0','0','0','0','-2.4124e-05','0.0138592','4.69106e-07','2.54459e-06','0','0','0','0','0','-6.27011e-08','4.69106e-07','6.34899e-09','5.07939e-10','0','0','0','0','0','-7.02802e-09','2.54459e-06','5.07939e-10','4.58434e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050064, ("CSC", 2, 1, 4, 18), "MEm14_18"))
reports[-1].posNum = 3071
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00381964, 0.00282575, 0), \
                           ValErr(0.00747289, 0.109055, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.51493e-05, 7.5427e-05, 0), \
                           1396.51, 3071, 3071, -nan)
reports[-1].sigmaresid = ValErr(0.153557, 0.00197426, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00079894, None, -0.00204476, None, 0.00311958, None, -0.00188603, None, 0.00311958, None, -0.00188603, None, 0.0049934, None, -0.00200906, None, 0.0049934, None, -0.00200906, None, 0.153598, None, 0.0066506, None, 0.153598, None, 0.0066506, None)
reports[-1].CovMatrix = ['7.98488e-06','8.56597e-06','-4.0641e-08','-1.83473e-09','0','0','0','0','0','8.56597e-06','0.011893','6.34221e-07','7.61816e-08','0','0','0','0','0','-4.0641e-08','6.34221e-07','5.68923e-09','-1.41657e-10','0','0','0','0','0','-1.83473e-09','7.61816e-08','-1.41657e-10','3.89772e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050080, ("CSC", 2, 1, 4, 20), "MEm14_20"))
reports[-1].posNum = 2872
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00620042, 0.00367432, 0), \
                           ValErr(-0.020662, 0.0756643, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000134476, 9.18532e-05, 0), \
                           1356.59, 2872, 2872, -nan)
reports[-1].sigmaresid = ValErr(0.150877, 0.00199174, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00602865, None, 0.00144423, None, 0.00505592, None, 0.00137527, None, 0.00505592, None, 0.00137527, None, 0.00351003, None, 0.0014683, None, 0.00351003, None, 0.0014683, None, 0.150962, None, 0.00538397, None, 0.150962, None, 0.00538397, None)
reports[-1].CovMatrix = ['1.35006e-05','-2.46976e-05','-1.66537e-07','7.43325e-08','0','0','0','0','0','-2.46976e-05','0.00572509','4.35508e-07','-3.71722e-07','0','0','0','0','0','-1.66537e-07','4.35508e-07','8.43701e-09','-1.6486e-09','0','0','0','0','0','7.43325e-08','-3.71722e-07','-1.6486e-09','3.96705e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050096, ("CSC", 2, 1, 4, 22), "MEm14_22"))
reports[-1].posNum = 2905
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000755999, 0.0029653, 0), \
                           ValErr(0.00480509, 0.110464, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.22301e-05, 7.98862e-05, 0), \
                           1349.7, 2905, 2905, -nan)
reports[-1].sigmaresid = ValErr(0.152047, 0.00214597, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00130701, None, -0.00167079, None, 0.000245654, None, -0.00138685, None, 0.000245654, None, -0.00138685, None, -0.00582312, None, -0.0015034, None, -0.00582312, None, -0.0015034, None, 0.152066, None, 0.00623662, None, 0.152066, None, 0.00623662, None)
reports[-1].CovMatrix = ['8.793e-06','-2.67217e-06','-6.22701e-08','-5.12323e-07','0','0','0','0','0','-2.67217e-06','0.0122024','3.76255e-07','2.20234e-07','0','0','0','0','0','-6.22701e-08','3.76255e-07','6.3818e-09','1.63157e-08','0','0','0','0','0','-5.12323e-07','2.20234e-07','1.63157e-08','4.60519e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050112, ("CSC", 2, 1, 4, 24), "MEm14_24"))
reports[-1].posNum = 2972
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0035056, 0.0029178, 0), \
                           ValErr(-0.00743084, 0.107926, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000129615, 7.59002e-05, 0), \
                           1335.49, 2972, 2972, -nan)
reports[-1].sigmaresid = ValErr(0.154386, 0.00200544, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00663255, None, -0.000452017, None, 0.00264505, None, -0.000234371, None, 0.00264505, None, -0.000234371, None, 0.00162514, None, -0.000405323, None, 0.00162514, None, -0.000405323, None, 0.154463, None, 0.00632151, None, 0.154463, None, 0.00632151, None)
reports[-1].CovMatrix = ['8.51357e-06','3.50111e-05','-4.13959e-08','9.75241e-09','0','0','0','0','0','3.50111e-05','0.011648','-5.01407e-07','3.45575e-07','0','0','0','0','0','-4.13959e-08','-5.01407e-07','5.76084e-09','-4.71669e-11','0','0','0','0','0','9.75241e-09','3.45575e-07','-4.71669e-11','4.0218e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050128, ("CSC", 2, 1, 4, 26), "MEm14_26"))
reports[-1].posNum = 2927
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000194312, 0.00297499, 0), \
                           ValErr(0.033648, 0.0748281, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.46961e-05, 7.89226e-05, 0), \
                           1251.03, 2927, 2927, -nan)
reports[-1].sigmaresid = ValErr(0.15781, 0.00206252, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00147578, None, -0.000969337, None, -0.000291833, None, -0.000911635, None, -0.000291833, None, -0.000911635, None, -0.00382269, None, -0.00104251, None, -0.00382269, None, -0.00104251, None, 0.157836, None, 0.00657959, None, 0.157836, None, 0.00657959, None)
reports[-1].CovMatrix = ['8.85058e-06','1.84968e-06','-4.61545e-08','1.62673e-09','0','0','0','0','0','1.84968e-06','0.00559924','-9.79807e-08','5.20154e-08','0','0','0','0','0','-4.61545e-08','-9.79807e-08','6.22878e-09','4.24854e-11','0','0','0','0','0','1.62673e-09','5.20154e-08','4.24854e-11','4.25399e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050144, ("CSC", 2, 1, 4, 28), "MEm14_28"))
reports[-1].posNum = 2847
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00172316, 0.00309892, 0), \
                           ValErr(-0.0384003, 0.105442, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000101985, 7.97083e-05, 0), \
                           1291.23, 2847, 2847, -nan)
reports[-1].sigmaresid = ValErr(0.153742, 0.00204353, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00249138, None, 0.000967511, None, 0.000883073, None, 0.00105752, None, 0.000883073, None, 0.00105752, None, 0.00753204, None, 0.000897467, None, 0.00753204, None, 0.000897467, None, 0.153798, None, 0.00585212, None, 0.153798, None, 0.00585212, None)
reports[-1].CovMatrix = ['9.60332e-06','-6.49886e-05','-6.96248e-08','4.319e-08','0','0','0','0','0','-6.49886e-05','0.0111181','1.43898e-06','-2.70187e-06','0','0','0','0','0','-6.96248e-08','1.43898e-06','6.35341e-09','-6.08897e-10','0','0','0','0','0','4.319e-08','-2.70187e-06','-6.08897e-10','4.17603e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050160, ("CSC", 2, 1, 4, 30), "MEm14_30"))
reports[-1].posNum = 2550
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00274121, 0.00318612, 0), \
                           ValErr(0.0236485, 0.081934, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000185528, 8.27507e-05, 0), \
                           1126.11, 2550, 2550, -nan)
reports[-1].sigmaresid = ValErr(0.155586, 0.00217863, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000361562, None, 0.00155354, None, 0.00103628, None, 0.001697, None, 0.00103628, None, 0.001697, None, 0.0091127, None, 0.00150617, None, 0.0091127, None, 0.00150617, None, 0.155741, None, 0.00609525, None, 0.155741, None, 0.00609525, None)
reports[-1].CovMatrix = ['1.01513e-05','3.13461e-05','-6.10647e-08','2.06581e-09','0','0','0','0','0','3.13461e-05','0.00671317','-4.21676e-07','6.20174e-08','0','0','0','0','0','-6.10647e-08','-4.21676e-07','6.84767e-09','4.27462e-11','0','0','0','0','0','2.06581e-09','6.20174e-08','4.27462e-11','4.74644e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050176, ("CSC", 2, 1, 4, 32), "MEm14_32"))
reports[-1].posNum = 2697
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00343578, 0.00294622, 0), \
                           ValErr(0.00307138, 0.116636, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000224113, 7.66065e-05, 0), \
                           1300.26, 2697, 2697, -nan)
reports[-1].sigmaresid = ValErr(0.14941, 0.00204764, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00131427, None, 0.00103969, None, 0.00179987, None, 0.00120652, None, 0.00179987, None, 0.00120652, None, -0.00247969, None, 0.00129342, None, -0.00247969, None, 0.00129342, None, 0.149648, None, 0.00594135, None, 0.149648, None, 0.00594135, None)
reports[-1].CovMatrix = ['8.6802e-06','-2.55481e-05','-4.34181e-08','-3.02436e-09','0','0','0','0','0','-2.55481e-05','0.013604','1.02171e-07','-6.20682e-07','0','0','0','0','0','-4.34181e-08','1.02171e-07','5.86855e-09','-1.3519e-10','0','0','0','0','0','-3.02436e-09','-6.20682e-07','-1.3519e-10','4.19284e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050192, ("CSC", 2, 1, 4, 34), "MEm14_34"))
reports[-1].posNum = 2731
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00242631, 0.00295522, 0), \
                           ValErr(0.0110278, 0.112689, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000194875, 7.78645e-05, 0), \
                           1275.6, 2731, 2731, -nan)
reports[-1].sigmaresid = ValErr(0.151671, 0.00211404, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(6.56113e-05, None, 0.00156092, None, 0.00118852, None, 0.00166303, None, 0.00118852, None, 0.00166303, None, -0.00675242, None, 0.00164299, None, -0.00675242, None, 0.00164299, None, 0.151851, None, 0.00661125, None, 0.151851, None, 0.00661125, None)
reports[-1].CovMatrix = ['8.73333e-06','2.3837e-05','-3.65165e-08','-2.38129e-08','0','0','0','0','0','2.3837e-05','0.0126988','6.24722e-07','5.49841e-08','0','0','0','0','0','-3.65165e-08','6.24722e-07','6.06288e-09','2.09402e-09','0','0','0','0','0','-2.38129e-08','5.49841e-08','2.09402e-09','4.46918e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050208, ("CSC", 2, 1, 4, 36), "MEm14_36"))
reports[-1].posNum = 2702
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00420978, 0.0030376, 0), \
                           ValErr(0.0178599, 0.0761784, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.64271e-05, 8.04685e-05, 0), \
                           1199.93, 2702, 2702, -nan)
reports[-1].sigmaresid = ValErr(0.155206, 0.00211136, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000541783, None, 0.00139841, None, 0.00360876, None, 0.00145731, None, 0.00360876, None, 0.00145731, None, 0.00287437, None, 0.00154019, None, 0.00287437, None, 0.00154019, None, 0.155237, None, 0.0055345, None, 0.155237, None, 0.0055345, None)
reports[-1].CovMatrix = ['9.22702e-06','2.00499e-06','-4.49183e-08','1.63797e-09','0','0','0','0','0','2.00499e-06','0.00580315','-1.24165e-07','5.16933e-08','0','0','0','0','0','-4.49183e-08','-1.24165e-07','6.47518e-09','4.67931e-11','0','0','0','0','0','1.63797e-09','5.16933e-08','4.67931e-11','4.45786e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054024, ("CSC", 2, 2, 1, 1), "MEm21_01"))
reports[-1].posNum = 6037
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00325429, 0.0048853, 0), \
                           ValErr(0.015395, 0.056465, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000150199, 9.93664e-05, 0), \
                           -2658.23, 6037, 6037, -nan)
reports[-1].sigmaresid = ValErr(0.375833, 0.00342035, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00788328, None, -0.00146727, None, 0.00429072, None, -0.00128285, None, 0.00429072, None, -0.00128285, None, -0.00349902, None, -0.00159549, None, -0.00349902, None, -0.00159549, None, 0.375905, None, 0.0110274, None, 0.375905, None, 0.0110274, None)
reports[-1].CovMatrix = ['2.38662e-05','1.23832e-06','-6.80243e-08','4.37706e-09','0','0','0','0','0','1.23832e-06','0.0031883','-9.43002e-08','5.88395e-08','0','0','0','0','0','-6.80243e-08','-9.43002e-08','9.87368e-09','1.015e-10','0','0','0','0','0','4.37706e-09','5.88395e-08','1.015e-10','1.16988e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054040, ("CSC", 2, 2, 1, 3), "MEm21_03"))
reports[-1].posNum = 5938
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00131362, 0.00487183, 0), \
                           ValErr(0.0124567, 0.0564518, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.59579e-05, 9.86799e-05, 0), \
                           -2577.76, 5938, 5938, -nan)
reports[-1].sigmaresid = ValErr(0.373504, 0.00342736, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00360423, None, -0.000430701, None, -0.00119638, None, -0.000287826, None, -0.00119638, None, -0.000287826, None, -0.0035755, None, -0.000246479, None, -0.0035755, None, -0.000246479, None, 0.373508, None, 0.0108751, None, 0.373508, None, 0.0108751, None)
reports[-1].CovMatrix = ['2.37347e-05','2.9728e-06','-4.81251e-08','4.83154e-09','0','0','0','0','0','2.9728e-06','0.00318681','4.67221e-08','6.32391e-08','0','0','0','0','0','-4.81251e-08','4.67221e-08','9.73772e-09','9.8971e-11','0','0','0','0','0','4.83154e-09','6.32391e-08','9.8971e-11','1.17468e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054056, ("CSC", 2, 2, 1, 5), "MEm21_05"))
reports[-1].posNum = 5727
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00184678, 0.00492999, 0), \
                           ValErr(-0.0118787, 0.0571972, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.93653e-05, 0.00010063, 0), \
                           -2436.93, 5727, 5727, -nan)
reports[-1].sigmaresid = ValErr(0.370307, 0.00346006, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00322187, None, -0.00221858, None, -0.00160011, None, -0.00219699, None, -0.00160011, None, -0.00219699, None, -0.00243718, None, -0.00232594, None, -0.00243718, None, -0.00232594, None, 0.370313, None, 0.0108277, None, 0.370313, None, 0.0108277, None)
reports[-1].CovMatrix = ['2.43048e-05','3.58293e-06','-6.01257e-08','4.85049e-09','0','0','0','0','0','3.58293e-06','0.00327152','-7.20794e-09','6.30094e-08','0','0','0','0','0','-6.01257e-08','-7.20794e-09','1.01264e-08','1.01378e-10','0','0','0','0','0','4.85049e-09','6.30094e-08','1.01378e-10','1.1972e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054072, ("CSC", 2, 2, 1, 7), "MEm21_07"))
reports[-1].posNum = 5763
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00332071, 0.00500837, 0), \
                           ValErr(0.00841007, 0.0578613, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.63601e-05, 0.000100932, 0), \
                           -2536.46, 5763, 5763, -nan)
reports[-1].sigmaresid = ValErr(0.375758, 0.00350001, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00677325, None, -0.00251625, None, -0.00265876, None, -0.00256163, None, -0.00265876, None, -0.00256163, None, -0.000260701, None, -0.00251584, None, -0.000260701, None, -0.00251584, None, 0.375783, None, 0.0105268, None, 0.375783, None, 0.0105268, None)
reports[-1].CovMatrix = ['2.50838e-05','-8.80371e-06','-7.56709e-08','4.7111e-09','0','0','0','0','0','-8.80371e-06','0.00334793','4.11606e-08','6.39788e-08','0','0','0','0','0','-7.56709e-08','4.11606e-08','1.01873e-08','9.9209e-11','0','0','0','0','0','4.7111e-09','6.39788e-08','9.9209e-11','1.22501e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054088, ("CSC", 2, 2, 1, 9), "MEm21_09"))
reports[-1].posNum = 6017
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00132952, 0.00483395, 0), \
                           ValErr(0.0040867, 0.0555333, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00013031, 9.72144e-05, 0), \
                           -2586.08, 6017, 6017, -nan)
reports[-1].sigmaresid = ValErr(0.371895, 0.00339012, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00144908, None, 0.00119823, None, -0.000501234, None, 0.00121592, None, -0.000501234, None, 0.00121592, None, -0.00060849, None, 0.00122728, None, -0.00060849, None, 0.00122728, None, 0.371951, None, 0.0107011, None, 0.371951, None, 0.0107011, None)
reports[-1].CovMatrix = ['2.33671e-05','-2.12948e-06','-5.9954e-08','4.57017e-09','0','0','0','0','0','-2.12948e-06','0.00308395','7.85029e-08','6.06269e-08','0','0','0','0','0','-5.9954e-08','7.85029e-08','9.45063e-09','9.43031e-11','0','0','0','0','0','4.57017e-09','6.06269e-08','9.43031e-11','1.14929e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054104, ("CSC", 2, 2, 1, 11), "MEm21_11"))
reports[-1].posNum = 5891
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000192797, 0.00488159, 0), \
                           ValErr(0.0284324, 0.0567757, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000242704, 9.99482e-05, 0), \
                           -2535.84, 5891, 5891, -nan)
reports[-1].sigmaresid = ValErr(0.372142, 0.00342846, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00550649, None, -0.00161355, None, 0.00120991, None, -0.00180576, None, 0.00120991, None, -0.00180576, None, 0.000253361, None, -0.00161194, None, 0.000253361, None, -0.00161194, None, 0.372336, None, 0.00975584, None, 0.372336, None, 0.00975584, None)
reports[-1].CovMatrix = ['2.38299e-05','-5.02475e-06','-5.59735e-08','4.67648e-09','0','0','0','0','0','-5.02475e-06','0.00322348','1.83349e-08','6.15774e-08','0','0','0','0','0','-5.59735e-08','1.83349e-08','9.98963e-09','9.81097e-11','0','0','0','0','0','4.67648e-09','6.15774e-08','9.81097e-11','1.17544e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054120, ("CSC", 2, 2, 1, 13), "MEm21_13"))
reports[-1].posNum = 5925
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00211041, 0.00491698, 0), \
                           ValErr(0.0228065, 0.0572254, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.02184e-05, 9.9832e-05, 0), \
                           -2603.17, 5925, 5925, -nan)
reports[-1].sigmaresid = ValErr(0.375467, 0.00344915, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00715191, None, 0.00290447, None, -0.0015145, None, 0.00322406, None, -0.0015145, None, 0.00322406, None, 0.00240485, None, 0.00304766, None, 0.00240485, None, 0.00304766, None, 0.375497, None, 0.010867, None, 0.375497, None, 0.010867, None)
reports[-1].CovMatrix = ['2.41767e-05','-7.95823e-06','-6.05016e-08','4.69238e-09','0','0','0','0','0','-7.95823e-06','0.00327474','1.161e-07','6.36361e-08','0','0','0','0','0','-6.05016e-08','1.161e-07','9.96642e-09','1.00658e-10','0','0','0','0','0','4.69238e-09','6.36361e-08','1.00658e-10','1.18967e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054136, ("CSC", 2, 2, 1, 15), "MEm21_15"))
reports[-1].posNum = 4913
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00501322, 0.00573123, 0), \
                           ValErr(0.0141344, 0.0735616, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.94673e-05, 0.000110902, 0), \
                           -2253.3, 4913, 4913, -nan)
reports[-1].sigmaresid = ValErr(0.38278, 0.00386156, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00828331, None, 0.000784566, None, -0.00484642, None, 0.000992029, None, -0.00484642, None, 0.000992029, None, -0.000459928, None, 0.000987112, None, -0.000459928, None, 0.000987112, None, 0.382812, None, 0.012887, None, 0.382812, None, 0.012887, None)
reports[-1].CovMatrix = ['3.2847e-05','0.000121683','-6.53053e-08','9.11625e-09','0','0','0','0','0','0.000121683','0.00541132','-2.60199e-07','1.23174e-07','0','0','0','0','0','-6.53053e-08','-2.60199e-07','1.22993e-08','1.22655e-10','0','0','0','0','0','9.11625e-09','1.23174e-07','1.22655e-10','1.49117e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054152, ("CSC", 2, 2, 1, 17), "MEm21_17"))
reports[-1].posNum = 5715
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00495053, 0.00495822, 0), \
                           ValErr(0.0112288, 0.0569178, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000119623, 0.000100439, 0), \
                           -2438.76, 5715, 5715, -nan)
reports[-1].sigmaresid = ValErr(0.370757, 0.0034679, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00439789, None, -0.00217166, None, -0.00410822, None, -0.00218075, None, -0.00410822, None, -0.00218075, None, -0.00700807, None, -0.00220683, None, -0.00700807, None, -0.00220683, None, 0.370804, None, 0.0106567, None, 0.370804, None, 0.0106567, None)
reports[-1].CovMatrix = ['2.4584e-05','4.85861e-06','-7.24886e-08','4.82631e-09','0','0','0','0','0','4.85861e-06','0.00323964','1.34184e-07','6.59483e-08','0','0','0','0','0','-7.24886e-08','1.34184e-07','1.00879e-08','9.86668e-11','0','0','0','0','0','4.82631e-09','6.59483e-08','9.86668e-11','1.20263e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054032, ("CSC", 2, 2, 1, 2), "MEm21_02"))
reports[-1].posNum = 5631
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00620002, 0.00484156, 0), \
                           ValErr(0.0489999, 0.0560271, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000173534, 9.88476e-05, 0), \
                           -2217.94, 5631, 5631, -nan)
reports[-1].sigmaresid = ValErr(0.358775, 0.00338075, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00163029, None, 0.000255631, None, -0.00490468, None, 0.000486477, None, -0.00490468, None, 0.000486477, None, -0.00104413, None, 0.000454777, None, -0.00104413, None, 0.000454777, None, 0.358899, None, 0.0103919, None, 0.358899, None, 0.0103919, None)
reports[-1].CovMatrix = ['2.34407e-05','3.0473e-06','-7.52295e-08','4.16718e-09','0','0','0','0','0','3.0473e-06','0.00313904','-4.11036e-08','5.99292e-08','0','0','0','0','0','-7.52295e-08','-4.11036e-08','9.77085e-09','8.80396e-11','0','0','0','0','0','4.16718e-09','5.99292e-08','8.80396e-11','1.14295e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054048, ("CSC", 2, 2, 1, 4), "MEm21_04"))
reports[-1].posNum = 5579
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00684116, 0.00481015, 0), \
                           ValErr(0.0324205, 0.0562084, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.41076e-05, 9.76778e-05, 0), \
                           -2172.57, 5579, 5579, -nan)
reports[-1].sigmaresid = ValErr(0.357177, 0.00338133, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.016524, None, 0.00282195, None, 0.00651697, None, 0.00302118, None, 0.00651697, None, 0.00302118, None, 0.0155634, None, 0.00311527, None, 0.0155634, None, 0.00311527, None, 0.357208, None, 0.0109263, None, 0.357208, None, 0.0109263, None)
reports[-1].CovMatrix = ['2.31375e-05','-6.17674e-06','-4.97218e-08','4.3422e-09','0','0','0','0','0','-6.17674e-06','0.00315939','3.75425e-08','5.72194e-08','0','0','0','0','0','-4.97218e-08','3.75425e-08','9.54095e-09','9.02333e-11','0','0','0','0','0','4.3422e-09','5.72194e-08','9.02333e-11','1.14334e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054064, ("CSC", 2, 2, 1, 6), "MEm21_06"))
reports[-1].posNum = 5786
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0013418, 0.00462673, 0), \
                           ValErr(0.0271433, 0.0533327, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.73846e-05, 9.29345e-05, 0), \
                           -2104.69, 5786, 5786, -nan)
reports[-1].sigmaresid = ValErr(0.348126, 0.00323614, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00169032, None, -0.00228915, None, -0.00095677, None, -0.00217519, None, -0.00095677, None, -0.00217519, None, -0.0014596, None, -0.00227653, None, -0.0014596, None, -0.00227653, None, 0.348144, None, 0.0108951, None, 0.348144, None, 0.0108951, None)
reports[-1].CovMatrix = ['2.14066e-05','-4.97181e-06','-6.26275e-08','3.75628e-09','0','0','0','0','0','-4.97181e-06','0.00284437','7.65176e-08','5.31597e-08','0','0','0','0','0','-6.26275e-08','7.65176e-08','8.63682e-09','7.27227e-11','0','0','0','0','0','3.75628e-09','5.31597e-08','7.27227e-11','1.04726e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054080, ("CSC", 2, 2, 1, 8), "MEm21_08"))
reports[-1].posNum = 3305
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00119551, 0.00620432, 0), \
                           ValErr(0.0583943, 0.0712242, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.80889e-05, 0.000124926, 0), \
                           -1248.53, 3305, 3305, -nan)
reports[-1].sigmaresid = ValErr(0.353038, 0.00434226, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00070497, None, -0.000552465, None, -0.000904359, None, -0.000693623, None, -0.000904359, None, -0.000693623, None, -0.00347508, None, -0.000459607, None, -0.00347508, None, -0.000459607, None, 0.35308, None, 0.0118604, None, 0.35308, None, 0.0118604, None)
reports[-1].CovMatrix = ['3.84936e-05','-8.1699e-06','-1.09593e-07','6.69134e-09','0','0','0','0','0','-8.1699e-06','0.00507288','2.34261e-08','9.25302e-08','0','0','0','0','0','-1.09593e-07','2.34261e-08','1.56066e-08','1.38211e-10','0','0','0','0','0','6.69134e-09','9.25302e-08','1.38211e-10','1.88553e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054096, ("CSC", 2, 2, 1, 10), "MEm21_10"))
reports[-1].posNum = 5953
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0053735, 0.0046256, 0), \
                           ValErr(0.0149637, 0.053702, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000173917, 9.37017e-05, 0), \
                           -2243.19, 5953, 5953, -nan)
reports[-1].sigmaresid = ValErr(0.352702, 0.00323236, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00525826, None, 0.00328763, None, -0.00406206, None, 0.00348444, None, -0.00406206, None, 0.00348444, None, -0.00497253, None, 0.00326093, None, -0.00497253, None, 0.00326093, None, 0.35281, None, 0.0117517, None, 0.35281, None, 0.0117517, None)
reports[-1].CovMatrix = ['2.13962e-05','6.59387e-08','-6.62193e-08','3.83063e-09','0','0','0','0','0','6.59387e-08','0.0028839','5.35195e-09','5.29916e-08','0','0','0','0','0','-6.62193e-08','5.35195e-09','8.78001e-09','7.71751e-11','0','0','0','0','0','3.83063e-09','5.29916e-08','7.71751e-11','1.04481e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054112, ("CSC", 2, 2, 1, 12), "MEm21_12"))
reports[-1].posNum = 5985
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00197278, 0.00467129, 0), \
                           ValErr(0.0183289, 0.0540416, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.92782e-07, 9.43598e-05, 0), \
                           -2359.49, 5985, 5985, -nan)
reports[-1].sigmaresid = ValErr(0.3589, 0.00328036, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00268111, None, 0.0014932, None, -0.00198859, None, 0.0015802, None, -0.00198859, None, 0.0015802, None, -0.00409229, None, 0.00142402, None, -0.00409229, None, 0.00142402, None, 0.358906, None, 0.0105992, None, 0.358906, None, 0.0105992, None)
reports[-1].CovMatrix = ['2.1821e-05','2.03652e-06','-5.14257e-08','4.08407e-09','0','0','0','0','0','2.03652e-06','0.00292049','6.45892e-08','5.23081e-08','0','0','0','0','0','-5.14257e-08','6.45892e-08','8.90377e-09','8.55183e-11','0','0','0','0','0','4.08407e-09','5.23081e-08','8.55183e-11','1.07608e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054128, ("CSC", 2, 2, 1, 14), "MEm21_14"))
reports[-1].posNum = 5650
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0011313, 0.00479367, 0), \
                           ValErr(0.0216095, 0.0551922, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0001286, 9.62667e-05, 0), \
                           -2198.18, 5650, 5650, -nan)
reports[-1].sigmaresid = ValErr(0.357048, 0.00335881, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00930361, None, -0.00153635, None, -0.000240341, None, -0.00131123, None, -0.000240341, None, -0.00131123, None, 0.00564446, None, -0.00159528, None, 0.00564446, None, -0.00159528, None, 0.357111, None, 0.0114659, None, 0.357111, None, 0.0114659, None)
reports[-1].CovMatrix = ['2.29792e-05','-5.38156e-06','-6.13189e-08','4.17687e-09','0','0','0','0','0','-5.38156e-06','0.00304618','-2.22735e-08','5.55195e-08','0','0','0','0','0','-6.13189e-08','-2.22735e-08','9.26727e-09','8.50806e-11','0','0','0','0','0','4.17687e-09','5.55195e-08','8.50806e-11','1.12816e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054144, ("CSC", 2, 2, 1, 16), "MEm21_16"))
reports[-1].posNum = 5757
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000966296, 0.00470149, 0), \
                           ValErr(0.0695892, 0.0538454, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.87025e-05, 9.52318e-05, 0), \
                           -2164.35, 5757, 5757, -nan)
reports[-1].sigmaresid = ValErr(0.352396, 0.00328406, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00443537, None, -0.00146459, None, 0.000471792, None, -0.0010738, None, 0.000471792, None, -0.0010738, None, -0.00418052, None, -0.00134612, None, -0.00418052, None, -0.00134612, None, 0.352468, None, 0.0115883, None, 0.352468, None, 0.0115883, None)
reports[-1].CovMatrix = ['2.2104e-05','-2.16934e-06','-6.94977e-08','4.01913e-09','0','0','0','0','0','-2.16934e-06','0.00289933','1.0182e-07','5.4376e-08','0','0','0','0','0','-6.94977e-08','1.0182e-07','9.0691e-09','8.19042e-11','0','0','0','0','0','4.01913e-09','5.4376e-08','8.19042e-11','1.07851e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054160, ("CSC", 2, 2, 1, 18), "MEm21_18"))
reports[-1].posNum = 5733
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00283341, 0.00473009, 0), \
                           ValErr(-0.0187664, 0.0550182, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.62305e-05, 9.65483e-05, 0), \
                           -2202.9, 5733, 5733, -nan)
reports[-1].sigmaresid = ValErr(0.355332, 0.00331833, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-1.16204e-05, None, -0.00228395, None, 0.00257396, None, -0.00224408, None, 0.00257396, None, -0.00224408, None, -0.0012079, None, -0.00228576, None, -0.0012079, None, -0.00228576, None, 0.355345, None, 0.0105199, None, 0.355345, None, 0.0105199, None)
reports[-1].CovMatrix = ['2.23737e-05','-5.67503e-06','-5.62382e-08','4.40585e-09','0','0','0','0','0','-5.67503e-06','0.00302701','-1.47725e-08','5.58463e-08','0','0','0','0','0','-5.62382e-08','-1.47725e-08','9.32157e-09','8.45409e-11','0','0','0','0','0','4.40585e-09','5.58463e-08','8.45409e-11','1.10113e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054536, ("CSC", 2, 2, 2, 1), "MEm22_01"))
reports[-1].posNum = 2126
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0269978, 0.021436, 0), \
                           ValErr(-0.0498038, 0.534916, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000284777, 0.000233812, 0), \
                           -2865.14, 2126, 2126, -nan)
reports[-1].sigmaresid = ValErr(0.931208, 0.0142806, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0303193, None, 0.00026988, None, 0.0182383, None, 0.000714544, None, 0.0182383, None, 0.000714544, None, 0.0026166, None, 0.000482997, None, 0.0026166, None, 0.000482997, None, 0.931536, None, 0.0111667, None, 0.931536, None, 0.0111667, None)
reports[-1].CovMatrix = ['0.000459501','-3.343e-06','-1.6797e-06','1.21011e-07','0','0','0','0','0','-3.343e-06','0.286135','-1.9385e-06','4.39127e-06','0','0','0','0','0','-1.6797e-06','-1.9385e-06','5.46682e-08','1.29764e-09','0','0','0','0','0','1.21011e-07','4.39127e-06','1.29764e-09','0.000203939','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054552, ("CSC", 2, 2, 2, 3), "MEm22_03"))
reports[-1].posNum = 1436
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0028673, 0.0267246, 0), \
                           ValErr(0.199391, 0.620083, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.5048e-05, 0.000268443, 0), \
                           -1796.16, 1436, 1436, -nan)
reports[-1].sigmaresid = ValErr(0.84524, 0.0157719, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0098209, None, 0.00202803, None, -0.000857469, None, 0.00235556, None, -0.000857469, None, 0.00235556, None, -0.018734, None, 0.00261791, None, -0.018734, None, 0.00261791, None, 0.845272, None, 0.0098998, None, 0.845272, None, 0.0098998, None)
reports[-1].CovMatrix = ['0.000714203','0.00582959','-3.27819e-06','2.49433e-07','0','0','0','0','0','0.00582959','0.384503','-1.66741e-05','7.41891e-06','0','0','0','0','0','-3.27819e-06','-1.66741e-05','7.20614e-08','1.06193e-09','0','0','0','0','0','2.49433e-07','7.41891e-06','1.06193e-09','0.000248756','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054568, ("CSC", 2, 2, 2, 5), "MEm22_05"))
reports[-1].posNum = 1516
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.017878, 0.0263515, 0), \
                           ValErr(0.443013, 0.577318, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000159336, 0.000266709, 0), \
                           -1823.15, 1516, 1516, -nan)
reports[-1].sigmaresid = ValErr(0.805465, 0.0146278, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0101963, None, -0.00080153, None, 0.00742758, None, -0.000664774, None, 0.00742758, None, -0.000664774, None, 0.0105713, None, -0.00091704, None, 0.0105713, None, -0.00091704, None, 0.805701, None, 0.010029, None, 0.805701, None, 0.010029, None)
reports[-1].CovMatrix = ['0.0006944','0.00121863','-4.34575e-06','1.20347e-07','0','0','0','0','0','0.00121863','0.333296','-1.07304e-05','4.57019e-06','0','0','0','0','0','-4.34575e-06','-1.07304e-05','7.11338e-08','8.53921e-10','0','0','0','0','0','1.20347e-07','4.57019e-06','8.53921e-10','0.000213975','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054584, ("CSC", 2, 2, 2, 7), "MEm22_07"))
reports[-1].posNum = 1866
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00564515, 0.0240822, 0), \
                           ValErr(-0.227045, 0.560354, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000117573, 0.000256421, 0), \
                           -2362.96, 1866, 1866, -nan)
reports[-1].sigmaresid = ValErr(0.858452, 0.014052, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0133258, None, -0.00044155, None, 0.00110887, None, -0.000329578, None, 0.00110887, None, -0.000329578, None, -0.0261096, None, -0.000381617, None, -0.0261096, None, -0.000381617, None, 0.858542, None, 0.00827278, None, 0.858542, None, 0.00827278, None)
reports[-1].CovMatrix = ['0.000579954','0.00103489','-3.46792e-06','1.35356e-07','0','0','0','0','0','0.00103489','0.313997','-4.1721e-06','4.84488e-06','0','0','0','0','0','-3.46792e-06','-4.1721e-06','6.57515e-08','7.34186e-10','0','0','0','0','0','1.35356e-07','4.84488e-06','7.34186e-10','0.000197462','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054600, ("CSC", 2, 2, 2, 9), "MEm22_09"))
reports[-1].posNum = 1686
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00257014, 0.0263972, 0), \
                           ValErr(0.065915, 0.555785, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.28144e-05, 0.000275068, 0), \
                           -2057.5, 1686, 1686, -nan)
reports[-1].sigmaresid = ValErr(0.819879, 0.014119, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00796643, None, 0.000721219, None, -0.000319094, None, 0.000721623, None, -0.000319094, None, 0.000721623, None, -0.00491116, None, 0.000838035, None, -0.00491116, None, 0.000838035, None, 0.819887, None, 0.00846686, None, 0.819887, None, 0.00846686, None)
reports[-1].CovMatrix = ['0.000696812','-0.00227995','-4.71935e-06','6.50693e-08','0','0','0','0','0','-0.00227995','0.308897','1.94328e-05','3.575e-06','0','0','0','0','0','-4.71935e-06','1.94328e-05','7.56624e-08','1.19134e-09','0','0','0','0','0','6.50693e-08','3.575e-06','1.19134e-09','0.000199347','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054616, ("CSC", 2, 2, 2, 11), "MEm22_11"))
reports[-1].posNum = 2149
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0218012, 0.0210088, 0), \
                           ValErr(-0.151112, 0.510608, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000200636, 0.000224486, 0), \
                           -2776.32, 2149, 2149, -nan)
reports[-1].sigmaresid = ValErr(0.880704, 0.0134336, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00104362, None, 0.000321898, None, -0.013687, None, 0.000555448, None, -0.013687, None, 0.000555448, None, -0.0225413, None, 0.000622988, None, -0.0225413, None, 0.000622988, None, 0.880885, None, 0.00890734, None, 0.880885, None, 0.00890734, None)
reports[-1].CovMatrix = ['0.000441369','0.000589308','-2.01039e-06','1.05807e-07','0','0','0','0','0','0.000589308','0.26072','-8.5574e-06','3.87176e-06','0','0','0','0','0','-2.01039e-06','-8.5574e-06','5.03941e-08','1.01045e-09','0','0','0','0','0','1.05807e-07','3.87176e-06','1.01045e-09','0.000180462','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054632, ("CSC", 2, 2, 2, 13), "MEm22_13"))
reports[-1].posNum = 1940
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0335931, 0.0217795, 0), \
                           ValErr(-0.195897, 0.527122, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000181828, 0.000239881, 0), \
                           -2468.93, 1940, 1940, -nan)
reports[-1].sigmaresid = ValErr(0.863871, 0.0138679, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.011238, None, -0.000238134, None, -0.0268182, None, 0.000252735, None, -0.0268182, None, 0.000252735, None, -0.0171095, None, -0.000329379, None, -0.0171095, None, -0.000329379, None, 0.864059, None, 0.0101731, None, 0.864059, None, 0.0101731, None)
reports[-1].CovMatrix = ['0.000474348','-0.000428509','-2.25775e-06','9.12065e-08','0','0','0','0','0','-0.000428509','0.277858','-3.07542e-06','4.55667e-06','0','0','0','0','0','-2.25775e-06','-3.07542e-06','5.75428e-08','1.15934e-09','0','0','0','0','0','9.12065e-08','4.55667e-06','1.15934e-09','0.00019232','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054648, ("CSC", 2, 2, 2, 15), "MEm22_15"))
reports[-1].posNum = 2174
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0043389, 0.0212872, 0), \
                           ValErr(0.00224844, 0.501116, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00011691, 0.0002363, 0), \
                           -2844.45, 2174, 2174, -nan)
reports[-1].sigmaresid = ValErr(0.895336, 0.0135779, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0047055, None, 0.000240568, None, 0.000227308, None, 0.000449031, None, 0.000227308, None, 0.000449031, None, -0.00146544, None, 0.000772079, None, -0.00146544, None, 0.000772079, None, 0.895397, None, 0.0092805, None, 0.895397, None, 0.0092805, None)
reports[-1].CovMatrix = ['0.000453145','-0.000218457','-2.16989e-06','8.43267e-08','0','0','0','0','0','-0.000218457','0.251117','1.81321e-06','3.82893e-06','0','0','0','0','0','-2.16989e-06','1.81321e-06','5.58377e-08','1.2643e-09','0','0','0','0','0','8.43267e-08','3.82893e-06','1.2643e-09','0.000184361','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054664, ("CSC", 2, 2, 2, 17), "MEm22_17"))
reports[-1].posNum = 1897
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000385132, 0.0220339, 0), \
                           ValErr(0.590977, 0.545638, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.42072e-05, 0.00022985, 0), \
                           -2475.36, 1897, 1897, -nan)
reports[-1].sigmaresid = ValErr(0.892191, 0.0144843, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00753337, None, 0.00137767, None, 0.00147373, None, 0.00139559, None, 0.00147373, None, 0.00139559, None, 0.0121106, None, 0.00145033, None, 0.0121106, None, 0.00145033, None, 0.89249, None, 0.00918139, None, 0.89249, None, 0.00918139, None)
reports[-1].CovMatrix = ['0.000485493','0.000138673','-1.86235e-06','9.58115e-08','0','0','0','0','0','0.000138673','0.29772','3.49296e-06','4.49965e-06','0','0','0','0','0','-1.86235e-06','3.49296e-06','5.28309e-08','1.4472e-09','0','0','0','0','0','9.58115e-08','4.49965e-06','1.4472e-09','0.000209796','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054680, ("CSC", 2, 2, 2, 19), "MEm22_19"))
reports[-1].posNum = 1968
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0092913, 0.0210016, 0), \
                           ValErr(-0.138456, 0.519368, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.03594e-05, 0.000228787, 0), \
                           -2531.56, 1968, 1968, -nan)
reports[-1].sigmaresid = ValErr(0.875826, 0.0139599, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0109184, None, 0.000404021, None, -0.00619191, None, 0.000357043, None, -0.00619191, None, 0.000357043, None, 0.00453209, None, 0.000422399, None, 0.00453209, None, 0.000422399, None, 0.875888, None, 0.00840852, None, 0.875888, None, 0.00840852, None)
reports[-1].CovMatrix = ['0.000441069','0.000291527','-1.62354e-06','1.11662e-07','0','0','0','0','0','0.000291527','0.269743','6.80798e-06','4.79952e-06','0','0','0','0','0','-1.62354e-06','6.80798e-06','5.23435e-08','1.36894e-09','0','0','0','0','0','1.11662e-07','4.79952e-06','1.36894e-09','0.000194881','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054696, ("CSC", 2, 2, 2, 21), "MEm22_21"))
reports[-1].posNum = 1983
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000223431, 0.0218581, 0), \
                           ValErr(0.239654, 0.518455, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.64306e-05, 0.000231663, 0), \
                           -2502.92, 1983, 1983, -nan)
reports[-1].sigmaresid = ValErr(0.854913, 0.013575, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0145023, None, 0.000890024, None, 0.00238952, None, 0.000901584, None, 0.00238952, None, 0.000901584, None, -0.0175128, None, 0.000838971, None, -0.0175128, None, 0.000838971, None, 0.854979, None, 0.00938523, None, 0.854979, None, 0.00938523, None)
reports[-1].CovMatrix = ['0.000477776','0.000674545','-2.4133e-06','9.16038e-08','0','0','0','0','0','0.000674545','0.268796','-5.46562e-06','3.76408e-06','0','0','0','0','0','-2.4133e-06','-5.46562e-06','5.36676e-08','1.07883e-09','0','0','0','0','0','9.16038e-08','3.76408e-06','1.07883e-09','0.000184283','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054712, ("CSC", 2, 2, 2, 23), "MEm22_23"))
reports[-1].posNum = 2101
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0146944, 0.0201971, 0), \
                           ValErr(-0.0166435, 0.488481, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.48897e-07, 0.000219848, 0), \
                           -2592.17, 2101, 2101, -nan)
reports[-1].sigmaresid = ValErr(0.830967, 0.0128189, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00334186, None, 0.000822126, None, -0.0146891, None, 0.000996273, None, -0.0146891, None, 0.000996273, None, -0.0330682, None, 0.00112271, None, -0.0330682, None, 0.00112271, None, 0.830973, None, 0.00953608, None, 0.830973, None, 0.00953608, None)
reports[-1].CovMatrix = ['0.000407924','5.98457e-05','-1.95614e-06','8.86403e-08','0','0','0','0','0','5.98457e-05','0.238614','-5.2617e-06','3.11225e-06','0','0','0','0','0','-1.95614e-06','-5.2617e-06','4.83331e-08','8.93063e-10','0','0','0','0','0','8.86403e-08','3.11225e-06','8.93063e-10','0.000164326','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054728, ("CSC", 2, 2, 2, 25), "MEm22_25"))
reports[-1].posNum = 1701
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00657135, 0.0234804, 0), \
                           ValErr(-0.0312798, 0.545453, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.79066e-05, 0.000244312, 0), \
                           -2152.23, 1701, 1701, -nan)
reports[-1].sigmaresid = ValErr(0.857556, 0.0147025, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.018038, None, -0.00346113, None, 0.00493351, None, -0.00322506, None, 0.00493351, None, -0.00322506, None, -0.0133011, None, -0.00320993, None, -0.0133011, None, -0.00320993, None, 0.857565, None, 0.00855896, None, 0.857565, None, 0.00855896, None)
reports[-1].CovMatrix = ['0.000551331','0.000461864','-2.65615e-06','1.25238e-07','0','0','0','0','0','0.000461864','0.297519','5.59562e-07','4.79859e-06','0','0','0','0','0','-2.65615e-06','5.59562e-07','5.96885e-08','1.15052e-09','0','0','0','0','0','1.25238e-07','4.79859e-06','1.15052e-09','0.000216166','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054744, ("CSC", 2, 2, 2, 27), "MEm22_27"))
reports[-1].posNum = 1579
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00205048, 0.0237877, 0), \
                           ValErr(-0.0421296, 0.558176, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.51501e-05, 0.000248337, 0), \
                           -1937.55, 1579, 1579, -nan)
reports[-1].sigmaresid = ValErr(0.825418, 0.0146881, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0167891, None, -0.00173826, None, -0.0007664, None, -0.00135772, None, -0.0007664, None, -0.00135772, None, 0.00763523, None, -0.00144927, None, 0.00763523, None, -0.00144927, None, 0.825423, None, 0.00879979, None, 0.825423, None, 0.00879979, None)
reports[-1].CovMatrix = ['0.000565853','0.000708363','-2.86016e-06','9.78412e-08','0','0','0','0','0','0.000708363','0.311561','5.11449e-07','4.42694e-06','0','0','0','0','0','-2.86016e-06','5.11449e-07','6.16714e-08','1.46574e-09','0','0','0','0','0','9.78412e-08','4.42694e-06','1.46574e-09','0.000215743','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054760, ("CSC", 2, 2, 2, 29), "MEm22_29"))
reports[-1].posNum = 1815
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00120907, 0.0235702, 0), \
                           ValErr(-0.0550744, 0.574682, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.4814e-05, 0.000248223, 0), \
                           -2374.71, 1815, 1815, -nan)
reports[-1].sigmaresid = ValErr(0.895336, 0.0148605, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00121679, None, -0.000636918, None, 0.000672186, None, -0.000421698, None, 0.000672186, None, -0.000421698, None, 0.0204143, None, -0.00105393, None, 0.0204143, None, -0.00105393, None, 0.895337, None, 0.0091626, None, 0.895337, None, 0.0091626, None)
reports[-1].CovMatrix = ['0.000555555','0.00104401','-2.6211e-06','1.71518e-07','0','0','0','0','0','0.00104401','0.330259','-3.68287e-06','5.1982e-06','0','0','0','0','0','-2.6211e-06','-3.68287e-06','6.16149e-08','1.06079e-09','0','0','0','0','0','1.71518e-07','5.1982e-06','1.06079e-09','0.000220835','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054776, ("CSC", 2, 2, 2, 31), "MEm22_31"))
reports[-1].posNum = 905
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0036394, 0.0383368, 0), \
                           ValErr(-0.390151, 0.717336, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.30681e-05, 0.000343588, 0), \
                           -1008.72, 905, 905, -nan)
reports[-1].sigmaresid = ValErr(0.737634, 0.0173384, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0138328, None, -0.00192419, None, -0.0103389, None, -0.00143345, None, -0.0103389, None, -0.00143345, None, -0.0234556, None, -0.00125372, None, -0.0234556, None, -0.00125372, None, 0.737742, None, 0.00826831, None, 0.737742, None, 0.00826831, None)
reports[-1].CovMatrix = ['0.00146971','-0.00674154','-1.00227e-05','4.35895e-08','0','0','0','0','0','-0.00674154','0.514571','4.45852e-05','6.22084e-06','0','0','0','0','0','-1.00227e-05','4.45852e-05','1.18053e-07','1.63387e-09','0','0','0','0','0','4.35895e-08','6.22084e-06','1.63387e-09','0.000300624','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054792, ("CSC", 2, 2, 2, 33), "MEm22_33"))
reports[-1].posNum = 1691
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00510561, 0.0234407, 0), \
                           ValErr(-0.191402, 0.556766, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000198666, 0.000243411, 0), \
                           -2106.64, 1691, 1691, -nan)
reports[-1].sigmaresid = ValErr(0.840991, 0.0144606, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0110044, None, 0.0013937, None, 0.00428107, None, 0.00195208, None, 0.00428107, None, 0.00195208, None, 0.00513513, None, 0.00175722, None, 0.00513513, None, 0.00175722, None, 0.841216, None, 0.00941807, None, 0.841216, None, 0.00941807, None)
reports[-1].CovMatrix = ['0.000549465','-0.000193971','-2.7882e-06','8.51193e-08','0','0','0','0','0','-0.000193971','0.309989','4.61306e-06','5.39504e-06','0','0','0','0','0','-2.7882e-06','4.61306e-06','5.92488e-08','1.38856e-09','0','0','0','0','0','8.51193e-08','5.39504e-06','1.38856e-09','0.000209111','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054808, ("CSC", 2, 2, 2, 35), "MEm22_35"))
reports[-1].posNum = 2037
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0224837, 0.0213574, 0), \
                           ValErr(-0.085552, 0.5286, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000201597, 0.000222498, 0), \
                           -2642.53, 2037, 2037, -nan)
reports[-1].sigmaresid = ValErr(0.885427, 0.0138719, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0234291, None, -0.000271872, None, -0.0148532, None, -0.000375392, None, -0.0148532, None, -0.000375392, None, -0.0510455, None, -0.00023736, None, -0.0510455, None, -0.00023736, None, 0.885619, None, 0.00922873, None, 0.885619, None, 0.00922873, None)
reports[-1].CovMatrix = ['0.00045614','-3.91709e-05','-1.8782e-06','1.04309e-07','0','0','0','0','0','-3.91709e-05','0.279418','-4.90387e-07','4.32858e-06','0','0','0','0','0','-1.8782e-06','-4.90387e-07','4.95053e-08','1.22101e-09','0','0','0','0','0','1.04309e-07','4.32858e-06','1.22101e-09','0.000192431','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054544, ("CSC", 2, 2, 2, 2), "MEm22_02"))
reports[-1].posNum = 2166
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00462034, 0.0211977, 0), \
                           ValErr(-0.0504168, 0.510074, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.65809e-05, 0.000228767, 0), \
                           -2857.08, 2166, 2166, -nan)
reports[-1].sigmaresid = ValErr(0.904927, 0.0137485, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0165794, None, -0.00133558, None, -0.00745919, None, -0.000822903, None, -0.00745919, None, -0.000822903, None, -0.00105509, None, -0.00104532, None, -0.00105509, None, -0.00104532, None, 0.904972, None, 0.0108618, None, 0.904972, None, 0.0108618, None)
reports[-1].CovMatrix = ['0.000449344','-7.66596e-05','-1.9312e-06','1.17542e-07','0','0','0','0','0','-7.66596e-05','0.260176','3.72979e-06','4.1476e-06','0','0','0','0','0','-1.9312e-06','3.72979e-06','5.23343e-08','1.16607e-09','0','0','0','0','0','1.17542e-07','4.1476e-06','1.16607e-09','0.000189022','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054560, ("CSC", 2, 2, 2, 4), "MEm22_04"))
reports[-1].posNum = 1455
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0313951, 0.0271127, 0), \
                           ValErr(0.179639, 0.614402, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000161975, 0.000275303, 0), \
                           -1841.03, 1455, 1455, -nan)
reports[-1].sigmaresid = ValErr(0.857577, 0.0158969, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0389953, None, -0.0018292, None, 0.0220137, None, -0.00173322, None, 0.0220137, None, -0.00173322, None, 0.0326572, None, -0.00198146, None, 0.0326572, None, -0.00198146, None, 0.857716, None, 0.00929849, None, 0.857716, None, 0.00929849, None)
reports[-1].CovMatrix = ['0.000735099','0.00223541','-4.1171e-06','1.38805e-07','0','0','0','0','0','0.00223541','0.37749','-1.35419e-05','4.98671e-06','0','0','0','0','0','-4.1171e-06','-1.35419e-05','7.57919e-08','1.22444e-09','0','0','0','0','0','1.38805e-07','4.98671e-06','1.22444e-09','0.000252714','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054576, ("CSC", 2, 2, 2, 6), "MEm22_06"))
reports[-1].posNum = 1554
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0309005, 0.0283718, 0), \
                           ValErr(0.106247, 0.572339, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000215399, 0.00029531, 0), \
                           -1867.63, 1554, 1554, -nan)
reports[-1].sigmaresid = ValErr(0.804826, 0.0144363, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00776444, None, -0.000475619, None, -0.0164721, None, 0.000229047, None, -0.0164721, None, 0.000229047, None, -0.0125244, None, -0.000144071, None, -0.0125244, None, -0.000144071, None, 0.804972, None, 0.0110663, None, 0.804972, None, 0.0110663, None)
reports[-1].CovMatrix = ['0.000804958','-0.00325734','-5.7614e-06','5.79288e-08','0','0','0','0','0','-0.00325734','0.327572','2.58509e-05','4.64697e-06','0','0','0','0','0','-5.7614e-06','2.58509e-05','8.72079e-08','1.25429e-09','0','0','0','0','0','5.79288e-08','4.64697e-06','1.25429e-09','0.000208408','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054592, ("CSC", 2, 2, 2, 8), "MEm22_08"))
reports[-1].posNum = 1736
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00313218, 0.0222999, 0), \
                           ValErr(-0.0523294, 0.521967, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.41708e-05, 0.000231094, 0), \
                           -2070.05, 1736, 1736, -nan)
reports[-1].sigmaresid = ValErr(0.797309, 0.0135312, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0291111, None, -0.00243535, None, 0.00195529, None, -0.00254367, None, 0.00195529, None, -0.00254367, None, -0.0021267, None, -0.00273789, None, -0.0021267, None, -0.00273789, None, 0.797314, None, 0.0101538, None, 0.797314, None, 0.0101538, None)
reports[-1].CovMatrix = ['0.000497283','0.000439598','-2.64559e-06','9.26874e-08','0','0','0','0','0','0.000439598','0.27245','-6.85841e-06','3.39931e-06','0','0','0','0','0','-2.64559e-06','-6.85841e-06','5.34044e-08','9.39711e-10','0','0','0','0','0','9.26874e-08','3.39931e-06','9.39711e-10','0.000183094','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054608, ("CSC", 2, 2, 2, 10), "MEm22_10"))
reports[-1].posNum = 2313
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000413599, 0.0202083, 0), \
                           ValErr(-0.000315115, 0.490309, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.91167e-05, 0.000220685, 0), \
                           -3032.47, 2313, 2313, -nan)
reports[-1].sigmaresid = ValErr(0.897736, 0.0131991, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00479132, None, -0.00103786, None, 0.00111134, None, -0.000383925, None, 0.00111134, None, -0.000383925, None, -0.0189558, None, -0.00046058, None, -0.0189558, None, -0.00046058, None, 0.897735, None, 0.0119589, None, 0.897735, None, 0.0119589, None)
reports[-1].CovMatrix = ['0.000408377','0.00012418','-1.70824e-06','8.29151e-08','0','0','0','0','0','0.00012418','0.240403','-1.31846e-06','3.59827e-06','0','0','0','0','0','-1.70824e-06','-1.31846e-06','4.87019e-08','1.29326e-09','0','0','0','0','0','8.29151e-08','3.59827e-06','1.29326e-09','0.000174218','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054624, ("CSC", 2, 2, 2, 12), "MEm22_12"))
reports[-1].posNum = 1647
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00384768, 0.0245102, 0), \
                           ValErr(0.133555, 0.541672, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000168696, 0.000252819, 0), \
                           -1978.89, 1647, 1647, -nan)
reports[-1].sigmaresid = ValErr(0.804572, 0.0140182, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0120651, None, -0.000613707, None, 0.00594987, None, -0.00041711, None, 0.00594987, None, -0.00041711, None, 0.0216708, None, -0.0001925, None, 0.0216708, None, -0.0001925, None, 0.804709, None, 0.0106202, None, 0.804709, None, 0.0106202, None)
reports[-1].CovMatrix = ['0.000600751','-0.000652105','-3.63687e-06','9.33356e-08','0','0','0','0','0','-0.000652105','0.293408','3.07309e-06','3.02687e-06','0','0','0','0','0','-3.63687e-06','3.07309e-06','6.39176e-08','9.32567e-10','0','0','0','0','0','9.33356e-08','3.02687e-06','9.32567e-10','0.00019651','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054640, ("CSC", 2, 2, 2, 14), "MEm22_14"))
reports[-1].posNum = 2162
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00878499, 0.0208283, 0), \
                           ValErr(-0.0385528, 0.507502, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000112277, 0.000226266, 0), \
                           -2784.78, 2162, 2162, -nan)
reports[-1].sigmaresid = ValErr(0.877318, 0.0133417, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0306874, None, -0.00242362, None, -0.00438819, None, -0.00237208, None, -0.00438819, None, -0.00237208, None, -0.0216112, None, -0.00257794, None, -0.0216112, None, -0.00257794, None, 0.877373, None, 0.0105583, None, 0.877373, None, 0.0105583, None)
reports[-1].CovMatrix = ['0.000433819','0.000153927','-1.99533e-06','9.76628e-08','0','0','0','0','0','0.000153927','0.257558','-1.15984e-06','3.87709e-06','0','0','0','0','0','-1.99533e-06','-1.15984e-06','5.11965e-08','1.05381e-09','0','0','0','0','0','9.76628e-08','3.87709e-06','1.05381e-09','0.000178002','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054656, ("CSC", 2, 2, 2, 16), "MEm22_16"))
reports[-1].posNum = 2086
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00388877, 0.0210648, 0), \
                           ValErr(-0.0181642, 0.502362, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.83587e-05, 0.000223616, 0), \
                           -2652.37, 2086, 2086, -nan)
reports[-1].sigmaresid = ValErr(0.862921, 0.0133597, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0119653, None, -0.00344595, None, -0.00104834, None, -0.00350827, None, -0.00104834, None, -0.00350827, None, -0.0127916, None, -0.00298812, None, -0.0127916, None, -0.00298812, None, 0.862943, None, 0.0123007, None, 0.862943, None, 0.0123007, None)
reports[-1].CovMatrix = ['0.000443724','-0.000224637','-2.08206e-06','9.11818e-08','0','0','0','0','0','-0.000224637','0.252367','2.32497e-06','3.8037e-06','0','0','0','0','0','-2.08206e-06','2.32497e-06','5.0004e-08','1.0511e-09','0','0','0','0','0','9.11818e-08','3.8037e-06','1.0511e-09','0.000178482','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054672, ("CSC", 2, 2, 2, 18), "MEm22_18"))
reports[-1].posNum = 1923
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.020414, 0.0220551, 0), \
                           ValErr(0.0701966, 0.527173, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000347561, 0.000236079, 0), \
                           -2486.18, 1923, 1923, -nan)
reports[-1].sigmaresid = ValErr(0.881531, 0.0142141, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0127773, None, -0.00186417, None, -0.00698272, None, -0.00148058, None, -0.00698272, None, -0.00148058, None, 0.0139019, None, -0.00154091, None, 0.0139019, None, -0.00154091, None, 0.882053, None, 0.0101904, None, 0.882053, None, 0.0101904, None)
reports[-1].CovMatrix = ['0.000486429','-0.000701104','-2.1145e-06','9.15496e-08','0','0','0','0','0','-0.000701104','0.277912','-1.64839e-06','3.94309e-06','0','0','0','0','0','-2.1145e-06','-1.64839e-06','5.57333e-08','1.19137e-09','0','0','0','0','0','9.15496e-08','3.94309e-06','1.19137e-09','0.000202042','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054688, ("CSC", 2, 2, 2, 20), "MEm22_20"))
reports[-1].posNum = 2009
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00240023, 0.021241, 0), \
                           ValErr(0.0378912, 0.515999, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000176095, 0.00022391, 0), \
                           -2602.04, 2009, 2009, -nan)
reports[-1].sigmaresid = ValErr(0.883586, 0.013939, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0061394, None, -0.00801112, None, 0.00381969, None, -0.00812942, None, 0.00381969, None, -0.00812942, None, 0.00225838, None, -0.00828973, None, 0.00225838, None, -0.00828973, None, 0.883742, None, 0.0102645, None, 0.883742, None, 0.0102645, None)
reports[-1].CovMatrix = ['0.000451178','0.000164664','-1.77089e-06','1.08877e-07','0','0','0','0','0','0.000164664','0.266255','-2.99106e-06','3.78488e-06','0','0','0','0','0','-1.77089e-06','-2.99106e-06','5.01356e-08','1.13049e-09','0','0','0','0','0','1.08877e-07','3.78488e-06','1.13049e-09','0.000194297','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054704, ("CSC", 2, 2, 2, 22), "MEm22_22"))
reports[-1].posNum = 1999
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00837106, 0.0219821, 0), \
                           ValErr(-0.261888, 0.52087, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.0113e-05, 0.000234135, 0), \
                           -2557.38, 1999, 1999, -nan)
reports[-1].sigmaresid = ValErr(0.869673, 0.0137536, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00424531, None, 0.00172703, None, -0.00609919, None, 0.00196052, None, -0.00609919, None, 0.00196052, None, 0.00941971, None, 0.00174598, None, 0.00941971, None, 0.00174598, None, 0.869767, None, 0.0112839, None, 0.869767, None, 0.0112839, None)
reports[-1].CovMatrix = ['0.000483212','-0.000465455','-2.39162e-06','7.58563e-08','0','0','0','0','0','-0.000465455','0.271306','2.08215e-06','4.69511e-06','0','0','0','0','0','-2.39162e-06','2.08215e-06','5.48192e-08','1.3577e-09','0','0','0','0','0','7.58563e-08','4.69511e-06','1.3577e-09','0.000189164','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054720, ("CSC", 2, 2, 2, 24), "MEm22_24"))
reports[-1].posNum = 2085
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000348131, 0.0215901, 0), \
                           ValErr(0.0762752, 0.510555, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.78545e-05, 0.000237819, 0), \
                           -2610.58, 2085, 2085, -nan)
reports[-1].sigmaresid = ValErr(0.846318, 0.0131059, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00323413, None, 0.0043212, None, -0.00298255, None, 0.00439167, None, -0.00298255, None, 0.00439167, None, -0.0469793, None, 0.00463269, None, -0.0469793, None, 0.00463269, None, 0.846336, None, 0.0113971, None, 0.846336, None, 0.0113971, None)
reports[-1].CovMatrix = ['0.000466134','0.000341634','-2.62303e-06','1.18338e-07','0','0','0','0','0','0.000341634','0.260666','3.39278e-06','4.32837e-06','0','0','0','0','0','-2.62303e-06','3.39278e-06','5.65578e-08','7.4692e-10','0','0','0','0','0','1.18338e-07','4.32837e-06','7.4692e-10','0.000171765','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054736, ("CSC", 2, 2, 2, 26), "MEm22_26"))
reports[-1].posNum = 1455
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00492541, 0.0252054, 0), \
                           ValErr(0.438277, 0.62573, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.31369e-05, 0.000265851, 0), \
                           -1849.42, 1455, 1455, -nan)
reports[-1].sigmaresid = ValErr(0.862549, 0.0159894, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00911702, None, 0.0018485, None, 0.00634274, None, 0.0020667, None, 0.00634274, None, 0.0020667, None, 0.0449886, None, 0.00176687, None, 0.0449886, None, 0.00176687, None, 0.862703, None, 0.0101421, None, 0.862703, None, 0.0101421, None)
reports[-1].CovMatrix = ['0.000635314','0.000123039','-2.95641e-06','1.3994e-07','0','0','0','0','0','0.000123039','0.391538','5.43843e-06','5.82991e-06','0','0','0','0','0','-2.95641e-06','5.43843e-06','7.0677e-08','1.49438e-09','0','0','0','0','0','1.3994e-07','5.82991e-06','1.49438e-09','0.000255665','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054752, ("CSC", 2, 2, 2, 28), "MEm22_28"))
reports[-1].posNum = 1750
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000597271, 0.024148, 0), \
                           ValErr(-0.331112, 0.562299, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.58433e-05, 0.000259814, 0), \
                           -2285.15, 1750, 1750, -nan)
reports[-1].sigmaresid = ValErr(0.893013, 0.0150943, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00138455, None, -0.00182428, None, -0.00185629, None, -0.00179862, None, -0.00185629, None, -0.00179862, None, 0.0141468, None, -0.00197917, None, 0.0141468, None, -0.00197917, None, 0.893124, None, 0.00974614, None, 0.893124, None, 0.00974614, None)
reports[-1].CovMatrix = ['0.000583124','-0.0001582','-2.92694e-06','1.51367e-07','0','0','0','0','0','-0.0001582','0.31618','-5.63995e-06','4.69486e-06','0','0','0','0','0','-2.92694e-06','-5.63995e-06','6.75033e-08','9.65607e-10','0','0','0','0','0','1.51367e-07','4.69486e-06','9.65607e-10','0.000227841','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054768, ("CSC", 2, 2, 2, 30), "MEm22_30"))
reports[-1].posNum = 899
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0088297, 0.0358367, 0), \
                           ValErr(-0.144429, 0.735028, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.29385e-05, 0.000332932, 0), \
                           -1045.99, 899, 899, -nan)
reports[-1].sigmaresid = ValErr(0.774585, 0.0182673, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0222826, None, -0.00298627, None, -0.00521572, None, -0.00273017, None, -0.00521572, None, -0.00273017, None, 0.0237826, None, -0.00306518, None, 0.0237826, None, -0.00306518, None, 0.774598, None, 0.00998259, None, 0.774598, None, 0.00998259, None)
reports[-1].CovMatrix = ['0.00128427','0.00842497','-7.94702e-06','2.76418e-07','0','0','0','0','0','0.00842497','0.540266','-4.85407e-05','8.88308e-06','0','0','0','0','0','-7.94702e-06','-4.85407e-05','1.10843e-07','6.62832e-10','0','0','0','0','0','2.76418e-07','8.88308e-06','6.62832e-10','0.0003337','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054784, ("CSC", 2, 2, 2, 32), "MEm22_32"))
reports[-1].posNum = 1364
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00118524, 0.0272712, 0), \
                           ValErr(0.124596, 0.606467, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.09013e-05, 0.000271372, 0), \
                           -1655.8, 1364, 1364, -nan)
reports[-1].sigmaresid = ValErr(0.814652, 0.0155975, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0332367, None, 0.0017446, None, -0.00334071, None, 0.00228945, None, -0.00334071, None, 0.00228945, None, 0.023651, None, 0.0022078, None, 0.023651, None, 0.0022078, None, 0.814661, None, 0.0110224, None, 0.814661, None, 0.0110224, None)
reports[-1].CovMatrix = ['0.000743718','-0.000143919','-4.34343e-06','5.16205e-08','0','0','0','0','0','-0.000143919','0.367802','-7.78198e-06','5.81693e-06','0','0','0','0','0','-4.34343e-06','-7.78198e-06','7.36426e-08','1.49556e-09','0','0','0','0','0','5.16205e-08','5.81693e-06','1.49556e-09','0.000243284','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054800, ("CSC", 2, 2, 2, 34), "MEm22_34"))
reports[-1].posNum = 2113
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0083737, 0.0209418, 0), \
                           ValErr(0.0447467, 0.506784, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000169785, 0.000228554, 0), \
                           -2773.16, 2113, 2113, -nan)
reports[-1].sigmaresid = ValErr(0.898952, 0.0138281, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0153596, None, 4.71003e-05, None, 0.00279909, None, 0.000565928, None, 0.00279909, None, 0.000565928, None, 0.00100329, None, 0.000636609, None, 0.00100329, None, 0.000636609, None, 0.899085, None, 0.0113973, None, 0.899085, None, 0.0113973, None)
reports[-1].CovMatrix = ['0.000438557','-2.81626e-05','-1.71187e-06','1.18769e-07','0','0','0','0','0','-2.81626e-05','0.25683','-5.00528e-07','3.76354e-06','0','0','0','0','0','-1.71187e-06','-5.00528e-07','5.22368e-08','1.20308e-09','0','0','0','0','0','1.18769e-07','3.76354e-06','1.20308e-09','0.000191218','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054816, ("CSC", 2, 2, 2, 36), "MEm22_36"))
reports[-1].posNum = 1970
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00459348, 0.0216686, 0), \
                           ValErr(-0.109394, 0.509822, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.60868e-05, 0.000231867, 0), \
                           -2533.04, 1970, 1970, -nan)
reports[-1].sigmaresid = ValErr(0.875344, 0.0139452, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0431133, None, -0.000349212, None, 0.00387891, None, -7.05807e-05, None, 0.00387891, None, -7.05807e-05, None, -0.0316071, None, -0.000311868, None, -0.0316071, None, -0.000311868, None, 0.875362, None, 0.0104174, None, 0.875362, None, 0.0104174, None)
reports[-1].CovMatrix = ['0.00046953','-0.000311711','-2.07907e-06','1.06679e-07','0','0','0','0','0','-0.000311711','0.259918','2.43668e-06','4.23953e-06','0','0','0','0','0','-2.07907e-06','2.43668e-06','5.37624e-08','1.10329e-09','0','0','0','0','0','1.06679e-07','4.23953e-06','1.10329e-09','0.00019447','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058120, ("CSC", 2, 3, 1, 1), "MEm31_01"))
reports[-1].posNum = 5052
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00205927, 0.00624831, 0), \
                           ValErr(0.0162784, 0.0718225, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000103475, 0.000144798, 0), \
                           -3048.18, 5052, 5052, -nan)
reports[-1].sigmaresid = ValErr(0.442384, 0.00440101, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00445701, None, -0.000148245, None, -0.00164711, None, -6.40038e-05, None, -0.00164711, None, -6.40038e-05, None, 0.0069144, None, -8.13787e-05, None, 0.0069144, None, -8.13787e-05, None, 0.442408, None, 0.01168, None, 0.442408, None, 0.01168, None)
reports[-1].CovMatrix = ['3.90414e-05','-1.14702e-05','-7.69344e-08','9.15576e-09','0','0','0','0','0','-1.14702e-05','0.00515848','2.73347e-07','1.19476e-07','0','0','0','0','0','-7.69344e-08','2.73347e-07','2.09665e-08','2.1912e-10','0','0','0','0','0','9.15576e-09','1.19476e-07','2.1912e-10','1.93689e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058136, ("CSC", 2, 3, 1, 3), "MEm31_03"))
reports[-1].posNum = 4869
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00229707, 0.00642354, 0), \
                           ValErr(-0.042977, 0.0749812, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.51618e-05, 0.000146364, 0), \
                           -2992.72, 4869, 4869, -nan)
reports[-1].sigmaresid = ValErr(0.447405, 0.00453383, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000244821, None, 0.00113566, None, 0.00210822, None, 0.00146114, None, 0.00210822, None, 0.00146114, None, -0.00218667, None, 0.00135251, None, -0.00218667, None, 0.00135251, None, 0.447437, None, 0.0108526, None, 0.447437, None, 0.0108526, None)
reports[-1].CovMatrix = ['4.12619e-05','5.0068e-06','-5.61367e-08','1.05919e-08','0','0','0','0','0','5.0068e-06','0.00562219','-2.40645e-07','1.28947e-07','0','0','0','0','0','-5.61367e-08','-2.40645e-07','2.14225e-08','2.38529e-10','0','0','0','0','0','1.05919e-08','1.28947e-07','2.38529e-10','2.05557e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058152, ("CSC", 2, 3, 1, 5), "MEm31_05"))
reports[-1].posNum = 4792
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00128476, 0.00632909, 0), \
                           ValErr(-0.00828183, 0.0722539, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.49898e-05, 0.00014777, 0), \
                           -2836.74, 4792, 4792, -nan)
reports[-1].sigmaresid = ValErr(0.437375, 0.00446765, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00119465, None, 0.00345602, None, 0.0012609, None, 0.00351091, None, 0.0012609, None, 0.00351091, None, 0.00648809, None, 0.00378287, None, 0.00648809, None, 0.00378287, None, 0.437376, None, 0.0115867, None, 0.437376, None, 0.0115867, None)
reports[-1].CovMatrix = ['4.00574e-05','7.31343e-06','-5.27641e-08','1.0126e-08','0','0','0','0','0','7.31343e-06','0.00522062','-4.52439e-08','1.22767e-07','0','0','0','0','0','-5.27641e-08','-4.52439e-08','2.1836e-08','2.33218e-10','0','0','0','0','0','1.0126e-08','1.22767e-07','2.33218e-10','1.99599e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058168, ("CSC", 2, 3, 1, 7), "MEm31_07"))
reports[-1].posNum = 4852
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00465381, 0.00658369, 0), \
                           ValErr(-0.034843, 0.0757002, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000183714, 0.000151806, 0), \
                           -3079.81, 4852, 4852, -nan)
reports[-1].sigmaresid = ValErr(0.456491, 0.00463401, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00900415, None, -0.00140522, None, 0.0040151, None, -0.00116127, None, 0.0040151, None, -0.00116127, None, 0.00226893, None, -0.00128563, None, 0.00226893, None, -0.00128563, None, 0.45657, None, 0.0118102, None, 0.45657, None, 0.0118102, None)
reports[-1].CovMatrix = ['4.33449e-05','1.49794e-05','-9.12871e-08','1.12797e-08','0','0','0','0','0','1.49794e-05','0.00573053','-1.93229e-07','1.39554e-07','0','0','0','0','0','-9.12871e-08','-1.93229e-07','2.30452e-08','2.52217e-10','0','0','0','0','0','1.12797e-08','1.39554e-07','2.52217e-10','2.14741e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058184, ("CSC", 2, 3, 1, 9), "MEm31_09"))
reports[-1].posNum = 4924
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0014082, 0.0063613, 0), \
                           ValErr(0.0195342, 0.0725877, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000168984, 0.000147716, 0), \
                           -2991.91, 4924, 4924, -nan)
reports[-1].sigmaresid = ValErr(0.444273, 0.0044769, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00284078, None, -0.00182676, None, 0.000706102, None, -0.00184622, None, 0.000706102, None, -0.00184622, None, -0.00112742, None, -0.00187467, None, -0.00112742, None, -0.00187467, None, 0.444333, None, 0.0113532, None, 0.444333, None, 0.0113532, None)
reports[-1].CovMatrix = ['4.04661e-05','-1.23011e-06','-9.11292e-08','9.91334e-09','0','0','0','0','0','-1.23011e-06','0.00526897','-9.67921e-08','1.22768e-07','0','0','0','0','0','-9.11292e-08','-9.67921e-08','2.18199e-08','2.46274e-10','0','0','0','0','0','9.91334e-09','1.22768e-07','2.46274e-10','2.00427e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058200, ("CSC", 2, 3, 1, 11), "MEm31_11"))
reports[-1].posNum = 4931
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00572088, 0.0062002, 0), \
                           ValErr(-0.0384865, 0.0711951, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.49391e-05, 0.000144128, 0), \
                           -2880.01, 4931, 4931, -nan)
reports[-1].sigmaresid = ValErr(0.433929, 0.00436955, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00345907, None, 0.0010248, None, 0.00559907, None, 0.00122539, None, 0.00559907, None, 0.00122539, None, 0.0120103, None, 0.00124904, None, 0.0120103, None, 0.00124904, None, 0.433945, None, 0.0115488, None, 0.433945, None, 0.0115488, None)
reports[-1].CovMatrix = ['3.84425e-05','3.58023e-06','-7.26293e-08','8.76679e-09','0','0','0','0','0','3.58023e-06','0.00506874','3.90492e-08','1.17274e-07','0','0','0','0','0','-7.26293e-08','3.90492e-08','2.07729e-08','2.17989e-10','0','0','0','0','0','8.76679e-09','1.17274e-07','2.17989e-10','1.9093e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058216, ("CSC", 2, 3, 1, 13), "MEm31_13"))
reports[-1].posNum = 4985
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00043056, 0.00613516, 0), \
                           ValErr(-0.0420444, 0.0706009, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000104875, 0.000142808, 0), \
                           -2881.83, 4985, 4985, -nan)
reports[-1].sigmaresid = ValErr(0.431349, 0.00431998, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00189085, None, 0.00107281, None, 0.000129905, None, 0.000784631, None, 0.000129905, None, 0.000784631, None, 0.0013093, None, 0.000857327, None, 0.0013093, None, 0.000857327, None, 0.431388, None, 0.0109693, None, 0.431388, None, 0.0109693, None)
reports[-1].CovMatrix = ['3.76402e-05','1.19046e-05','-7.71057e-08','9.20078e-09','0','0','0','0','0','1.19046e-05','0.00498449','-2.39415e-07','1.11107e-07','0','0','0','0','0','-7.71057e-08','-2.39415e-07','2.03942e-08','2.16461e-10','0','0','0','0','0','9.20078e-09','1.11107e-07','2.16461e-10','1.86622e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058232, ("CSC", 2, 3, 1, 15), "MEm31_15"))
reports[-1].posNum = 4660
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00480499, 0.0065556, 0), \
                           ValErr(0.0363471, 0.0770936, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000111512, 0.000152383, 0), \
                           -2830.07, 4660, 4660, -nan)
reports[-1].sigmaresid = ValErr(0.444134, 0.0046005, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0038852, None, -0.00248007, None, -0.00412021, None, -0.00219014, None, -0.00412021, None, -0.00219014, None, -0.000367213, None, -0.00236439, None, -0.000367213, None, -0.00236439, None, 0.444169, None, 0.0111183, None, 0.444169, None, 0.0111183, None)
reports[-1].CovMatrix = ['4.29758e-05','-3.5717e-05','-1.0343e-07','9.56685e-09','0','0','0','0','0','-3.5717e-05','0.00594342','5.68059e-07','1.33109e-07','0','0','0','0','0','-1.0343e-07','5.68059e-07','2.32206e-08','2.50817e-10','0','0','0','0','0','9.56685e-09','1.33109e-07','2.50817e-10','2.11646e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058248, ("CSC", 2, 3, 1, 17), "MEm31_17"))
reports[-1].posNum = 4733
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000947821, 0.00647042, 0), \
                           ValErr(0.00838109, 0.0749799, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.02927e-06, 0.000148273, 0), \
                           -2857.4, 4733, 4733, -nan)
reports[-1].sigmaresid = ValErr(0.442542, 0.00454852, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00460696, None, 0.000792596, None, -0.00088223, None, 0.000833942, None, -0.00088223, None, 0.000833942, None, 0.00388695, None, 0.000529474, None, 0.00388695, None, 0.000529474, None, 0.442543, None, 0.010999, None, 0.442543, None, 0.010999, None)
reports[-1].CovMatrix = ['4.18663e-05','-1.59133e-05','-9.79223e-08','9.75269e-09','0','0','0','0','0','-1.59133e-05','0.00562198','-2.62764e-07','1.22136e-07','0','0','0','0','0','-9.79223e-08','-2.62764e-07','2.19848e-08','2.25643e-10','0','0','0','0','0','9.75269e-09','1.22136e-07','2.25643e-10','2.06891e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058128, ("CSC", 2, 3, 1, 2), "MEm31_02"))
reports[-1].posNum = 4757
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00138933, 0.00687923, 0), \
                           ValErr(-0.00865572, 0.078729, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.62015e-06, 0.000160259, 0), \
                           -3183.09, 4757, 4757, -nan)
reports[-1].sigmaresid = ValErr(0.47246, 0.00484377, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00730276, None, 0.000312699, None, 0.00135457, None, 0.000474389, None, 0.00135457, None, 0.000474389, None, -0.00464273, None, 0.000323366, None, -0.00464273, None, 0.000323366, None, 0.472461, None, 0.0102355, None, 0.472461, None, 0.0102355, None)
reports[-1].CovMatrix = ['4.73238e-05','2.84978e-06','-1.01188e-07','1.22115e-08','0','0','0','0','0','2.84978e-06','0.00619825','-1.47718e-07','1.51444e-07','0','0','0','0','0','-1.01188e-07','-1.47718e-07','2.56828e-08','2.78235e-10','0','0','0','0','0','1.22115e-08','1.51444e-07','2.78235e-10','2.34621e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058144, ("CSC", 2, 3, 1, 4), "MEm31_04"))
reports[-1].posNum = 3815
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00330121, 0.00751528, 0), \
                           ValErr(0.0610813, 0.0867478, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.41281e-05, 0.000173684, 0), \
                           -2476.65, 3815, 3815, -nan)
reports[-1].sigmaresid = ValErr(0.463129, 0.005302, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00653171, None, -0.000572314, None, 0.00370639, None, -0.000524252, None, 0.00370639, None, -0.000524252, None, 0.0109246, None, -0.00054062, None, 0.0109246, None, -0.00054062, None, 0.463168, None, 0.0110473, None, 0.463168, None, 0.0110473, None)
reports[-1].CovMatrix = ['5.64795e-05','-3.44446e-05','-5.78221e-08','1.41148e-08','0','0','0','0','0','-3.44446e-05','0.00752518','6.74781e-07','1.75508e-07','0','0','0','0','0','-5.78221e-08','6.74781e-07','3.01662e-08','3.57684e-10','0','0','0','0','0','1.41148e-08','1.75508e-07','3.57684e-10','2.81113e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058160, ("CSC", 2, 3, 1, 6), "MEm31_06"))
reports[-1].posNum = 4874
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00112526, 0.00651373, 0), \
                           ValErr(-0.0074666, 0.0746122, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.98485e-05, 0.000150798, 0), \
                           -3054.19, 4874, 4874, -nan)
reports[-1].sigmaresid = ValErr(0.452797, 0.00458612, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00378672, None, 0.0031208, None, -0.00118648, None, 0.00329728, None, -0.00118648, None, 0.00329728, None, 0.00446201, None, 0.00327432, None, 0.00446201, None, 0.00327432, None, 0.452799, None, 0.00956595, None, 0.452799, None, 0.00956595, None)
reports[-1].CovMatrix = ['4.24286e-05','1.31782e-05','-8.77034e-08','1.09863e-08','0','0','0','0','0','1.31782e-05','0.00556699','-3.45245e-07','1.32241e-07','0','0','0','0','0','-8.77034e-08','-3.45245e-07','2.274e-08','2.35397e-10','0','0','0','0','0','1.09863e-08','1.32241e-07','2.35397e-10','2.10325e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058176, ("CSC", 2, 3, 1, 8), "MEm31_08"))
reports[-1].posNum = 4405
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000697915, 0.00693314, 0), \
                           ValErr(0.0465577, 0.0800256, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000115609, 0.000165642, 0), \
                           -2749.01, 4405, 4405, -nan)
reports[-1].sigmaresid = ValErr(0.451639, 0.00481176, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00887689, None, -5.15903e-05, None, -0.001678, None, 0.000119592, None, -0.001678, None, 0.000119592, None, 0.00587134, None, 0.000221701, None, 0.00587134, None, 0.000221701, None, 0.451682, None, 0.00981796, None, 0.451682, None, 0.00981796, None)
reports[-1].CovMatrix = ['4.80685e-05','7.13699e-06','-2.19414e-07','1.11595e-08','0','0','0','0','0','7.13699e-06','0.0064041','-9.55675e-09','1.46733e-07','0','0','0','0','0','-2.19414e-07','-9.55675e-09','2.74374e-08','2.58532e-10','0','0','0','0','0','1.11595e-08','1.46733e-07','2.58532e-10','2.3153e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058192, ("CSC", 2, 3, 1, 10), "MEm31_10"))
reports[-1].posNum = 5080
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000284003, 0.0063828, 0), \
                           ValErr(-0.0434325, 0.0735913, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000169401, 0.000148651, 0), \
                           -3189.28, 5080, 5080, -nan)
reports[-1].sigmaresid = ValErr(0.453334, 0.00449751, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00403409, None, 0.00311687, None, -0.000319595, None, 0.00321437, None, -0.000319595, None, 0.00321437, None, 0.00342273, None, 0.00317983, None, 0.00342273, None, 0.00317983, None, 0.453406, None, 0.010347, None, 0.453406, None, 0.010347, None)
reports[-1].CovMatrix = ['4.07402e-05','2.10739e-07','-7.93516e-08','1.02884e-08','0','0','0','0','0','2.10739e-07','0.00541568','1.58392e-07','1.29595e-07','0','0','0','0','0','-7.93516e-08','1.58392e-07','2.20972e-08','2.54456e-10','0','0','0','0','0','1.02884e-08','1.29595e-07','2.54456e-10','2.02277e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058208, ("CSC", 2, 3, 1, 12), "MEm31_12"))
reports[-1].posNum = 5023
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000848273, 0.00655165, 0), \
                           ValErr(-0.00159869, 0.0762776, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000129476, 0.000153893, 0), \
                           -3260.04, 5023, 5023, -nan)
reports[-1].sigmaresid = ValErr(0.463052, 0.00461991, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00413053, None, 0.00208362, None, 0.000444666, None, 0.00208304, None, 0.000444666, None, 0.00208304, None, 0.00588578, None, 0.00230435, None, 0.00588578, None, 0.00230435, None, 0.463085, None, 0.00987722, None, 0.463085, None, 0.00987722, None)
reports[-1].CovMatrix = ['4.29241e-05','5.94843e-06','-7.39828e-08','1.12714e-08','0','0','0','0','0','5.94843e-06','0.00581827','-3.85789e-08','1.39435e-07','0','0','0','0','0','-7.39828e-08','-3.85789e-08','2.36831e-08','2.64185e-10','0','0','0','0','0','1.12714e-08','1.39435e-07','2.64185e-10','2.13436e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058224, ("CSC", 2, 3, 1, 14), "MEm31_14"))
reports[-1].posNum = 4822
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00308186, 0.00658313, 0), \
                           ValErr(0.00725014, 0.0753555, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.66978e-05, 0.000152627, 0), \
                           -3040.67, 4822, 4822, -nan)
reports[-1].sigmaresid = ValErr(0.454591, 0.00462905, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00702678, None, 0.00240177, None, 0.00268065, None, 0.00242705, None, 0.00268065, None, 0.00242705, None, -0.00128672, None, 0.00256394, None, -0.00128672, None, 0.00256394, None, 0.454607, None, 0.00900728, None, 0.454607, None, 0.00900728, None)
reports[-1].CovMatrix = ['4.33377e-05','4.64313e-06','-1.05188e-07','1.08121e-08','0','0','0','0','0','4.64313e-06','0.00567846','3.04598e-07','1.39562e-07','0','0','0','0','0','-1.05188e-07','3.04598e-07','2.3295e-08','2.56323e-10','0','0','0','0','0','1.08121e-08','1.39562e-07','2.56323e-10','2.14281e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058240, ("CSC", 2, 3, 1, 16), "MEm31_16"))
reports[-1].posNum = 4682
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000623961, 0.00680058, 0), \
                           ValErr(-0.0074094, 0.0777784, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000145861, 0.000158909, 0), \
                           -3035.56, 4682, 4682, -nan)
reports[-1].sigmaresid = ValErr(0.462739, 0.00478196, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000303404, None, -0.00270915, None, -0.00128478, None, -0.00264135, None, -0.00128478, None, -0.00264135, None, -0.00242507, None, -0.00289059, None, -0.00242507, None, -0.00289059, None, 0.462781, None, 0.00985405, None, 0.462781, None, 0.00985405, None)
reports[-1].CovMatrix = ['4.62478e-05','-1.32715e-06','-1.13872e-07','1.16383e-08','0','0','0','0','0','-1.32715e-06','0.00604948','1.21704e-07','1.47205e-07','0','0','0','0','0','-1.13872e-07','1.21704e-07','2.52521e-08','2.81721e-10','0','0','0','0','0','1.16383e-08','1.47205e-07','2.81721e-10','2.28672e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058256, ("CSC", 2, 3, 1, 18), "MEm31_18"))
reports[-1].posNum = 4796
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000421152, 0.00660618, 0), \
                           ValErr(-0.0116708, 0.0762111, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.37939e-05, 0.000152907, 0), \
                           -3041.94, 4796, 4796, -nan)
reports[-1].sigmaresid = ValErr(0.456269, 0.00465871, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00468579, None, 0.000504399, None, -0.000358102, None, 0.000395711, None, -0.000358102, None, 0.000395711, None, -0.00303538, None, 0.000383205, None, -0.00303538, None, 0.000383205, None, 0.456271, None, 0.00996106, None, 0.456271, None, 0.00996106, None)
reports[-1].CovMatrix = ['4.36416e-05','1.08504e-05','-7.09578e-08','1.1393e-08','0','0','0','0','0','1.08504e-05','0.00580814','-1.14731e-07','1.39961e-07','0','0','0','0','0','-7.09578e-08','-1.14731e-07','2.33807e-08','2.54899e-10','0','0','0','0','0','1.1393e-08','1.39961e-07','2.54899e-10','2.17036e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058632, ("CSC", 2, 3, 2, 1), "MEm32_01"))
reports[-1].posNum = 2192
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00954231, 0.0218793, 0), \
                           ValErr(-0.209342, 0.540814, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000105894, 0.000240383, 0), \
                           -3007.96, 2192, 2192, -nan)
reports[-1].sigmaresid = ValErr(0.95436, 0.0144134, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.007268, None, -0.000263455, None, 0.00623957, None, 8.7644e-06, None, 0.00623957, None, 8.7644e-06, None, 0.0235183, None, 3.42602e-06, None, 0.0235183, None, 3.42602e-06, None, 0.954452, None, 0.0128188, None, 0.954452, None, 0.0128188, None)
reports[-1].CovMatrix = ['0.000478705','0.000235872','-1.90762e-06','1.26194e-07','0','0','0','0','0','0.000235872','0.292479','4.74495e-07','5.0008e-06','0','0','0','0','0','-1.90762e-06','4.74495e-07','5.77842e-08','1.21195e-09','0','0','0','0','0','1.26194e-07','5.0008e-06','1.21195e-09','0.000207747','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058648, ("CSC", 2, 3, 2, 3), "MEm32_03"))
reports[-1].posNum = 1898
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.012224, 0.0217362, 0), \
                           ValErr(0.112537, 0.515461, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000125593, 0.000244853, 0), \
                           -2377.49, 1898, 1898, -nan)
reports[-1].sigmaresid = ValErr(0.846773, 0.0137434, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00811525, None, -0.00284153, None, 0.00744994, None, -0.0022278, None, 0.00744994, None, -0.0022278, None, -0.0327617, None, -0.00249627, None, -0.0327617, None, -0.00249627, None, 0.846856, None, 0.0118582, None, 0.846856, None, 0.0118582, None)
reports[-1].CovMatrix = ['0.000472464','-0.000696068','-2.37498e-06','9.11518e-08','0','0','0','0','0','-0.000696068','0.2657','7.49508e-06','3.31007e-06','0','0','0','0','0','-2.37498e-06','7.49508e-06','5.99529e-08','1.17253e-09','0','0','0','0','0','9.11518e-08','3.31007e-06','1.17253e-09','0.000188883','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058664, ("CSC", 2, 3, 2, 5), "MEm32_05"))
reports[-1].posNum = 1746
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0164591, 0.025352, 0), \
                           ValErr(0.231006, 0.551761, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.7016e-05, 0.000270672, 0), \
                           -2165.32, 1746, 1746, -nan)
reports[-1].sigmaresid = ValErr(0.836294, 0.0141521, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00605551, None, -0.00288494, None, 0.0111345, None, -0.00201465, None, 0.0111345, None, -0.00201465, None, 0.0134013, None, -0.00279741, None, 0.0134013, None, -0.00279741, None, 0.836369, None, 0.012673, None, 0.836369, None, 0.012673, None)
reports[-1].CovMatrix = ['0.000642722','-0.000637775','-4.20881e-06','1.03546e-07','0','0','0','0','0','-0.000637775','0.304441','5.25681e-06','3.63242e-06','0','0','0','0','0','-4.20881e-06','5.25681e-06','7.32634e-08','9.2567e-10','0','0','0','0','0','1.03546e-07','3.63242e-06','9.2567e-10','0.000200283','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058680, ("CSC", 2, 3, 2, 7), "MEm32_07"))
reports[-1].posNum = 2106
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0253625, 0.0227143, 0), \
                           ValErr(0.426467, 0.545163, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000280002, 0.000248496, 0), \
                           -2775.98, 2106, 2106, -nan)
reports[-1].sigmaresid = ValErr(0.904112, 0.0139309, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00604012, None, 0.00106747, None, 0.0130937, None, 0.00141937, None, 0.0130937, None, 0.00141937, None, -0.00610712, None, 0.00130481, None, -0.00610712, None, 0.00130481, None, 0.904523, None, 0.012336, None, 0.904523, None, 0.012336, None)
reports[-1].CovMatrix = ['0.000515942','-0.000491213','-2.80622e-06','8.70289e-08','0','0','0','0','0','-0.000491213','0.297203','4.51181e-06','4.01429e-06','0','0','0','0','0','-2.80622e-06','4.51181e-06','6.17503e-08','1.14872e-09','0','0','0','0','0','8.70289e-08','4.01429e-06','1.14872e-09','0.000194073','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058696, ("CSC", 2, 3, 2, 9), "MEm32_09"))
reports[-1].posNum = 1919
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0136237, 0.0242616, 0), \
                           ValErr(0.0902769, 0.548193, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.73575e-05, 0.000271308, 0), \
                           -2467.11, 1919, 1919, -nan)
reports[-1].sigmaresid = ValErr(0.875204, 0.0141275, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0175185, None, -0.00272867, None, -0.017197, None, -0.0022586, None, -0.017197, None, -0.0022586, None, -0.0185472, None, -0.00290413, None, -0.0185472, None, -0.00290413, None, 0.875208, None, 0.0123522, None, 0.875208, None, 0.0123522, None)
reports[-1].CovMatrix = ['0.000588626','0.00135121','-3.72175e-06','1.31414e-07','0','0','0','0','0','0.00135121','0.300516','-1.44665e-05','5.13679e-06','0','0','0','0','0','-3.72175e-06','-1.44665e-05','7.36079e-08','7.71707e-10','0','0','0','0','0','1.31414e-07','5.13679e-06','7.71707e-10','0.000199587','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058712, ("CSC", 2, 3, 2, 11), "MEm32_11"))
reports[-1].posNum = 2153
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0034356, 0.0220695, 0), \
                           ValErr(0.269077, 0.537034, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000146312, 0.000246253, 0), \
                           -2900.91, 2153, 2153, -nan)
reports[-1].sigmaresid = ValErr(0.930942, 0.0141868, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0196694, None, -0.00114521, None, -0.00882882, None, -0.000509129, None, -0.00882882, None, -0.000509129, None, -0.0153875, None, -0.000911995, None, -0.0153875, None, -0.000911995, None, 0.931078, None, 0.012281, None, 0.931078, None, 0.012281, None)
reports[-1].CovMatrix = ['0.000487061','-0.000261005','-2.2637e-06','1.21375e-07','0','0','0','0','0','-0.000261005','0.288405','4.73832e-06','3.61488e-06','0','0','0','0','0','-2.2637e-06','4.73832e-06','6.06403e-08','1.19389e-09','0','0','0','0','0','1.21375e-07','3.61488e-06','1.19389e-09','0.000201266','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058728, ("CSC", 2, 3, 2, 13), "MEm32_13"))
reports[-1].posNum = 1982
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0129206, 0.0216128, 0), \
                           ValErr(-0.126558, 0.526939, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.99614e-06, 0.000238273, 0), \
                           -2583.48, 1982, 1982, -nan)
reports[-1].sigmaresid = ValErr(0.890927, 0.0141501, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0240927, None, 0.000117412, None, 0.0130577, None, 0.000431504, None, 0.0130577, None, 0.000431504, None, 0.0193793, None, 0.00020967, None, 0.0193793, None, 0.00020967, None, 0.890963, None, 0.0121847, None, 0.890963, None, 0.0121847, None)
reports[-1].CovMatrix = ['0.000467113','0.00065746','-1.9264e-06','1.27582e-07','0','0','0','0','0','0.00065746','0.277664','-1.88522e-06','4.78265e-06','0','0','0','0','0','-1.9264e-06','-1.88522e-06','5.6774e-08','1.16968e-09','0','0','0','0','0','1.27582e-07','4.78265e-06','1.16968e-09','0.000200226','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058744, ("CSC", 2, 3, 2, 15), "MEm32_15"))
reports[-1].posNum = 2231
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0037578, 0.0218252, 0), \
                           ValErr(0.200258, 0.520917, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000110268, 0.000246408, 0), \
                           -3046.86, 2231, 2231, -nan)
reports[-1].sigmaresid = ValErr(0.948119, 0.0141932, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0283465, None, 0.000413682, None, -7.49391e-05, None, 0.000814632, None, -7.49391e-05, None, 0.000814632, None, 0.0137198, None, 0.000855275, None, 0.0137198, None, 0.000855275, None, 0.94822, None, 0.012424, None, 0.94822, None, 0.012424, None)
reports[-1].CovMatrix = ['0.000476337','5.84858e-05','-2.11116e-06','1.29146e-07','0','0','0','0','0','5.84858e-05','0.271355','-2.66922e-06','3.53859e-06','0','0','0','0','0','-2.11116e-06','-2.66922e-06','6.07171e-08','1.23128e-09','0','0','0','0','0','1.29146e-07','3.53859e-06','1.23128e-09','0.000201448','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058760, ("CSC", 2, 3, 2, 17), "MEm32_17"))
reports[-1].posNum = 1948
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0161339, 0.0226333, 0), \
                           ValErr(0.0608062, 0.547591, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000197877, 0.000241168, 0), \
                           -2566, 1948, 1948, -nan)
reports[-1].sigmaresid = ValErr(0.903299, 0.0144715, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0069039, None, -0.00340437, None, 0.00825651, None, -0.00344247, None, 0.00825651, None, -0.00344247, None, 0.0155913, None, -0.00371314, None, 0.0155913, None, -0.00371314, None, 0.903469, None, 0.0118812, None, 0.903469, None, 0.0118812, None)
reports[-1].CovMatrix = ['0.000512266','-0.000219436','-2.32659e-06','1.2249e-07','0','0','0','0','0','-0.000219436','0.299856','-2.41316e-06','3.96097e-06','0','0','0','0','0','-2.32659e-06','-2.41316e-06','5.81622e-08','1.18112e-09','0','0','0','0','0','1.2249e-07','3.96097e-06','1.18112e-09','0.000209426','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058776, ("CSC", 2, 3, 2, 19), "MEm32_19"))
reports[-1].posNum = 1580
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00343129, 0.0252058, 0), \
                           ValErr(-0.409844, 0.617736, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.31946e-05, 0.00027, 0), \
                           -2050.77, 1580, 1580, -nan)
reports[-1].sigmaresid = ValErr(0.886037, 0.0157616, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000828501, None, 0.00258254, None, -0.00617683, None, 0.00285827, None, -0.00617683, None, 0.00285827, None, -0.0110752, None, 0.00251742, None, -0.0110752, None, 0.00251742, None, 0.886187, None, 0.0116636, None, 0.886187, None, 0.0116636, None)
reports[-1].CovMatrix = ['0.000635334','-0.0045796','-2.59084e-06','1.06328e-07','0','0','0','0','0','-0.0045796','0.381597','1.07282e-05','4.03235e-06','0','0','0','0','0','-2.59084e-06','1.07282e-05','7.29002e-08','1.6706e-09','0','0','0','0','0','1.06328e-07','4.03235e-06','1.6706e-09','0.00024843','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058792, ("CSC", 2, 3, 2, 21), "MEm32_21"))
reports[-1].posNum = 2078
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00626357, 0.0216375, 0), \
                           ValErr(0.17328, 0.516752, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.32474e-05, 0.000236714, 0), \
                           -2674.69, 2078, 2078, -nan)
reports[-1].sigmaresid = ValErr(0.876511, 0.013596, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0057644, None, -0.00159732, None, -0.00671246, None, -0.00120972, None, -0.00671246, None, -0.00120972, None, -0.0275749, None, -0.00123747, None, -0.0275749, None, -0.00123747, None, 0.876549, None, 0.0122557, None, 0.876549, None, 0.0122557, None)
reports[-1].CovMatrix = ['0.000468183','-0.00029937','-2.348e-06','8.10341e-08','0','0','0','0','0','-0.00029937','0.267033','3.72734e-06','3.56421e-06','0','0','0','0','0','-2.348e-06','3.72734e-06','5.60333e-08','1.34735e-09','0','0','0','0','0','8.10341e-08','3.56421e-06','1.34735e-09','0.000184851','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058808, ("CSC", 2, 3, 2, 23), "MEm32_23"))
reports[-1].posNum = 2204
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00829108, 0.0201525, 0), \
                           ValErr(-0.0529993, 0.489063, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.34434e-05, 0.000225672, 0), \
                           -2816.23, 2204, 2204, -nan)
reports[-1].sigmaresid = ValErr(0.868349, 0.0130789, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.030103, None, 0.00282518, None, 0.00536598, None, 0.00298573, None, 0.00536598, None, 0.00298573, None, -0.00654052, None, 0.00319289, None, -0.00654052, None, 0.00319289, None, 0.868383, None, 0.0122687, None, 0.868383, None, 0.0122687, None)
reports[-1].CovMatrix = ['0.000406123','0.000172749','-1.80441e-06','9.86805e-08','0','0','0','0','0','0.000172749','0.239183','-1.16875e-06','3.7434e-06','0','0','0','0','0','-1.80441e-06','-1.16875e-06','5.09276e-08','1.02589e-09','0','0','0','0','0','9.86805e-08','3.7434e-06','1.02589e-09','0.000171058','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058824, ("CSC", 2, 3, 2, 25), "MEm32_25"))
reports[-1].posNum = 1869
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00708838, 0.0229739, 0), \
                           ValErr(-0.26388, 0.543134, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.133e-05, 0.000235521, 0), \
                           -2429.48, 1869, 1869, -nan)
reports[-1].sigmaresid = ValErr(0.887735, 0.0145194, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.022703, None, 0.00460438, None, 0.00275625, None, 0.00508028, None, 0.00275625, None, 0.00508028, None, 0.00617042, None, 0.00503074, None, 0.00617042, None, 0.00503074, None, 0.887843, None, 0.011841, None, 0.887843, None, 0.011841, None)
reports[-1].CovMatrix = ['0.0005278','-0.000686247','-2.42143e-06','1.24703e-07','0','0','0','0','0','-0.000686247','0.294995','7.44789e-06','5.21071e-06','0','0','0','0','0','-2.42143e-06','7.44789e-06','5.54703e-08','1.19521e-09','0','0','0','0','0','1.24703e-07','5.21071e-06','1.19521e-09','0.000210814','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058840, ("CSC", 2, 3, 2, 27), "MEm32_27"))
reports[-1].posNum = 1619
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0195304, 0.0238606, 0), \
                           ValErr(0.0272023, 0.584573, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000168283, 0.000253432, 0), \
                           -2052.45, 1619, 1619, -nan)
reports[-1].sigmaresid = ValErr(0.859661, 0.0151072, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0371599, None, 0.00427668, None, 0.0126085, None, 0.00458689, None, 0.0126085, None, 0.00458689, None, -0.0138888, None, 0.00441826, None, -0.0138888, None, 0.00441826, None, 0.859782, None, 0.010397, None, 0.859782, None, 0.010397, None)
reports[-1].CovMatrix = ['0.000569327','-0.000806401','-2.66408e-06','1.13615e-07','0','0','0','0','0','-0.000806401','0.341725','-2.20295e-06','4.15691e-06','0','0','0','0','0','-2.66408e-06','-2.20295e-06','6.42278e-08','1.24594e-09','0','0','0','0','0','1.13615e-07','4.15691e-06','1.24594e-09','0.00022823','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058856, ("CSC", 2, 3, 2, 29), "MEm32_29"))
reports[-1].posNum = 2013
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00194423, 0.0231411, 0), \
                           ValErr(0.0956856, 0.562566, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.59618e-05, 0.000240156, 0), \
                           -2722.71, 2013, 2013, -nan)
reports[-1].sigmaresid = ValErr(0.935752, 0.0147471, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0116412, None, -0.000382117, None, 0.000136194, None, -0.000630093, None, 0.000136194, None, -0.000630093, None, 0.00427211, None, -0.000537312, None, 0.00427211, None, -0.000537312, None, 0.935792, None, 0.0131105, None, 0.935792, None, 0.0131105, None)
reports[-1].CovMatrix = ['0.000535509','-0.000678412','-2.39742e-06','1.02776e-07','0','0','0','0','0','-0.000678412','0.31648','3.73855e-06','4.24243e-06','0','0','0','0','0','-2.39742e-06','3.73855e-06','5.76751e-08','1.37621e-09','0','0','0','0','0','1.02776e-07','4.24243e-06','1.37621e-09','0.000217479','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058872, ("CSC", 2, 3, 2, 31), "MEm32_31"))
reports[-1].posNum = 1250
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0117979, 0.034131, 0), \
                           ValErr(-0.112761, 0.634284, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.72565e-06, 0.000321387, 0), \
                           -1481.91, 1250, 1250, -nan)
reports[-1].sigmaresid = ValErr(0.791838, 0.0158368, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.014042, None, -0.0016909, None, 0.011304, None, -0.00161332, None, 0.011304, None, -0.00161332, None, -0.014297, None, -0.00143793, None, -0.014297, None, -0.00143793, None, 0.791842, None, 0.0125254, None, 0.791842, None, 0.0125254, None)
reports[-1].CovMatrix = ['0.00116492','0.00278296','-8.26188e-06','1.47377e-07','0','0','0','0','0','0.00278296','0.402317','-2.24037e-05','5.6224e-06','0','0','0','0','0','-8.26188e-06','-2.24037e-05','1.0329e-07','7.12177e-10','0','0','0','0','0','1.47377e-07','5.6224e-06','7.12177e-10','0.000250808','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058888, ("CSC", 2, 3, 2, 33), "MEm32_33"))
reports[-1].posNum = 1796
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000464253, 0.0244724, 0), \
                           ValErr(-0.014307, 0.565843, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.95979e-05, 0.000261781, 0), \
                           -2314.4, 1796, 1796, -nan)
reports[-1].sigmaresid = ValErr(0.877837, 0.0146469, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00679799, None, 0.00169942, None, -0.00355592, None, 0.00213422, None, -0.00355592, None, 0.00213422, None, 0.00560472, None, 0.00210332, None, 0.00560472, None, 0.00210332, None, 0.877857, None, 0.0110864, None, 0.877857, None, 0.0110864, None)
reports[-1].CovMatrix = ['0.0005989','8.87226e-05','-3.40756e-06','1.49687e-07','0','0','0','0','0','8.87226e-05','0.320178','-8.95433e-06','4.33783e-06','0','0','0','0','0','-3.40756e-06','-8.95433e-06','6.85294e-08','6.12141e-10','0','0','0','0','0','1.49687e-07','4.33783e-06','6.12141e-10','0.000214533','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058904, ("CSC", 2, 3, 2, 35), "MEm32_35"))
reports[-1].posNum = 2049
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00134062, 0.0216792, 0), \
                           ValErr(0.105415, 0.517554, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000141249, 0.00022918, 0), \
                           -2624.68, 2049, 2049, -nan)
reports[-1].sigmaresid = ValErr(0.871096, 0.0136072, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00447701, None, -0.00297385, None, -0.00477936, None, -0.00298895, None, -0.00477936, None, -0.00298895, None, 0.0406256, None, -0.00318815, None, 0.0406256, None, -0.00318815, None, 0.871204, None, 0.012022, None, 0.871204, None, 0.012022, None)
reports[-1].CovMatrix = ['0.000469989','-0.000181802','-2.28703e-06','1.1344e-07','0','0','0','0','0','-0.000181802','0.267862','9.63019e-07','3.34845e-06','0','0','0','0','0','-2.28703e-06','9.63019e-07','5.25235e-08','9.29554e-10','0','0','0','0','0','1.1344e-07','3.34845e-06','9.29554e-10','0.000185156','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058640, ("CSC", 2, 3, 2, 2), "MEm32_02"))
reports[-1].posNum = 2254
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00451842, 0.0210621, 0), \
                           ValErr(0.0459796, 0.509206, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.73105e-05, 0.000234435, 0), \
                           -3036.21, 2254, 2254, -nan)
reports[-1].sigmaresid = ValErr(0.930601, 0.0138599, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00803677, None, -0.000551024, None, 0.00364714, None, -2.57214e-05, None, 0.00364714, None, -2.57214e-05, None, 0.0310375, None, -0.000409111, None, 0.0310375, None, -0.000409111, None, 0.930624, None, 0.0110016, None, 0.930624, None, 0.0110016, None)
reports[-1].CovMatrix = ['0.00044361','-0.000134415','-1.8054e-06','1.12176e-07','0','0','0','0','0','-0.000134415','0.25929','-5.48631e-07','3.79287e-06','0','0','0','0','0','-1.8054e-06','-5.48631e-07','5.49597e-08','1.21365e-09','0','0','0','0','0','1.12176e-07','3.79287e-06','1.21365e-09','0.000192097','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058656, ("CSC", 2, 3, 2, 4), "MEm32_04"))
reports[-1].posNum = 1584
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000466641, 0.0254779, 0), \
                           ValErr(0.326112, 0.602305, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.79001e-05, 0.000277707, 0), \
                           -2071.73, 1584, 1584, -nan)
reports[-1].sigmaresid = ValErr(0.894898, 0.0158989, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0103424, None, 0.00365903, None, -0.00206729, None, 0.00374049, None, -0.00206729, None, 0.00374049, None, -0.00169169, None, 0.00359634, None, -0.00169169, None, 0.00359634, None, 0.895035, None, 0.0110407, None, 0.895035, None, 0.0110407, None)
reports[-1].CovMatrix = ['0.000649122','-0.00186494','-3.27186e-06','1.46504e-07','0','0','0','0','0','-0.00186494','0.362772','1.31724e-05','4.61623e-06','0','0','0','0','0','-3.27186e-06','1.31724e-05','7.71214e-08','1.41675e-09','0','0','0','0','0','1.46504e-07','4.61623e-06','1.41675e-09','0.000252778','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058672, ("CSC", 2, 3, 2, 6), "MEm32_06"))
reports[-1].posNum = 1938
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.025255, 0.0242319, 0), \
                           ValErr(-0.104351, 0.564233, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.82196e-05, 0.000271002, 0), \
                           -2581.06, 1938, 1938, -nan)
reports[-1].sigmaresid = ValErr(0.91656, 0.0147219, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0404575, None, -0.0016655, None, -0.0209996, None, -0.00128426, None, -0.0209996, None, -0.00128426, None, -0.0135312, None, -0.00142405, None, -0.0135312, None, -0.00142405, None, 0.916594, None, 0.0110132, None, 0.916594, None, 0.0110132, None)
reports[-1].CovMatrix = ['0.000587184','0.00157109','-3.33026e-06','1.38053e-07','0','0','0','0','0','0.00157109','0.318359','-1.43214e-05','4.92946e-06','0','0','0','0','0','-3.33026e-06','-1.43214e-05','7.34419e-08','1.08771e-09','0','0','0','0','0','1.38053e-07','4.92946e-06','1.08771e-09','0.000216738','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058688, ("CSC", 2, 3, 2, 8), "MEm32_08"))
reports[-1].posNum = 2009
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0028905, 0.0226135, 0), \
                           ValErr(0.156476, 0.527066, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000215174, 0.000251034, 0), \
                           -2597.26, 2009, 2009, -nan)
reports[-1].sigmaresid = ValErr(0.881516, 0.013907, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0161989, None, -0.00125357, None, -0.00657998, None, -0.0010864, None, -0.00657998, None, -0.0010864, None, -0.00275239, None, -0.00119267, None, -0.00275239, None, -0.00119267, None, 0.881681, None, 0.0113454, None, 0.881681, None, 0.0113454, None)
reports[-1].CovMatrix = ['0.000511368','-0.000101612','-2.8006e-06','1.05362e-07','0','0','0','0','0','-0.000101612','0.277799','-1.66495e-06','3.36747e-06','0','0','0','0','0','-2.8006e-06','-1.66495e-06','6.30179e-08','1.02708e-09','0','0','0','0','0','1.05362e-07','3.36747e-06','1.02708e-09','0.000193406','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058704, ("CSC", 2, 3, 2, 10), "MEm32_10"))
reports[-1].posNum = 2360
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00977566, 0.0205353, 0), \
                           ValErr(-0.175489, 0.274115, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00022126, 0.000232941, 0), \
                           -3201.83, 2360, 2360, -nan)
reports[-1].sigmaresid = ValErr(0.939667, 0.0136782, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00152794, None, 0.00137756, None, 0.00318567, None, 0.00179364, None, 0.00318567, None, 0.00179364, None, 0.0196615, None, 0.00142344, None, 0.0196615, None, 0.00142344, None, 0.939872, None, 0.0119312, None, 0.939872, None, 0.0119312, None)
reports[-1].CovMatrix = ['0.0004217','-4.29251e-05','-1.59525e-06','2.69079e-07','0','0','0','0','0','-4.29251e-05','0.0751389','3.95353e-06','0.000117936','0','0','0','0','0','-1.59525e-06','3.95353e-06','5.42615e-08','-3.17591e-09','0','0','0','0','0','2.69079e-07','0.000117936','-3.17591e-09','0.000187093','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058720, ("CSC", 2, 3, 2, 12), "MEm32_12"))
reports[-1].posNum = 1995
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00421467, 0.0228196, 0), \
                           ValErr(0.151217, 0.530361, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.27845e-05, 0.000260105, 0), \
                           -2563.89, 1995, 1995, -nan)
reports[-1].sigmaresid = ValErr(0.874793, 0.0138492, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0190767, None, 0.00229319, None, -0.00538857, None, 0.00241031, None, -0.00538857, None, 0.00241031, None, -0.0148864, None, 0.00236518, None, -0.0148864, None, 0.00236518, None, 0.874799, None, 0.00924026, None, 0.874799, None, 0.00924026, None)
reports[-1].CovMatrix = ['0.000520733','0.000222541','-3.04213e-06','8.70586e-08','0','0','0','0','0','0.000222541','0.281283','2.04045e-06','5.21819e-06','0','0','0','0','0','-3.04213e-06','2.04045e-06','6.76548e-08','1.33273e-09','0','0','0','0','0','8.70586e-08','5.21819e-06','1.33273e-09','0.000191803','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058736, ("CSC", 2, 3, 2, 14), "MEm32_14"))
reports[-1].posNum = 2391
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0145996, 0.0200716, 0), \
                           ValErr(-0.0505051, 0.483496, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000101001, 0.000224587, 0), \
                           -3173.94, 2391, 2391, -nan)
reports[-1].sigmaresid = ValErr(0.912555, 0.013196, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.022899, None, -0.00170757, None, 0.0112976, None, -0.00183657, None, 0.0112976, None, -0.00183657, None, -0.0169441, None, -0.00189549, None, -0.0169441, None, -0.00189549, None, 0.912614, None, 0.00999411, None, 0.912614, None, 0.00999411, None)
reports[-1].CovMatrix = ['0.000402869','0.000127648','-1.65897e-06','1.04e-07','0','0','0','0','0','0.000127648','0.233768','-1.99953e-06','3.75332e-06','0','0','0','0','0','-1.65897e-06','-1.99953e-06','5.04395e-08','1.01439e-09','0','0','0','0','0','1.04e-07','3.75332e-06','1.01439e-09','0.000174136','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058752, ("CSC", 2, 3, 2, 16), "MEm32_16"))
reports[-1].posNum = 2260
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0128075, 0.021016, 0), \
                           ValErr(0.0705878, 0.509266, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.95011e-05, 0.00023359, 0), \
                           -3004.66, 2260, 2260, -nan)
reports[-1].sigmaresid = ValErr(0.914419, 0.0136007, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0130213, None, -0.00189284, None, 0.0107168, None, -0.00161284, None, 0.0107168, None, -0.00161284, None, -0.00206618, None, -0.00164268, None, -0.00206618, None, -0.00164268, None, 0.914458, None, 0.0116452, None, 0.914458, None, 0.0116452, None)
reports[-1].CovMatrix = ['0.000441672','-3.58787e-05','-1.97433e-06','1.10029e-07','0','0','0','0','0','-3.58787e-05','0.259352','-6.04502e-06','3.54516e-06','0','0','0','0','0','-1.97433e-06','-6.04502e-06','5.45644e-08','9.35731e-10','0','0','0','0','0','1.10029e-07','3.54516e-06','9.35731e-10','0.00018498','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058768, ("CSC", 2, 3, 2, 18), "MEm32_18"))
reports[-1].posNum = 2152
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00676966, 0.0214726, 0), \
                           ValErr(0.307285, 0.514315, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.2147e-05, 0.000238186, 0), \
                           -2810.47, 2152, 2152, -nan)
reports[-1].sigmaresid = ValErr(0.893162, 0.0136137, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0271043, None, -0.0014791, None, 0.00286154, None, -0.00144671, None, 0.00286154, None, -0.00144671, None, 0.0190934, None, -0.00149364, None, 0.0190934, None, -0.00149364, None, 0.893283, None, 0.0116811, None, 0.893283, None, 0.0116811, None)
reports[-1].CovMatrix = ['0.000461071','0.000786797','-2.25057e-06','1.33803e-07','0','0','0','0','0','0.000786797','0.26452','-6.28397e-06','3.2823e-06','0','0','0','0','0','-2.25057e-06','-6.28397e-06','5.67324e-08','9.22858e-10','0','0','0','0','0','1.33803e-07','3.2823e-06','9.22858e-10','0.000185335','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058784, ("CSC", 2, 3, 2, 20), "MEm32_20"))
reports[-1].posNum = 2118
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00483183, 0.0215289, 0), \
                           ValErr(0.168846, 0.516915, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000117633, 0.000232985, 0), \
                           -2772.45, 2118, 2118, -nan)
reports[-1].sigmaresid = ValErr(0.895862, 0.0137641, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0172981, None, -0.00239082, None, 0.000147986, None, -0.00215793, None, 0.000147986, None, -0.00215793, None, 0.0375755, None, -0.00224657, None, 0.0375755, None, -0.00224657, None, 0.89596, None, 0.011009, None, 0.89596, None, 0.011009, None)
reports[-1].CovMatrix = ['0.000463493','3.03678e-05','-2.14249e-06','1.18482e-07','0','0','0','0','0','3.03678e-05','0.267201','-2.05172e-07','3.34349e-06','0','0','0','0','0','-2.14249e-06','-2.05172e-07','5.4282e-08','1.08311e-09','0','0','0','0','0','1.18482e-07','3.34349e-06','1.08311e-09','0.000189453','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058800, ("CSC", 2, 3, 2, 22), "MEm32_22"))
reports[-1].posNum = 2207
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00195334, 0.0219968, 0), \
                           ValErr(0.0191621, 0.524683, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.04489e-05, 0.000252393, 0), \
                           -2990.39, 2207, 2207, -nan)
reports[-1].sigmaresid = ValErr(0.937999, 0.0141179, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0174896, None, -0.00213513, None, -0.000158667, None, -0.0021967, None, -0.000158667, None, -0.0021967, None, 0.00562172, None, -0.00223841, None, 0.00562172, None, -0.00223841, None, 0.938033, None, 0.011188, None, 0.938033, None, 0.011188, None)
reports[-1].CovMatrix = ['0.000483861','0.000800755','-2.31612e-06','1.2124e-07','0','0','0','0','0','0.000800755','0.275292','-7.68464e-06','4.13474e-06','0','0','0','0','0','-2.31612e-06','-7.68464e-06','6.37022e-08','1.19474e-09','0','0','0','0','0','1.2124e-07','4.13474e-06','1.19474e-09','0.000199317','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058816, ("CSC", 2, 3, 2, 24), "MEm32_24"))
reports[-1].posNum = 2377
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00420119, 0.0209907, 0), \
                           ValErr(-0.288142, 0.517083, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.71546e-05, 0.000236585, 0), \
                           -3230.14, 2377, 2377, -nan)
reports[-1].sigmaresid = ValErr(0.94171, 0.0136574, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00391847, None, -0.00430436, None, 0.00442487, None, -0.00462591, None, 0.00442487, None, -0.00462591, None, 0.049356, None, -0.0049768, None, 0.049356, None, -0.0049768, None, 0.941805, None, 0.0100727, None, 0.941805, None, 0.0100727, None)
reports[-1].CovMatrix = ['0.000440607','-0.000421274','-1.9384e-06','1.17962e-07','0','0','0','0','0','-0.000421274','0.267375','2.78161e-06','4.09352e-06','0','0','0','0','0','-1.9384e-06','2.78161e-06','5.59725e-08','1.00221e-09','0','0','0','0','0','1.17962e-07','4.09352e-06','1.00221e-09','0.000186525','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058832, ("CSC", 2, 3, 2, 26), "MEm32_26"))
reports[-1].posNum = 1724
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00248267, 0.0242476, 0), \
                           ValErr(-0.0731582, 0.598967, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.43741e-05, 0.000254038, 0), \
                           -2285.67, 1724, 1724, -nan)
reports[-1].sigmaresid = ValErr(0.911068, 0.0155156, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00381496, None, 0.000148331, None, 0.00394627, None, 0.000707449, None, 0.00394627, None, 0.000707449, None, -0.011026, None, 0.000453013, None, -0.011026, None, 0.000453013, None, 0.91107, None, 0.0111321, None, 0.91107, None, 0.0111321, None)
reports[-1].CovMatrix = ['0.000587948','0.000556015','-2.61897e-06','1.23037e-07','0','0','0','0','0','0.000556015','0.358761','-7.1103e-06','4.57311e-06','0','0','0','0','0','-2.61897e-06','-7.1103e-06','6.45355e-08','1.55271e-09','0','0','0','0','0','1.23037e-07','4.57311e-06','1.55271e-09','0.000240737','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058848, ("CSC", 2, 3, 2, 28), "MEm32_28"))
reports[-1].posNum = 1996
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0100792, 0.0229254, 0), \
                           ValErr(0.192632, 0.542956, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.15222e-05, 0.000245054, 0), \
                           -2682.8, 1996, 1996, -nan)
reports[-1].sigmaresid = ValErr(0.927888, 0.0146859, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00853574, None, -0.00168367, None, 0.00830295, None, -0.0017252, None, 0.00830295, None, -0.0017252, None, 0.00275719, None, -0.00200754, None, 0.00275719, None, -0.00200754, None, 0.927919, None, 0.0101897, None, 0.927919, None, 0.0101897, None)
reports[-1].CovMatrix = ['0.000525574','0.000428942','-2.37717e-06','1.33524e-07','0','0','0','0','0','0.000428942','0.294801','-6.05446e-06','3.94141e-06','0','0','0','0','0','-2.37717e-06','-6.05446e-06','6.00514e-08','1.18478e-09','0','0','0','0','0','1.33524e-07','3.94141e-06','1.18478e-09','0.000215678','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058864, ("CSC", 2, 3, 2, 30), "MEm32_30"))
reports[-1].posNum = 1393
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0114879, 0.0300137, 0), \
                           ValErr(-0.0790944, 0.630772, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.23124e-05, 0.000300058, 0), \
                           -1732.51, 1393, 1393, -nan)
reports[-1].sigmaresid = ValErr(0.839251, 0.0158994, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0431877, None, 0.00226656, None, 0.0164323, None, 0.00273861, None, 0.0164323, None, 0.00273861, None, 0.0445926, None, 0.00269305, None, 0.0445926, None, 0.00269305, None, 0.839309, None, 0.0109247, None, 0.839309, None, 0.0109247, None)
reports[-1].CovMatrix = ['0.000900824','-0.00359535','-5.90409e-06','2.92044e-08','0','0','0','0','0','-0.00359535','0.397874','2.7867e-05','6.58273e-06','0','0','0','0','0','-5.90409e-06','2.7867e-05','9.00349e-08','1.90765e-09','0','0','0','0','0','2.92044e-08','6.58273e-06','1.90765e-09','0.000252795','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058880, ("CSC", 2, 3, 2, 32), "MEm32_32"))
reports[-1].posNum = 1715
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00335535, 0.0250928, 0), \
                           ValErr(-0.136946, 0.572067, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.17696e-05, 0.00026156, 0), \
                           -2175.7, 1715, 1715, -nan)
reports[-1].sigmaresid = ValErr(0.860452, 0.0146921, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0103035, None, 0.00126336, None, -0.002107, None, 0.00144781, None, -0.002107, None, 0.00144781, None, 0.000138419, None, 0.00121446, None, 0.000138419, None, 0.00121446, None, 0.86046, None, 0.010688, None, 0.86046, None, 0.010688, None)
reports[-1].CovMatrix = ['0.00062965','-0.000249515','-3.67944e-06','1.03666e-07','0','0','0','0','0','-0.000249515','0.327261','7.10163e-06','3.90297e-06','0','0','0','0','0','-3.67944e-06','7.10163e-06','6.84137e-08','1.02489e-09','0','0','0','0','0','1.03666e-07','3.90297e-06','1.02489e-09','0.000215859','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058896, ("CSC", 2, 3, 2, 34), "MEm32_34"))
reports[-1].posNum = 2250
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0148512, 0.0210579, 0), \
                           ValErr(0.0704757, 0.507323, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000164901, 0.000232052, 0), \
                           -3035.2, 2250, 2250, -nan)
reports[-1].sigmaresid = ValErr(0.932441, 0.0139002, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00966565, None, 0.000907084, None, 0.00951203, None, 0.0010456, None, 0.00951203, None, 0.0010456, None, 0.0180769, None, 0.000929008, None, 0.0180769, None, 0.000929008, None, 0.932538, None, 0.0101007, None, 0.932538, None, 0.0101007, None)
reports[-1].CovMatrix = ['0.000443433','2.28358e-05','-1.75212e-06','1.03008e-07','0','0','0','0','0','2.28358e-05','0.257377','-6.68841e-08','3.16017e-06','0','0','0','0','0','-1.75212e-06','-6.68841e-08','5.38483e-08','1.19754e-09','0','0','0','0','0','1.03008e-07','3.16017e-06','1.19754e-09','0.000193216','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058912, ("CSC", 2, 3, 2, 36), "MEm32_36"))
reports[-1].posNum = 2182
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0060221, 0.0223187, 0), \
                           ValErr(-0.48798, 0.528315, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.53953e-06, 0.000248509, 0), \
                           -2972.81, 2182, 2182, -nan)
reports[-1].sigmaresid = ValErr(0.945006, 0.0143042, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0243685, None, 0.000524366, None, -0.00559643, None, 0.000844616, None, -0.00559643, None, 0.000844616, None, -0.000810046, None, 0.000433714, None, -0.000810046, None, 0.000433714, None, 0.945238, None, 0.0106677, None, 0.945238, None, 0.0106677, None)
reports[-1].CovMatrix = ['0.000498123','0.000217592','-2.34241e-06','9.35815e-08','0','0','0','0','0','0.000217592','0.279117','-5.2033e-06','4.54483e-06','0','0','0','0','0','-2.34241e-06','-5.2033e-06','6.17569e-08','1.56272e-09','0','0','0','0','0','9.35815e-08','4.54483e-06','1.56272e-09','0.000204612','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062216, ("CSC", 2, 4, 1, 1), "MEm41_01"))
reports[-1].posNum = 4029
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00355735, 0.00810674, 0), \
                           ValErr(-0.0180862, 0.0917613, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000206946, 0.000212914, 0), \
                           -3039.89, 4029, 4029, -nan)
reports[-1].sigmaresid = ValErr(0.514563, 0.00573223, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00281512, None, -7.59075e-06, None, 0.00353846, None, 0.000134855, None, 0.00353846, None, 0.000134855, None, 0.0179033, None, 0.000178747, None, 0.0179033, None, 0.000178747, None, 0.514626, None, 0.0120054, None, 0.514626, None, 0.0120054, None)
reports[-1].CovMatrix = ['6.57192e-05','3.24752e-06','-5.19924e-09','1.99258e-08','0','0','0','0','0','3.24752e-06','0.00842014','2.43348e-07','2.21675e-07','0','0','0','0','0','-5.19924e-09','2.43348e-07','4.53325e-08','5.15474e-10','0','0','0','0','0','1.99258e-08','2.21675e-07','5.15474e-10','3.28585e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062232, ("CSC", 2, 4, 1, 3), "MEm41_03"))
reports[-1].posNum = 3863
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.007175, 0.00841063, 0), \
                           ValErr(-0.0469073, 0.0966134, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.5344e-06, 0.000220289, 0), \
                           -2975.04, 3863, 3863, -nan)
reports[-1].sigmaresid = ValErr(0.522668, 0.00594626, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00656576, None, 0.00148843, None, -0.00724612, None, 0.00189753, None, -0.00724612, None, 0.00189753, None, -0.00902272, None, 0.00149315, None, -0.00902272, None, 0.00149315, None, 0.522688, None, 0.0126005, None, 0.522688, None, 0.0126005, None)
reports[-1].CovMatrix = ['7.07387e-05','-1.33291e-05','-1.00515e-08','2.13018e-08','0','0','0','0','0','-1.33291e-05','0.00933414','-1.74617e-07','2.50352e-07','0','0','0','0','0','-1.00515e-08','-1.74617e-07','4.85272e-08','5.72761e-10','0','0','0','0','0','2.13018e-08','2.50352e-07','5.72761e-10','3.5358e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062248, ("CSC", 2, 4, 1, 5), "MEm41_05"))
reports[-1].posNum = 3736
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00141778, 0.00838107, 0), \
                           ValErr(0.114272, 0.0964666, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000194298, 0.000223043, 0), \
                           -2800.99, 3736, 3736, -nan)
reports[-1].sigmaresid = ValErr(0.512113, 0.00592444, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000640607, None, 0.00109793, None, -0.00171643, None, 0.00149821, None, -0.00171643, None, 0.00149821, None, 0.00350695, None, 0.00122177, None, 0.00350695, None, 0.00122177, None, 0.51226, None, 0.0116601, None, 0.51226, None, 0.0116601, None)
reports[-1].CovMatrix = ['7.02424e-05','1.29352e-05','-3.64245e-08','2.09413e-08','0','0','0','0','0','1.29352e-05','0.00930581','-1.84509e-07','2.43337e-07','0','0','0','0','0','-3.64245e-08','-1.84509e-07','4.97482e-08','5.43014e-10','0','0','0','0','0','2.09413e-08','2.43337e-07','5.43014e-10','3.50991e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062264, ("CSC", 2, 4, 1, 7), "MEm41_07"))
reports[-1].posNum = 3321
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00304629, 0.00925569, 0), \
                           ValErr(-0.02317, 0.105629, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.50722e-05, 0.000239386, 0), \
                           -2595.57, 3321, 3321, -nan)
reports[-1].sigmaresid = ValErr(0.528678, 0.00648697, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0065185, None, -0.0030545, None, -0.00287393, None, -0.00272966, None, -0.00287393, None, -0.00272966, None, -0.0232254, None, -0.00317049, None, -0.0232254, None, -0.00317049, None, 0.528691, None, 0.0133754, None, 0.528691, None, 0.0133754, None)
reports[-1].CovMatrix = ['8.56678e-05','0.00012696','-6.1633e-08','2.92979e-08','0','0','0','0','0','0.00012696','0.0111574','-1.9232e-07','3.40666e-07','0','0','0','0','0','-6.1633e-08','-1.9232e-07','5.73056e-08','6.42408e-10','0','0','0','0','0','2.92979e-08','3.40666e-07','6.42408e-10','4.20808e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062280, ("CSC", 2, 4, 1, 9), "MEm41_09"))
reports[-1].posNum = 3899
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000363167, 0.00832468, 0), \
                           ValErr(-0.0193172, 0.0933414, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000189516, 0.000218961, 0), \
                           -2980.77, 3899, 3899, -nan)
reports[-1].sigmaresid = ValErr(0.519728, 0.00588546, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00129988, None, 0.000934482, None, 0.000237634, None, 0.000916689, None, 0.000237634, None, 0.000916689, None, -0.00337389, None, 0.00111031, None, -0.00337389, None, 0.00111031, None, 0.519785, None, 0.0124343, None, 0.519785, None, 0.0124343, None)
reports[-1].CovMatrix = ['6.93003e-05','2.91768e-06','-3.1703e-08','2.14369e-08','0','0','0','0','0','2.91768e-06','0.00871261','-5.13324e-07','2.42949e-07','0','0','0','0','0','-3.1703e-08','-5.13324e-07','4.7944e-08','5.45715e-10','0','0','0','0','0','2.14369e-08','2.42949e-07','5.45715e-10','3.46387e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062296, ("CSC", 2, 4, 1, 11), "MEm41_11"))
reports[-1].posNum = 3998
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00326217, 0.00802887, 0), \
                           ValErr(0.0066132, 0.0913968, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.60619e-05, 0.000211139, 0), \
                           -2962.35, 3998, 3998, -nan)
reports[-1].sigmaresid = ValErr(0.507636, 0.00567689, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00474065, None, -0.00174038, None, 0.00327523, None, -0.00176245, None, 0.00327523, None, -0.00176245, None, -1.7435e-05, None, -0.00193667, None, -1.7435e-05, None, -0.00193667, None, 0.50765, None, 0.0119217, None, 0.50765, None, 0.0119217, None)
reports[-1].CovMatrix = ['6.44628e-05','6.00698e-06','1.07817e-08','1.94683e-08','0','0','0','0','0','6.00698e-06','0.00835337','1.96061e-07','2.21827e-07','0','0','0','0','0','1.07817e-08','1.96061e-07','4.45798e-08','5.10095e-10','0','0','0','0','0','1.94683e-08','2.21827e-07','5.10095e-10','3.22271e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062312, ("CSC", 2, 4, 1, 13), "MEm41_13"))
reports[-1].posNum = 3954
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00075746, 0.00799581, 0), \
                           ValErr(0.0294727, 0.091554, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000322796, 0.000211225, 0), \
                           -2890.6, 3954, 3954, -nan)
reports[-1].sigmaresid = ValErr(0.502645, 0.0056524, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.007992, None, -0.00217241, None, -0.000991906, None, -0.00236423, None, -0.000991906, None, -0.00236423, None, 0.00432793, None, -0.00208062, None, 0.00432793, None, -0.00208062, None, 0.502795, None, 0.0127354, None, 0.502795, None, 0.0127354, None)
reports[-1].CovMatrix = ['6.3933e-05','1.26145e-05','-2.68455e-08','1.83552e-08','0','0','0','0','0','1.26145e-05','0.00838213','8.07357e-09','2.16254e-07','0','0','0','0','0','-2.68455e-08','8.07357e-09','4.46161e-08','4.83766e-10','0','0','0','0','0','1.83552e-08','2.16254e-07','4.83766e-10','3.19497e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062328, ("CSC", 2, 4, 1, 15), "MEm41_15"))
reports[-1].posNum = 3790
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00446917, 0.0084331, 0), \
                           ValErr(0.00717229, 0.0975403, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.85583e-05, 0.000222342, 0), \
                           -2882.81, 3790, 3790, -nan)
reports[-1].sigmaresid = ValErr(0.517729, 0.00594659, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00698778, None, -0.0015081, None, 0.00453748, None, -0.00149816, None, 0.00453748, None, -0.00149816, None, -0.00349565, None, -0.00149843, None, -0.00349565, None, -0.00149843, None, 0.51773, None, 0.011368, None, 0.51773, None, 0.011368, None)
reports[-1].CovMatrix = ['7.11172e-05','-4.94006e-05','-8.5888e-08','1.89891e-08','0','0','0','0','0','-4.94006e-05','0.00951411','7.12206e-07','2.41391e-07','0','0','0','0','0','-8.5888e-08','7.12206e-07','4.94361e-08','5.57674e-10','0','0','0','0','0','1.89891e-08','2.41391e-07','5.57674e-10','3.5362e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062344, ("CSC", 2, 4, 1, 17), "MEm41_17"))
reports[-1].posNum = 2850
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00264013, 0.0100749, 0), \
                           ValErr(-0.0413396, 0.113235, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000254142, 0.000251087, 0), \
                           -2145.3, 2850, 2850, -nan)
reports[-1].sigmaresid = ValErr(0.513656, 0.00680352, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00766089, None, 0.00170471, None, -0.00385774, None, 0.00167895, None, -0.00385774, None, 0.00167895, None, 0.00358033, None, 0.00166665, None, 0.00358033, None, 0.00166665, None, 0.513759, None, 0.0110507, None, 0.513759, None, 0.0110507, None)
reports[-1].CovMatrix = ['0.000101503','-0.000338021','-3.83554e-08','2.09688e-08','0','0','0','0','0','-0.000338021','0.0128221','2.49675e-07','2.43122e-07','0','0','0','0','0','-3.83554e-08','2.49675e-07','6.30445e-08','7.18649e-10','0','0','0','0','0','2.09688e-08','2.43122e-07','7.18649e-10','4.62881e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062224, ("CSC", 2, 4, 1, 2), "MEm41_02"))
reports[-1].posNum = 3871
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00231848, 0.00854211, 0), \
                           ValErr(0.00555403, 0.097788, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.48275e-05, 0.000224681, 0), \
                           -3044.01, 3871, 3871, -nan)
reports[-1].sigmaresid = ValErr(0.53122, 0.00603733, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00870453, None, 0.00031723, None, -0.00229541, None, 0.000589776, None, -0.00229541, None, 0.000589776, None, -0.00413466, None, 0.000374728, None, -0.00413466, None, 0.000374728, None, 0.531223, None, 0.0107352, None, 0.531223, None, 0.0107352, None)
reports[-1].CovMatrix = ['7.29676e-05','-2.24852e-05','2.70249e-08','2.17124e-08','0','0','0','0','0','-2.24852e-05','0.0095625','2.55441e-07','2.59755e-07','0','0','0','0','0','2.70249e-08','2.55441e-07','5.04815e-08','5.87967e-10','0','0','0','0','0','2.17124e-08','2.59755e-07','5.87967e-10','3.64494e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062240, ("CSC", 2, 4, 1, 4), "MEm41_04"))
reports[-1].posNum = 3636
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00754313, 0.00882764, 0), \
                           ValErr(0.0402047, 0.101584, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.7331e-06, 0.000232992, 0), \
                           -2865.63, 3636, 3636, -nan)
reports[-1].sigmaresid = ValErr(0.53216, 0.00624044, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0103262, None, 0.000162305, None, 0.00746372, None, 0.000344779, None, 0.00746372, None, 0.000344779, None, 0.00963714, None, 0.000382534, None, 0.00963714, None, 0.000382534, None, 0.532171, None, 0.0112717, None, 0.532171, None, 0.0112717, None)
reports[-1].CovMatrix = ['7.79272e-05','2.04837e-05','5.46095e-09','2.4505e-08','0','0','0','0','0','2.04837e-05','0.0103193','3.92632e-07','2.85723e-07','0','0','0','0','0','5.46095e-09','3.92632e-07','5.42852e-08','6.4323e-10','0','0','0','0','0','2.4505e-08','2.85723e-07','6.4323e-10','3.89432e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062256, ("CSC", 2, 4, 1, 6), "MEm41_06"))
reports[-1].posNum = 3929
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00349433, 0.00843399, 0), \
                           ValErr(0.0106808, 0.096321, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000194897, 0.000219601, 0), \
                           -3069.94, 3929, 3929, -nan)
reports[-1].sigmaresid = ValErr(0.528568, 0.00596272, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00607726, None, 0.00151241, None, 0.00349557, None, 0.00164635, None, 0.00349557, None, 0.00164635, None, -0.0022151, None, 0.00160147, None, -0.0022151, None, 0.00160147, None, 0.528621, None, 0.0107899, None, 0.528621, None, 0.0107899, None)
reports[-1].CovMatrix = ['7.11322e-05','1.48038e-05','3.97373e-09','2.21757e-08','0','0','0','0','0','1.48038e-05','0.00927773','-3.89727e-07','2.48053e-07','0','0','0','0','0','3.97373e-09','-3.89727e-07','4.82244e-08','5.55029e-10','0','0','0','0','0','2.21757e-08','2.48053e-07','5.55029e-10','3.55541e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062272, ("CSC", 2, 4, 1, 8), "MEm41_08"))
reports[-1].posNum = 3779
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00986656, 0.00886109, 0), \
                           ValErr(-0.118735, 0.100934, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.59265e-05, 0.000230718, 0), \
                           -3063.26, 3779, 3779, -nan)
reports[-1].sigmaresid = ValErr(0.544256, 0.00626038, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00318112, None, 0.000190205, None, 0.00978314, None, 0.000440709, None, 0.00978314, None, 0.000440709, None, -4.53509e-05, None, 0.000308913, None, -4.53509e-05, None, 0.000308913, None, 0.544362, None, 0.010576, None, 0.544362, None, 0.010576, None)
reports[-1].CovMatrix = ['7.85189e-05','2.50338e-06','-8.42626e-08','2.3615e-08','0','0','0','0','0','2.50338e-06','0.0101877','4.80523e-07','2.85793e-07','0','0','0','0','0','-8.42626e-08','4.80523e-07','5.32307e-08','6.20975e-10','0','0','0','0','0','2.3615e-08','2.85793e-07','6.20975e-10','3.91924e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062288, ("CSC", 2, 4, 1, 10), "MEm41_10"))
reports[-1].posNum = 4067
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000334716, 0.00830559, 0), \
                           ValErr(-0.0857747, 0.095916, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.61553e-05, 0.000218517, 0), \
                           -3185.12, 4067, 4067, -nan)
reports[-1].sigmaresid = ValErr(0.529525, 0.0058713, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00177326, None, -0.00228223, None, -0.000181059, None, -0.00246667, None, -0.000181059, None, -0.00246667, None, -0.0158801, None, -0.00240661, None, -0.0158801, None, -0.00240661, None, 0.529577, None, 0.0110727, None, 0.529577, None, 0.0110727, None)
reports[-1].CovMatrix = ['6.89829e-05','1.54284e-05','-2.4058e-08','2.1174e-08','0','0','0','0','0','1.54284e-05','0.00919988','2.80393e-07','2.50773e-07','0','0','0','0','0','-2.4058e-08','2.80393e-07','4.77496e-08','5.54238e-10','0','0','0','0','0','2.1174e-08','2.50773e-07','5.54238e-10','3.44723e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062304, ("CSC", 2, 4, 1, 12), "MEm41_12"))
reports[-1].posNum = 4139
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00638831, 0.00841715, 0), \
                           ValErr(-0.0503632, 0.0969632, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.94854e-05, 0.000224087, 0), \
                           -3333.48, 4139, 4139, -nan)
reports[-1].sigmaresid = ValErr(0.541423, 0.0059508, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00191124, None, 0.00338169, None, 0.00630604, None, 0.00321172, None, 0.00630604, None, 0.00321172, None, 0.0172857, None, 0.00326786, None, 0.0172857, None, 0.00326786, None, 0.541442, None, 0.00989599, None, 0.541442, None, 0.00989599, None)
reports[-1].CovMatrix = ['7.08483e-05','-1.21588e-05','-2.12415e-08','2.14395e-08','0','0','0','0','0','-1.21588e-05','0.00940186','3.05948e-08','2.48534e-07','0','0','0','0','0','-2.12415e-08','3.05948e-08','5.02148e-08','5.76797e-10','0','0','0','0','0','2.14395e-08','2.48534e-07','5.76797e-10','3.54121e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062320, ("CSC", 2, 4, 1, 14), "MEm41_14"))
reports[-1].posNum = 4028
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00153672, 0.00828522, 0), \
                           ValErr(-0.0512509, 0.0949149, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.49094e-05, 0.000218736, 0), \
                           -3122.9, 4028, 4028, -nan)
reports[-1].sigmaresid = ValErr(0.525374, 0.00585338, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00184993, None, 0.00275522, None, -0.00142287, None, 0.00303839, None, -0.00142287, None, 0.00303839, None, -0.00937123, None, 0.00303814, None, -0.00937123, None, 0.00303814, None, 0.525396, None, 0.0106004, None, 0.525396, None, 0.0106004, None)
reports[-1].CovMatrix = ['6.86448e-05','2.04324e-05','-5.76998e-08','1.92905e-08','0','0','0','0','0','2.04324e-05','0.00900883','7.06081e-07','2.52064e-07','0','0','0','0','0','-5.76998e-08','7.06081e-07','4.78456e-08','5.17347e-10','0','0','0','0','0','1.92905e-08','2.52064e-07','5.17347e-10','3.42621e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062336, ("CSC", 2, 4, 1, 16), "MEm41_16"))
reports[-1].posNum = 3893
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00873882, 0.00862561, 0), \
                           ValErr(-0.0585746, 0.0983173, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000106234, 0.000227211, 0), \
                           -3111.92, 3893, 3893, -nan)
reports[-1].sigmaresid = ValErr(0.538167, 0.00609891, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00660704, None, 0.00326262, None, -0.00876237, None, 0.00354996, None, -0.00876237, None, 0.00354996, None, 0.00851067, None, 0.00309528, None, 0.00851067, None, 0.00309528, None, 0.538213, None, 0.0123115, None, 0.538213, None, 0.0123115, None)
reports[-1].CovMatrix = ['7.44012e-05','2.35853e-07','-1.6501e-08','2.13937e-08','0','0','0','0','0','2.35853e-07','0.00966629','-1.3095e-07','2.51095e-07','0','0','0','0','0','-1.6501e-08','-1.3095e-07','5.16247e-08','6.1363e-10','0','0','0','0','0','2.13937e-08','2.51095e-07','6.1363e-10','3.71968e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062352, ("CSC", 2, 4, 1, 18), "MEm41_18"))
reports[-1].posNum = 3829
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.004781, 0.00868903, 0), \
                           ValErr(-0.0794073, 0.0995169, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.55721e-05, 0.000225545, 0), \
                           -3057.09, 3829, 3829, -nan)
reports[-1].sigmaresid = ValErr(0.537653, 0.00614382, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00654013, None, 0.00165799, None, 0.0048155, None, 0.00184929, None, 0.0048155, None, 0.00184929, None, 0.016075, None, 0.00187752, None, 0.016075, None, 0.00187752, None, 0.537708, None, 0.0106363, None, 0.537708, None, 0.0106363, None)
reports[-1].CovMatrix = ['7.54993e-05','2.53057e-06','1.35528e-08','2.37962e-08','0','0','0','0','0','2.53057e-06','0.00990361','2.03203e-07','2.52471e-07','0','0','0','0','0','1.35528e-08','2.03203e-07','5.08708e-08','5.88223e-10','0','0','0','0','0','2.37962e-08','2.52471e-07','5.88223e-10','3.77467e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062728, ("CSC", 2, 4, 2, 1), "MEm42_01"))
reports[-1].posNum = 2232
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00976356, 0.0227221, 0), \
                           ValErr(0.208572, 0.56056, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000161367, 0.000259621, 0), \
                           -3152.18, 2232, 2232, -nan)
reports[-1].sigmaresid = ValErr(0.993344, 0.0148673, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00658871, None, 6.70594e-06, None, -0.0153466, None, 0.000235017, None, -0.0153466, None, 0.000235017, None, -0.0421819, None, 0.000186052, None, -0.0421819, None, 0.000186052, None, 0.993464, None, 0.0121777, None, 0.993464, None, 0.0121777, None)
reports[-1].CovMatrix = ['0.000516295','0.000492466','-2.23063e-06','1.51888e-07','0','0','0','0','0','0.000492466','0.314228','-4.29736e-06','4.3653e-06','0','0','0','0','0','-2.23063e-06','-4.29736e-06','6.74029e-08','1.32685e-09','0','0','0','0','0','1.51888e-07','4.3653e-06','1.32685e-09','0.000221039','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062744, ("CSC", 2, 4, 2, 3), "MEm42_03"))
reports[-1].posNum = 2046
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00402449, 0.021897, 0), \
                           ValErr(0.0780715, 0.533476, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.57777e-05, 0.000250224, 0), \
                           -2712.44, 2046, 2046, -nan)
reports[-1].sigmaresid = ValErr(0.910987, 0.0142408, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000859116, None, 0.000366437, None, 0.00142355, None, 0.000515293, None, 0.00142355, None, 0.000515293, None, 0.00854366, None, 5.05649e-05, None, 0.00854366, None, 5.05649e-05, None, 0.911026, None, 0.0115136, None, 0.911026, None, 0.0115136, None)
reports[-1].CovMatrix = ['0.000479477','-0.000121311','-2.15035e-06','1.1863e-07','0','0','0','0','0','-0.000121311','0.284597','2.38099e-06','4.00353e-06','0','0','0','0','0','-2.15035e-06','2.38099e-06','6.26121e-08','1.34738e-09','0','0','0','0','0','1.1863e-07','4.00353e-06','1.34738e-09','0.000202803','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062760, ("CSC", 2, 4, 2, 5), "MEm42_05"))
reports[-1].posNum = 1947
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0111648, 0.025712, 0), \
                           ValErr(0.0944156, 0.578792, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000218755, 0.000287164, 0), \
                           -2618.6, 1947, 1947, -nan)
reports[-1].sigmaresid = ValErr(0.928676, 0.0148822, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00131347, None, -0.000271783, None, -2.3853e-05, None, 0.000108081, None, -2.3853e-05, None, 0.000108081, None, 0.00301402, None, -0.000416598, None, 0.00301402, None, -0.000416598, None, 0.928818, None, 0.00957868, None, 0.928818, None, 0.00957868, None)
reports[-1].CovMatrix = ['0.000661108','-0.000282464','-4.23972e-06','1.2457e-07','0','0','0','0','0','-0.000282464','0.335001','8.29346e-07','4.10186e-06','0','0','0','0','0','-4.23972e-06','8.29346e-07','8.24634e-08','1.069e-09','0','0','0','0','0','1.2457e-07','4.10186e-06','1.069e-09','0.000221481','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062776, ("CSC", 2, 4, 2, 7), "MEm42_07"))
reports[-1].posNum = 2232
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00789122, 0.0230775, 0), \
                           ValErr(0.280152, 0.562599, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.51202e-05, 0.000263872, 0), \
                           -3120.77, 2232, 2232, -nan)
reports[-1].sigmaresid = ValErr(0.979475, 0.01466, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0156515, None, -0.00212982, None, -0.00820289, None, -0.00159934, None, -0.00820289, None, -0.00159934, None, -0.0185377, None, -0.00201385, None, -0.0185377, None, -0.00201385, None, 0.979525, None, 0.0133543, None, 0.979525, None, 0.0133543, None)
reports[-1].CovMatrix = ['0.000532572','-0.000544037','-2.67171e-06','9.9775e-08','0','0','0','0','0','-0.000544037','0.316517','7.14764e-06','4.15209e-06','0','0','0','0','0','-2.67171e-06','7.14764e-06','6.96282e-08','1.56277e-09','0','0','0','0','0','9.9775e-08','4.15209e-06','1.56277e-09','0.000214916','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062792, ("CSC", 2, 4, 2, 9), "MEm42_09"))
reports[-1].posNum = 2082
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0113982, 0.0238103, 0), \
                           ValErr(-0.0120502, 0.568524, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.89129e-05, 0.000274177, 0), \
                           -2888.83, 2082, 2082, -nan)
reports[-1].sigmaresid = ValErr(0.969063, 0.0150172, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00183503, None, -0.000422115, None, 0.0106765, None, -8.98585e-05, None, 0.0106765, None, -8.98585e-05, None, 0.0332422, None, -0.000207543, None, 0.0332422, None, -0.000207543, None, 0.969077, None, 0.0132601, None, 0.969077, None, 0.0132601, None)
reports[-1].CovMatrix = ['0.00056693','0.000588812','-2.94573e-06','1.35383e-07','0','0','0','0','0','0.000588812','0.32322','-5.29496e-06','5.16831e-06','0','0','0','0','0','-2.94573e-06','-5.29496e-06','7.51732e-08','1.33879e-09','0','0','0','0','0','1.35383e-07','5.16831e-06','1.33879e-09','0.000225517','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062808, ("CSC", 2, 4, 2, 11), "MEm42_11"))
reports[-1].posNum = 2148
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0333035, 0.0224169, 0), \
                           ValErr(0.0530811, 0.552229, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000289943, 0.000258333, 0), \
                           -2967.77, 2148, 2148, -nan)
reports[-1].sigmaresid = ValErr(0.963379, 0.0146979, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0459706, None, -0.00160028, None, 0.0238729, None, -0.000985192, None, 0.0238729, None, -0.000985192, None, 0.0166859, None, -0.00116189, None, 0.0166859, None, -0.00116189, None, 0.963675, None, 0.0129594, None, 0.963675, None, 0.0129594, None)
reports[-1].CovMatrix = ['0.000502517','3.83723e-05','-2.16793e-06','1.35216e-07','0','0','0','0','0','3.83723e-05','0.304957','9.40351e-07','4.43715e-06','0','0','0','0','0','-2.16793e-06','9.40351e-07','6.67358e-08','1.24869e-09','0','0','0','0','0','1.35216e-07','4.43715e-06','1.24869e-09','0.000216031','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062824, ("CSC", 2, 4, 2, 13), "MEm42_13"))
reports[-1].posNum = 2022
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00030889, 0.0223548, 0), \
                           ValErr(-0.0946709, 0.550132, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.67966e-05, 0.000253819, 0), \
                           -2738.48, 2022, 2022, -nan)
reports[-1].sigmaresid = ValErr(0.937422, 0.0147405, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0148596, None, -0.000296009, None, 0.00199652, None, 0.000393603, None, 0.00199652, None, 0.000393603, None, 0.0399177, None, 2.92517e-06, None, 0.0399177, None, 2.92517e-06, None, 0.937462, None, 0.0111913, None, 0.937462, None, 0.0111913, None)
reports[-1].CovMatrix = ['0.000499738','0.000844092','-2.0254e-06','1.31816e-07','0','0','0','0','0','0.000844092','0.302645','-5.70754e-06','4.87508e-06','0','0','0','0','0','-2.0254e-06','-5.70754e-06','6.44243e-08','1.45363e-09','0','0','0','0','0','1.31816e-07','4.87508e-06','1.45363e-09','0.000217285','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062840, ("CSC", 2, 4, 2, 15), "MEm42_15"))
reports[-1].posNum = 2241
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0260782, 0.0219844, 0), \
                           ValErr(0.376271, 0.542763, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000264433, 0.000256102, 0), \
                           -3171.69, 2241, 2241, -nan)
reports[-1].sigmaresid = ValErr(0.996359, 0.0148824, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0252896, None, -0.000294751, None, 0.0191934, None, 4.29549e-05, None, 0.0191934, None, 4.29549e-05, None, 0.0140428, None, -0.000358459, None, 0.0140428, None, -0.000358459, None, 0.996702, None, 0.0114155, None, 0.996702, None, 0.0114155, None)
reports[-1].CovMatrix = ['0.000483314','0.000438582','-1.62031e-06','1.4637e-07','0','0','0','0','0','0.000438582','0.294592','-5.74372e-06','4.33886e-06','0','0','0','0','0','-1.62031e-06','-5.74372e-06','6.55881e-08','1.54361e-09','0','0','0','0','0','1.4637e-07','4.33886e-06','1.54361e-09','0.000221486','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062856, ("CSC", 2, 4, 2, 17), "MEm42_17"))
reports[-1].posNum = 1950
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00864536, 0.0231485, 0), \
                           ValErr(-0.108613, 0.545255, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000163993, 0.000254687, 0), \
                           -2562.86, 1950, 1950, -nan)
reports[-1].sigmaresid = ValErr(0.900615, 0.0144209, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00928757, None, -0.000549494, None, 0.00148951, None, -0.000613379, None, 0.00148951, None, -0.000613379, None, 0.0139927, None, -0.00036148, None, 0.0139927, None, -0.00036148, None, 0.900743, None, 0.0116707, None, 0.900743, None, 0.0116707, None)
reports[-1].CovMatrix = ['0.000535855','-0.000157143','-2.78686e-06','1.21232e-07','0','0','0','0','0','-0.000157143','0.297303','-1.5651e-06','4.9198e-06','0','0','0','0','0','-2.78686e-06','-1.5651e-06','6.48656e-08','1.19139e-09','0','0','0','0','0','1.21232e-07','4.9198e-06','1.19139e-09','0.000207963','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062872, ("CSC", 2, 4, 2, 19), "MEm42_19"))
reports[-1].posNum = 2012
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000275969, 0.0223574, 0), \
                           ValErr(-0.0917283, 0.55164, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.02226e-06, 0.000248354, 0), \
                           -2715.98, 2012, 2012, -nan)
reports[-1].sigmaresid = ValErr(0.933288, 0.0147126, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00383298, None, 0.00147671, None, -0.000216063, None, 0.00162028, None, -0.000216063, None, 0.00162028, None, 0.0115952, None, 0.00169043, None, 0.0115952, None, 0.00169043, None, 0.933286, None, 0.0113605, None, 0.933286, None, 0.0113605, None)
reports[-1].CovMatrix = ['0.000499853','-0.00121605','-1.96498e-06','1.32248e-07','0','0','0','0','0','-0.00121605','0.304306','2.11395e-06','3.47658e-06','0','0','0','0','0','-1.96498e-06','2.11395e-06','6.16799e-08','1.15244e-09','0','0','0','0','0','1.32248e-07','3.47658e-06','1.15244e-09','0.000216463','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062888, ("CSC", 2, 4, 2, 21), "MEm42_21"))
reports[-1].posNum = 2137
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00360879, 0.0221057, 0), \
                           ValErr(-0.0775551, 0.297944, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000138568, 0.000251203, 0), \
                           -2876.41, 2137, 2137, -nan)
reports[-1].sigmaresid = ValErr(0.92966, 0.0142129, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0202007, None, -0.000251248, None, -0.00149609, None, -1.04955e-06, None, -0.00149609, None, -1.04955e-06, None, -0.0396301, None, -0.000243137, None, -0.0396301, None, -0.000243137, None, 0.929731, None, 0.0113321, None, 0.929731, None, 0.0113321, None)
reports[-1].CovMatrix = ['0.000488662','-0.000755796','-2.29796e-06','-3.55141e-07','0','0','0','0','0','-0.000755796','0.0887709','1.2438e-05','-0.00023729','0','0','0','0','0','-2.29796e-06','1.2438e-05','6.31029e-08','1.15913e-08','0','0','0','0','0','-3.55141e-07','-0.00023729','1.15913e-08','0.000202007','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062904, ("CSC", 2, 4, 2, 23), "MEm42_23"))
reports[-1].posNum = 2271
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00408866, 0.0213727, 0), \
                           ValErr(-0.104647, 0.522216, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.99883e-05, 0.000241041, 0), \
                           -3099.45, 2271, 2271, -nan)
reports[-1].sigmaresid = ValErr(0.947289, 0.0140557, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0317806, None, -0.00147143, None, -0.00298976, None, -0.00117317, None, -0.00298976, None, -0.00117317, None, 0.0105499, None, -0.00121598, None, 0.0105499, None, -0.00121598, None, 0.947307, None, 0.0115141, None, 0.947307, None, 0.0115141, None)
reports[-1].CovMatrix = ['0.000456793','0.00045674','-1.88636e-06','1.22239e-07','0','0','0','0','0','0.00045674','0.27271','-3.76303e-06','4.51031e-06','0','0','0','0','0','-1.88636e-06','-3.76303e-06','5.8101e-08','1.3255e-09','0','0','0','0','0','1.22239e-07','4.51031e-06','1.3255e-09','0.000197565','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062920, ("CSC", 2, 4, 2, 25), "MEm42_25"))
reports[-1].posNum = 1948
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00113662, 0.0243418, 0), \
                           ValErr(0.37143, 0.571238, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000117216, 0.000263897, 0), \
                           -2634.79, 1948, 1948, -nan)
reports[-1].sigmaresid = ValErr(0.935778, 0.0149921, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0462195, None, 0.000599275, None, 0.00431575, None, 0.000941289, None, 0.00431575, None, 0.000941289, None, -0.01051, None, 0.000702211, None, -0.01051, None, 0.000702211, None, 0.935919, None, 0.0124397, None, 0.935919, None, 0.0124397, None)
reports[-1].CovMatrix = ['0.000592525','-0.000485012','-3.15515e-06','1.13507e-07','0','0','0','0','0','-0.000485012','0.326312','7.85527e-06','4.97169e-06','0','0','0','0','0','-3.15515e-06','7.85527e-06','6.96416e-08','1.43756e-09','0','0','0','0','0','1.13507e-07','4.97169e-06','1.43756e-09','0.000224765','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062936, ("CSC", 2, 4, 2, 27), "MEm42_27"))
reports[-1].posNum = 1332
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0128152, 0.0288698, 0), \
                           ValErr(-0.216879, 0.611172, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000153859, 0.000313169, 0), \
                           -1783.61, 1332, 1332, -nan)
reports[-1].sigmaresid = ValErr(0.923185, 0.0178855, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0389683, None, -0.00212203, None, 0.00547875, None, -0.00231348, None, 0.00547875, None, -0.00231348, None, -0.0059301, None, -0.00168714, None, -0.0059301, None, -0.00168714, None, 0.923339, None, 0.0125723, None, 0.923339, None, 0.0125723, None)
reports[-1].CovMatrix = ['0.000833467','-0.00135179','-4.33093e-06','1.77426e-07','0','0','0','0','0','-0.00135179','0.373531','9.32285e-06','7.29056e-06','0','0','0','0','0','-4.33093e-06','9.32285e-06','9.80746e-08','1.86167e-09','0','0','0','0','0','1.77426e-07','7.29056e-06','1.86167e-09','0.000319894','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062952, ("CSC", 2, 4, 2, 29), "MEm42_29"))
reports[-1].posNum = 2016
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00155369, 0.0246819, 0), \
                           ValErr(-0.211223, 0.587605, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.24664e-07, 0.00026897, 0), \
                           -2806.05, 2016, 2016, -nan)
reports[-1].sigmaresid = ValErr(0.973309, 0.015328, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0129236, None, -0.000412894, None, -0.00158284, None, -7.94683e-05, None, -0.00158284, None, -7.94683e-05, None, 0.00378226, None, -0.000564232, None, 0.00378226, None, -0.000564232, None, 0.973343, None, 0.011033, None, 0.973343, None, 0.011033, None)
reports[-1].CovMatrix = ['0.000609198','-0.000220472','-3.17438e-06','1.1558e-07','0','0','0','0','0','-0.000220472','0.34528','3.98774e-06','5.29936e-06','0','0','0','0','0','-3.17438e-06','3.98774e-06','7.23451e-08','1.61573e-09','0','0','0','0','0','1.1558e-07','5.29936e-06','1.61573e-09','0.000234951','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062968, ("CSC", 2, 4, 2, 31), "MEm42_31"))
reports[-1].posNum = 1507
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0114252, 0.0321146, 0), \
                           ValErr(-0.108943, 0.619949, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000128372, 0.00033391, 0), \
                           -1910.43, 1507, 1507, -nan)
reports[-1].sigmaresid = ValErr(0.859649, 0.0156585, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00210075, None, -0.000817751, None, 0.00248376, None, -0.000466336, None, 0.00248376, None, -0.000466336, None, -0.0146239, None, -0.000513403, None, -0.0146239, None, -0.000513403, None, 0.859699, None, 0.00950898, None, 0.859699, None, 0.00950898, None)
reports[-1].CovMatrix = ['0.00103135','0.000956667','-7.76631e-06','1.25672e-07','0','0','0','0','0','0.000956667','0.384337','-1.44181e-05','5.33715e-06','0','0','0','0','0','-7.76631e-06','-1.44181e-05','1.11496e-07','7.90367e-10','0','0','0','0','0','1.25672e-07','5.33715e-06','7.90367e-10','0.00024519','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062984, ("CSC", 2, 4, 2, 33), "MEm42_33"))
reports[-1].posNum = 1995
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0056965, 0.0242748, 0), \
                           ValErr(-0.21782, 0.580753, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000146364, 0.000273929, 0), \
                           -2708.21, 1995, 1995, -nan)
reports[-1].sigmaresid = ValErr(0.940409, 0.0148878, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0255, None, -0.001598, None, 0.000487856, None, -0.00103677, None, 0.000487856, None, -0.00103677, None, -0.00412316, None, -0.00127386, None, -0.00412316, None, -0.00127386, None, 0.940506, None, 0.0117368, None, 0.940506, None, 0.0117368, None)
reports[-1].CovMatrix = ['0.000589266','-0.000212818','-3.30369e-06','1.16376e-07','0','0','0','0','0','-0.000212818','0.337274','-4.66981e-06','4.66583e-06','0','0','0','0','0','-3.30369e-06','-4.66981e-06','7.50371e-08','1.27613e-09','0','0','0','0','0','1.16376e-07','4.66583e-06','1.27613e-09','0.000221647','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604063000, ("CSC", 2, 4, 2, 35), "MEm42_35"))
reports[-1].posNum = 2091
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0171967, 0.0231702, 0), \
                           ValErr(0.0200857, 0.552931, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000187258, 0.000260148, 0), \
                           -2850.96, 2091, 2091, -nan)
reports[-1].sigmaresid = ValErr(0.946014, 0.0146286, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000828528, None, -0.00100886, None, 0.00969801, None, -0.000710876, None, 0.00969801, None, -0.000710876, None, 0.0147938, None, -0.000875203, None, 0.0147938, None, -0.000875203, None, 0.946134, None, 0.0103581, None, 0.946134, None, 0.0103581, None)
reports[-1].CovMatrix = ['0.000536857','-0.000229417','-2.71381e-06','1.17763e-07','0','0','0','0','0','-0.000229417','0.305733','3.0996e-06','4.3352e-06','0','0','0','0','0','-2.71381e-06','3.0996e-06','6.76771e-08','1.3225e-09','0','0','0','0','0','1.17763e-07','4.3352e-06','1.3225e-09','0.000213998','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062736, ("CSC", 2, 4, 2, 2), "MEm42_02"))
reports[-1].posNum = 2299
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00733481, 0.0219912, 0), \
                           ValErr(-0.412753, 0.532081, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000223695, 0.00024999, 0), \
                           -3223.41, 2299, 2299, -nan)
reports[-1].sigmaresid = ValErr(0.983281, 0.0145005, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0163501, None, -0.00259823, None, -0.000336498, None, -0.00218842, None, -0.000336498, None, -0.00218842, None, -0.0116411, None, -0.00268022, None, -0.0116411, None, -0.00268022, None, 0.983595, None, 0.0100641, None, 0.983595, None, 0.0100641, None)
reports[-1].CovMatrix = ['0.000483612','-0.000429153','-1.97546e-06','1.16417e-07','0','0','0','0','0','-0.000429153','0.28311','3.36617e-07','5.08703e-06','0','0','0','0','0','-1.97546e-06','3.36617e-07','6.2495e-08','1.40565e-09','0','0','0','0','0','1.16417e-07','5.08703e-06','1.40565e-09','0.000210267','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062752, ("CSC", 2, 4, 2, 4), "MEm42_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062768, ("CSC", 2, 4, 2, 6), "MEm42_06"))
reports[-1].posNum = 2218
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00337179, 0.0233653, 0), \
                           ValErr(-0.176663, 0.565354, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000127254, 0.000263741, 0), \
                           -3144.54, 2218, 2218, -nan)
reports[-1].sigmaresid = ValErr(0.998762, 0.0149949, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00346435, None, -0.00348203, None, 0.00154657, None, -0.00263182, None, 0.00154657, None, -0.00263182, None, -0.00263007, None, -0.00315402, None, -0.00263007, None, -0.00315402, None, 0.998868, None, 0.0115231, None, 0.998868, None, 0.0115231, None)
reports[-1].CovMatrix = ['0.000545939','0.000575919','-2.58271e-06','1.22213e-07','0','0','0','0','0','0.000575919','0.319626','-7.13209e-06','5.60853e-06','0','0','0','0','0','-2.58271e-06','-7.13209e-06','6.95595e-08','1.42626e-09','0','0','0','0','0','1.22213e-07','5.60853e-06','1.42626e-09','0.00022485','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062784, ("CSC", 2, 4, 2, 8), "MEm42_08"))
reports[-1].posNum = 2141
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0178837, 0.0227326, 0), \
                           ValErr(-0.323413, 0.538008, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000300746, 0.000259803, 0), \
                           -2884.77, 2141, 2141, -nan)
reports[-1].sigmaresid = ValErr(0.930955, 0.0142313, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0166451, None, -0.00226886, None, 0.00570141, None, -0.0016018, None, 0.00570141, None, -0.0016018, None, 0.00190215, None, -0.00187677, None, 0.00190215, None, -0.00187677, None, 0.931333, None, 0.00888801, None, 0.931333, None, 0.00888801, None)
reports[-1].CovMatrix = ['0.00051677','0.00018167','-2.73874e-06','4.47141e-07','0','0','0','0','0','0.00018167','0.289453','-3.94752e-06','2.2451e-06','0','0','0','0','0','-2.73874e-06','-3.94752e-06','6.74977e-08','-1.83928e-10','0','0','0','0','0','4.47141e-07','2.2451e-06','-1.83928e-10','0.000202531','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062800, ("CSC", 2, 4, 2, 10), "MEm42_10"))
reports[-1].posNum = 2331
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00502945, 0.0215964, 0), \
                           ValErr(-0.0711326, 0.530991, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.14988e-05, 0.000248798, 0), \
                           -3297.94, 2331, 2331, -nan)
reports[-1].sigmaresid = ValErr(0.99588, 0.0145853, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00880627, None, -0.000387727, None, -0.0047141, None, 0.00011951, None, -0.0047141, None, 0.00011951, None, 0.00616453, None, -9.82183e-05, None, 0.00616453, None, -9.82183e-05, None, 0.995892, None, 0.0107972, None, 0.995892, None, 0.0107972, None)
reports[-1].CovMatrix = ['0.000466402','0.000207779','-1.59124e-06','1.37362e-07','0','0','0','0','0','0.000207779','0.281952','-4.82004e-06','4.53361e-06','0','0','0','0','0','-1.59124e-06','-4.82004e-06','6.19006e-08','1.5227e-09','0','0','0','0','0','1.37362e-07','4.53361e-06','1.5227e-09','0.000212732','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062816, ("CSC", 2, 4, 2, 12), "MEm42_12"))
reports[-1].posNum = 2206
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000239494, 0.0213153, 0), \
                           ValErr(-0.408379, 0.516085, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.07726e-05, 0.000245626, 0), \
                           -2947.98, 2206, 2206, -nan)
reports[-1].sigmaresid = ValErr(0.920708, 0.013861, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0408463, None, 2.13884e-05, None, -0.000967443, None, 0.000265355, None, -0.000967443, None, 0.000265355, None, 0.00765232, None, -2.7091e-05, None, 0.00765232, None, -2.7091e-05, None, 0.920856, None, 0.0105905, None, 0.920856, None, 0.0105905, None)
reports[-1].CovMatrix = ['0.000454341','-0.000153731','-2.05605e-06','1.27781e-07','0','0','0','0','0','-0.000153731','0.266344','4.84501e-06','4.14091e-06','0','0','0','0','0','-2.05605e-06','4.84501e-06','6.03319e-08','1.21132e-09','0','0','0','0','0','1.27781e-07','4.14091e-06','1.21132e-09','0.000192127','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062832, ("CSC", 2, 4, 2, 14), "MEm42_14"))
reports[-1].posNum = 2387
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00664727, 0.0206229, 0), \
                           ValErr(-0.148048, 0.503561, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.22157e-05, 0.000234969, 0), \
                           -3265.69, 2387, 2387, -nan)
reports[-1].sigmaresid = ValErr(0.950434, 0.0137554, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0149048, None, -0.000142428, None, 0.00504714, None, 0.000233409, None, 0.00504714, None, 0.000233409, None, 0.0204707, None, 0.000333816, None, 0.0204707, None, 0.000333816, None, 0.950472, None, 0.0112896, None, 0.950472, None, 0.0112896, None)
reports[-1].CovMatrix = ['0.000425303','-0.00012733','-1.6072e-06','1.13252e-07','0','0','0','0','0','-0.00012733','0.253574','-5.73792e-07','4.19115e-06','0','0','0','0','0','-1.6072e-06','-5.73792e-07','5.52103e-08','1.21546e-09','0','0','0','0','0','1.13252e-07','4.19115e-06','1.21546e-09','0.000189212','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062848, ("CSC", 2, 4, 2, 16), "MEm42_16"))
reports[-1].posNum = 2241
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000934518, 0.0221064, 0), \
                           ValErr(0.187979, 0.543914, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000126795, 0.000256735, 0), \
                           -3122.83, 2241, 2241, -nan)
reports[-1].sigmaresid = ValErr(0.974844, 0.0145606, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00799662, None, -0.00216996, None, -0.00267353, None, -0.00180633, None, -0.00267353, None, -0.00180633, None, 0.00939746, None, -0.00185812, None, 0.00939746, None, -0.00185812, None, 0.974959, None, 0.0101135, None, 0.974959, None, 0.0101135, None)
reports[-1].CovMatrix = ['0.000488692','-0.000610944','-2.04743e-06','1.32351e-07','0','0','0','0','0','-0.000610944','0.295842','1.87982e-06','3.76387e-06','0','0','0','0','0','-2.04743e-06','1.87982e-06','6.59131e-08','1.45939e-09','0','0','0','0','0','1.32351e-07','3.76387e-06','1.45939e-09','0.000212012','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062864, ("CSC", 2, 4, 2, 18), "MEm42_18"))
reports[-1].posNum = 2251
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00974757, 0.0215934, 0), \
                           ValErr(0.510971, 0.548453, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.04232e-05, 0.000243552, 0), \
                           -3103.97, 2251, 2251, -nan)
reports[-1].sigmaresid = ValErr(0.960738, 0.0143178, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0275831, None, 0.00115732, None, 0.0102938, None, 0.00111124, None, 0.0102938, None, 0.00111124, None, 0.019112, None, 0.00116019, None, 0.019112, None, 0.00116019, None, 0.960978, None, 0.00970456, None, 0.960978, None, 0.00970456, None)
reports[-1].CovMatrix = ['0.000466275','0.000613726','-1.81808e-06','1.51047e-07','0','0','0','0','0','0.000613726','0.300801','-7.35304e-06','4.39916e-06','0','0','0','0','0','-1.81808e-06','-7.35304e-06','5.93175e-08','1.0253e-09','0','0','0','0','0','1.51047e-07','4.39916e-06','1.0253e-09','0.000205','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062880, ("CSC", 2, 4, 2, 20), "MEm42_20"))
reports[-1].posNum = 2133
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0212134, 0.0226636, 0), \
                           ValErr(-0.123012, 0.543478, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000195849, 0.000259148, 0), \
                           -2904.72, 2133, 2133, -nan)
reports[-1].sigmaresid = ValErr(0.944454, 0.0144598, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0105497, None, -0.000146116, None, 0.0138325, None, 0.000116834, None, 0.0138325, None, 0.000116834, None, -0.0137498, None, 5.84989e-05, None, -0.0137498, None, 5.84989e-05, None, 0.9446, None, 0.00958772, None, 0.9446, None, 0.00958772, None)
reports[-1].CovMatrix = ['0.00051364','-0.000159413','-2.53187e-06','1.17757e-07','0','0','0','0','0','-0.000159413','0.295368','4.3328e-06','5.06298e-06','0','0','0','0','0','-2.53187e-06','4.3328e-06','6.71577e-08','1.33158e-09','0','0','0','0','0','1.17757e-07','5.06298e-06','1.33158e-09','0.000209087','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062896, ("CSC", 2, 4, 2, 22), "MEm42_22"))
reports[-1].posNum = 2313
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0178839, 0.0220757, 0), \
                           ValErr(-0.141616, 0.536901, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.31983e-06, 0.000251411, 0), \
                           -3272.12, 2313, 2313, -nan)
reports[-1].sigmaresid = ValErr(0.995731, 0.0146398, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000660173, None, -0.000750394, None, 0.0178289, None, -0.000589017, None, 0.0178289, None, -0.000589017, None, 0.00749076, None, -0.000632048, None, 0.00749076, None, -0.000632048, None, 0.995752, None, 0.0098438, None, 0.995752, None, 0.0098438, None)
reports[-1].CovMatrix = ['0.000487337','0.00068756','-1.91767e-06','1.3878e-07','0','0','0','0','0','0.00068756','0.288262','-1.01717e-05','5.00941e-06','0','0','0','0','0','-1.91767e-06','-1.01717e-05','6.32077e-08','1.3315e-09','0','0','0','0','0','1.3878e-07','5.00941e-06','1.3315e-09','0.000214325','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062912, ("CSC", 2, 4, 2, 24), "MEm42_24"))
reports[-1].posNum = 2517
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00271407, 0.0217045, 0), \
                           ValErr(0.0863408, 0.538488, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.58413e-05, 0.000245186, 0), \
                           -3624.09, 2517, 2517, -nan)
reports[-1].sigmaresid = ValErr(1.02114, 0.0143923, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0171644, None, -0.00202694, None, -0.003709, None, -0.00191419, None, -0.003709, None, -0.00191419, None, -0.0482745, None, -0.00172876, None, -0.0482745, None, -0.00172876, None, 1.02114, None, 0.0102231, None, 1.02114, None, 0.0102231, None)
reports[-1].CovMatrix = ['0.000471084','-0.000590214','-1.84293e-06','1.13208e-07','0','0','0','0','0','-0.000590214','0.28997','9.38321e-06','5.1433e-06','0','0','0','0','0','-1.84293e-06','9.38321e-06','6.01161e-08','1.63832e-09','0','0','0','0','0','1.13208e-07','5.1433e-06','1.63832e-09','0.000207139','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062928, ("CSC", 2, 4, 2, 26), "MEm42_26"))
reports[-1].posNum = 1816
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0111926, 0.026504, 0), \
                           ValErr(0.232118, 0.621176, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000239837, 0.000291498, 0), \
                           -2494.07, 1816, 1816, -nan)
reports[-1].sigmaresid = ValErr(0.955491, 0.0158549, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0203057, None, 0.00133733, None, 0.000596207, None, 0.0014129, None, 0.000596207, None, 0.0014129, None, 0.00255809, None, 0.00142111, None, 0.00255809, None, 0.00142111, None, 0.955685, None, 0.0105736, None, 0.955685, None, 0.0105736, None)
reports[-1].CovMatrix = ['0.00070246','-0.000296708','-4.11723e-06','1.31188e-07','0','0','0','0','0','-0.000296708','0.38586','8.58122e-11','4.73853e-06','0','0','0','0','0','-4.11723e-06','8.58122e-11','8.49711e-08','1.53004e-09','0','0','0','0','0','1.31188e-07','4.73853e-06','1.53004e-09','0.000251381','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062944, ("CSC", 2, 4, 2, 28), "MEm42_28"))
reports[-1].posNum = 2063
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0102954, 0.0234913, 0), \
                           ValErr(0.149297, 0.549754, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.15802e-05, 0.000261975, 0), \
                           -2826.36, 2063, 2063, -nan)
reports[-1].sigmaresid = ValErr(0.952229, 0.0148237, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000807183, None, 0.0018478, None, -0.00910727, None, 0.00179056, None, -0.00910727, None, 0.00179056, None, 0.00913269, None, 0.00174054, None, 0.00913269, None, 0.00174054, None, 0.952282, None, 0.0105562, None, 0.952282, None, 0.0105562, None)
reports[-1].CovMatrix = ['0.000551841','0.000385273','-2.77503e-06','1.20037e-07','0','0','0','0','0','0.000385273','0.30223','-5.02298e-06','3.74376e-06','0','0','0','0','0','-2.77503e-06','-5.02298e-06','6.8631e-08','1.44851e-09','0','0','0','0','0','1.20037e-07','3.74376e-06','1.44851e-09','0.000219744','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062960, ("CSC", 2, 4, 2, 30), "MEm42_30"))
reports[-1].posNum = 1641
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00861415, 0.0295869, 0), \
                           ValErr(-0.293372, 0.632814, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000273376, 0.000318458, 0), \
                           -2174.07, 1641, 1641, -nan)
reports[-1].sigmaresid = ValErr(0.9102, 0.0158854, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00829368, None, -0.00243002, None, -0.0089428, None, -0.00217199, None, -0.0089428, None, -0.00217199, None, -0.00520203, None, -0.00230709, None, -0.00520203, None, -0.00230709, None, 0.910446, None, 0.00963018, None, 0.910446, None, 0.00963018, None)
reports[-1].CovMatrix = ['0.000875382','-0.00306558','-6.03993e-06','-1.08932e-07','0','0','0','0','0','-0.00306558','0.400454','1.7085e-05','1.9632e-06','0','0','0','0','0','-6.03993e-06','1.7085e-05','1.01415e-07','1.55771e-09','0','0','0','0','0','-1.08932e-07','1.9632e-06','1.55771e-09','0.00025235','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062976, ("CSC", 2, 4, 2, 32), "MEm42_32"))
reports[-1].posNum = 1944
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0146993, 0.0263939, 0), \
                           ValErr(0.355083, 0.571235, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000276518, 0.000300651, 0), \
                           -2616.45, 1944, 1944, -nan)
reports[-1].sigmaresid = ValErr(0.92958, 0.0149082, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0208697, None, 0.00152332, None, -0.000478638, None, 0.0015378, None, -0.000478638, None, 0.0015378, None, 0.0319843, None, 0.00146607, None, 0.0319843, None, 0.00146607, None, 0.929862, None, 0.0106962, None, 0.929862, None, 0.0106962, None)
reports[-1].CovMatrix = ['0.000696638','0.000931249','-4.76245e-06','8.04757e-08','0','0','0','0','0','0.000931249','0.326309','-5.73839e-06','4.46189e-06','0','0','0','0','0','-4.76245e-06','-5.73839e-06','9.03912e-08','1.63326e-09','0','0','0','0','0','8.04757e-08','4.46189e-06','1.63326e-09','0.000222256','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062992, ("CSC", 2, 4, 2, 34), "MEm42_34"))
reports[-1].posNum = 2284
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0013338, 0.0219132, 0), \
                           ValErr(0.258246, 0.52881, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00015429, 0.000249604, 0), \
                           -3176.43, 2284, 2284, -nan)
reports[-1].sigmaresid = ValErr(0.972139, 0.0143826, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0376272, None, 0.00154422, None, -0.0038495, None, 0.00178672, None, -0.0038495, None, 0.00178672, None, 0.00156475, None, 0.00163953, None, 0.00156475, None, 0.00163953, None, 0.972317, None, 0.0110433, None, 0.972317, None, 0.0110433, None)
reports[-1].CovMatrix = ['0.000480189','0.000177403','-2.03319e-06','1.39275e-07','0','0','0','0','0','0.000177403','0.27964','-1.29791e-06','3.78976e-06','0','0','0','0','0','-2.03319e-06','-1.29791e-06','6.23022e-08','1.27378e-09','0','0','0','0','0','1.39275e-07','3.78976e-06','1.27378e-09','0.000206861','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604063008, ("CSC", 2, 4, 2, 36), "MEm42_36"))
reports[-1].posNum = 2297
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0168013, 0.0226074, 0), \
                           ValErr(-0.506385, 0.558755, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00010958, 0.00025733, 0), \
                           -3272.01, 2297, 2297, -nan)
reports[-1].sigmaresid = ValErr(1.00555, 0.0148357, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0167362, None, -0.00122661, None, -0.0137835, None, -0.000568146, None, -0.0137835, None, -0.000568146, None, 0.00231622, None, -0.00080419, None, 0.00231622, None, -0.00080419, None, 1.00576, None, 0.0127979, None, 1.00576, None, 0.0127979, None)
reports[-1].CovMatrix = ['0.000511093','-0.000229751','-2.16078e-06','1.28864e-07','0','0','0','0','0','-0.000229751','0.312207','-3.6193e-06','4.61685e-06','0','0','0','0','0','-2.16078e-06','-3.6193e-06','6.62185e-08','1.4464e-09','0','0','0','0','0','1.28864e-07','4.61685e-06','1.4464e-09','0.000220099','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

