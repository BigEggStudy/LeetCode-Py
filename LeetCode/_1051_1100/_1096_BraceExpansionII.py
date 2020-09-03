#-----------------------------------------------------------------------------
# Runtime: 48ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def braceExpansionII(self, expression: str) -> [str]:
        stack, union, product = [], [], [""]

        for ch in expression:
            if ch == '{':
                stack.append(union)
                stack.append(product)
                union, product = [], [""]
            elif ch == '}':
                pre_product = stack.pop()
                pre_union = stack.pop()

                for item in product:
                    union.append(item)
                product = []

                for str1 in pre_product:
                    for str2 in union:
                        product.append(str1 + str2)
                union = pre_union
            elif ch == ',':
                for item in product:
                    union.append(item)
                product = [""]
            else:
                for i in range(len(product)):
                    product[i] += ch

        for item in product:
            union.append(item)
        return sorted(set(union))
