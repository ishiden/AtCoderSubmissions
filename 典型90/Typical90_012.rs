use proconio::input;

struct UnionFind {
    parent: Vec<usize>
} impl UnionFind {
    fn new(size: usize) -> UnionFind {
        UnionFind {
            parent: vec![0; size]
        }
    }
    fn root(&mut self, pos: usize) -> usize {
        let current_par = self.parent[pos];
        if current_par == 0 {
            pos
        } else {
            self.parent[pos] = self.root(current_par);
            self.parent[pos]
        }
    }
    fn unite(&mut self, a: usize, b: usize) {
        let root_a = self.root(a);
        let root_b = self.root(b);
        if root_a != root_b {
            self.parent[root_a] = root_b
        }
    }
    fn same(&mut self, a: usize, b: usize) -> bool {
        self.root(a) == self.root(b)
    }
}

fn main() {
    input!{
        h: usize, w: usize,
        q: usize
    }
    let hash = |r: usize, c:usize| w * r + c;
    let mut used = vec![vec![false; 1+w+1]; 1+h+1];
    let mut uf = UnionFind::new(hash(1+h+1, 1+w+1));

    let mut ans = String::new();
    let mut handle_query = |querytype:u8| {
        if querytype == 1 {
            input!{ r:usize, c:usize}
            used[r][c] = true;
            let next_to = [(r-1, c), (r, c+1), (r+1, c), (r, c-1)];
            for n in next_to.iter() {
                if used[n.0][n.1] {
                    uf.unite(hash(r, c), hash(n.0, n.1));
                }
            }
        }
        if querytype == 2 {
            input! { ra:usize, ca:usize, rb:usize, cb:usize }
            let can_follow =
                if !used[ra][ca] && !used[rb][cb] {
                    false
                } else {
                    uf.same(hash(ra, ca), hash(rb, cb))
                };
            ans += if can_follow {
                "Yes\n"
            } else {
                "No\n"
            }
        }
    };
    for _ in 0..q {
        input! { query_type: u8 }
        handle_query(query_type)
    }
    print!("{}", ans);
}