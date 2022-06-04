class PohonBiner:
	def __init__(self,A,L,R):
		self.A = A
		self.L = L
		self.R = R

def MakePB(A,L,R):
	return PohonBiner(A,L,R)

def Akar(P):
	return P.A

def Left(P):
	return P.L

def Right(P):
	return P.R

def IsTreeEmpty(P):
	if(P == None):
		return True
	else:
		return False

def IsOneElmtPB(P):
	if(not IsTreeEmpty(P) and IsTreeEmpty(Right(P)) and IsTreeEmpty(Left(P))):
		return True
	else:
		return False

def IsUnerLeftPB(P):
	if(not IsTreeEmpty(P) and IsTreeEmpty(Right(P)) and not IsTreeEmpty(Left(P))):
		return True
	else:
		return False

def IsUnerRightPB(P):
	if(not IsTreeEmpty(P) and not IsTreeEmpty(Right(P)) and IsTreeEmpty(Left(P))):
		return True
	else:
		return False

def IsBinerPB(P):
	if(not IsTreeEmpty(P) and not IsTreeEmpty(Right(P)) and not IsTreeEmpty(Left(P))):
		return True
	else:
		return False

def NbElmtPB(P):
	if(IsOneElmtPB(P)):
		return 1
	else:
		if(IsBinerPB(P)):
			return NbElmtPB(Left(P)) + 1 + NbElmtPB(Right(P))
		elif(IsUnerLeftPB(P)):
			return NbElmtPB(Left(P)) + 1
		elif(IsUnerRightPB(P)):
			return 1 + NbElmtPB(Right(P))

def NbDaunPB(P):
	if(IsOneElmtPB(P)):
		return 1
	else:
		if(IsBinerPB(P)):
			return NbDaunPB(Left(P)) + NbDaunPB(Right(P))
		elif(IsUnerLeftPB(P)):
			return NbDaunPB(Left(P))
		elif(IsUnerRightPB(P)):
			return NbDaunPB(Right(P))


P1 = MakePB(1,
			MakePB(
				2,
				None,
				None
			),
			MakePB(
				3,
				MakePB(
					4,
					None,
					MakePB(
						5,
						None,
						None
					)
				),
				None
			)
		)

P2= MakePB(
		"^",
		MakePB(
			"*",
			MakePB(
				"+",
				MakePB(
					"3",
					None,
					None
				),
				MakePB(
					"4",
					None,
					None
				)
			),
			MakePB(
				"/",
				MakePB(
					"8",
					None,
					None
				),
				MakePB(
					"21",
					None,
					None
				)
			),
		),
		MakePB(
			"10",
			None,
			None
		)
	)

P3 = MakePB(2,
		    MakePB(
			    4,
                None,
                None
            ),
			MakePB(
				6,
				None,
				MakePB(
					1,
					None,
					None
				    )
		        )
            )

print(NbElmtPB(P1))
print(NbElmtPB(P2))
print(NbElmtPB(P3))
print(NbDaunPB(P1))
print(NbDaunPB(P2))
print(NbDaunPB(P3))