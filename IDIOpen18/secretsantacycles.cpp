#include <vector>
#include <iostream>


using namespace std;
class UnionFind {
private:
	vector<int> p, rank, setSize, doublePointers;
	vector<bool> hasGiftGiven;
	//p er lederen til hver enkelt node
	// rank er kun for o p t i m a l i s e r i n g naar vi slaar sammen grupper
	// setSize er antall noder i hver gruppe
	int numSets; // antall grupper
	int start;
public:
	UnionFind(int N){
		start = N;
		setSize.assign(N, 1); // er kun 1 i hver gruppe
		numSets = N; //N grupper
		rank.assign(N, 0);
		p.assign(N, 0);
		hasGiftGiven.assign(N, false);
		doublePointers.assign(N, 0);
		for (int i = 0; i < N; i++)
			p[i] = i;
	}

	int findSet(int i) {
		return (p[i] == i) ? i : (p[i] = findSet(p[i]));
		//p[i]= findSet (p[i]) er kun for aa optimalisere ,
		// slik at den husker hvem som er lederen til neste gang
	}
	bool isSameSet(int i, int j) {
		return findSet(i) == findSet(j);
	}
	//Får, gir
	void unionSet(int i, int j) {
		if (!isSameSet(i, j)) {
			numSets--;
		}
		// cout << "får: " << i << " gir: " << j << endl;
		if (hasGiftGiven[i]) {
			// cout << "--------------------" << endl;
			// cout << "antall feil i " << findSet(j) << " før merging er " << doublePointers[findSet(j)] << endl;
			// cout << "antall feil i " << findSet(i) << " før merging er " << doublePointers[findSet(i)] << endl;
			doublePointers[findSet(i)] += 1 + doublePointers[findSet(j)];
			// cout << "antall feil i " << findSet(j) << " etter merging er " << doublePointers[findSet(j)] << endl;
			// cout << "antall feil i " << findSet(i) << " etter merging er " << doublePointers[findSet(i)] << endl;
			// cout << "--------------------" << endl;
		}
		else {
			doublePointers[findSet(i)] += doublePointers[findSet(j)];
			hasGiftGiven[i] = true;
		}
		// doublePointers[findSet(j)] = 0;
		int x = findSet(i), y = findSet(j);
		p[y] = x;
		doublePointers[y] = doublePointers[x];
		setSize[x] += setSize[y];
	}
	int numTurns() {
		int changes = numSets;
		bool noChanges = true;
		for (int i = 0; i < start; i++) {
			if (i == findSet(i)) {
				// cout << "antall feil i " << i << " er " << doublePointers[i] << endl;
				if (doublePointers[i] != 0) {
					noChanges = false;
					changes += doublePointers[i]-1;
				}
			}
		}
		if (noChanges&&numSets==1)
			return 0;
		return changes;
	}

	int numDisjointSets() { return numSets; }
	int sizeOfSet(int i) { return setSize[findSet(i)]; }
};


int main() {
	int a;
	cin >> a;
	UnionFind UF(a);
	for (int i = 0; i < a; i++) {
		int b; 
		cin >> b;
		UF.unionSet(b - 1, i);
	}
	cout << UF.numTurns() << endl;
}

/*
2 2 1 -> 0 
2 1 2 -> 2
1 1 -> 0
4 2 1 4 3 -> 2
4 1 1 1 4 -> 3
6 2 3 4 5 1 2 -> 1
8 2 3 1 6 4 4 4 8 -> 4
*/