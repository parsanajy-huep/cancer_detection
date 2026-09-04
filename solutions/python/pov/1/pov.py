from json import dumps

class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def _dict_(self):
        return {self.label: [c._dict_() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self._dict_(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self._dict_() == other._dict_()

    # پیدا کردن مسیر از ریشه به یک گره مشخص (بر اساس لیبل)
    # خروجی: لیستی از خودِ گره‌ها (Node objects)
    def _find_path_nodes(self, label, path=None):
        if path is None:
            path = []
        path = path + [self]
        
        if self.label == label:
            return path
            
        for child in self.children:
            result = child._find_path_nodes(label, path)
            if result:
                return result
        return None

    # کپی کردن یک گره و همه فرزندانش، به جز گره‌ای که باید رد شود (برای جلوگیری از چرخه)
    def _copy_subtree(self, node_to_skip=None):
        new_children = []
        for child in self.children:
            if child is node_to_skip:
                continue
            new_children.append(child._copy_subtree())
        return Tree(self.label, new_children)

    def from_pov(self, from_node):
        # 1. پیدا کردن مسیر از ریشه تا گره هدف
        path_nodes = self._find_path_nodes(from_node)
        if not path_nodes:
            raise ValueError("Tree could not be reoriented")
        
        # 2. شروع ساخت درخت جدید از پایین مسیر (گره هدف)
        # ابتدا یک کپی از گره هدف می‌سازیم (با همه فرزندانش)
        new_root = path_nodes[-1]._copy_subtree()
        
        # متغیری که نشان می‌دهد درخت جدید در حال رشد کجاست
        current_new_node = new_root
        
        # 3. حالا از والد هدف تا ریشه قدیمی بالا می‌رویم
        for i in range(len(path_nodes) - 2, -1, -1):
            parent_node = path_nodes[i]
            
            # یک کپی از والد می‌سازیم، اما فرزندِ مسیر را از آن حذف می‌کنیم
            # تا چرخه ایجاد نشود
            new_parent = parent_node._copy_subtree(node_to_skip=path_nodes[i+1])
            
            # والد جدید را به عنوان فرزند به درخت فعلی اضافه می‌کنیم
            current_new_node.children.append(new_parent)
            
            # حالا والد جدید، ریشه‌ی در حال رشد می‌شود
            current_new_node = new_parent
            
        # 4. انتقال اطلاعات درخت جدید به خودِ self
        self.label = new_root.label
        self.children = new_root.children
        
        return self

    def path_to(self, from_node, to_node):
        # اول گره شروع را ریشه می‌کنیم
        self.from_pov(from_node)
        
        # حالا مسیر تا گره مقصد را پیدا می‌کنیم
        path_nodes = self._find_path_nodes(to_node)
        if not path_nodes:
            raise ValueError("No path found")
            
        return [node.label for node in path_nodes]
