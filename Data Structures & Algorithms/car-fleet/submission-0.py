class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Unisce posizione e velocità, e ordina in base alla posizione decrescente
        auto_ordinate = sorted(zip(position, speed), reverse=True)
        
        ris = []

        for macchina in auto_ordinate:
            if not ris:
                ris.append((target-macchina[0])/macchina[1])
                continue
            if ((target-macchina[0])/macchina[1]) > ris[-1]:
                ris.append((target-macchina[0])/macchina[1])

        return len(ris)
            