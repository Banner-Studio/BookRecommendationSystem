import math
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BookRecommend.settings")
django.setup()

from data.models import ReaderInfo, BookInfo

class UserCf:
    """基于用户的协调过滤算法类"""

    @staticmethod
    def user_sim(target_user_rid):
        """计算用户相似度"""
        # 基于目标用户rid获取目标用户id
        target_user = ReaderInfo.objects.get(rid=target_user_rid)
        target_user_id = target_user.id
        # 基于目标用户id获取目标用户读过的书籍
        #   基于列去重
        target_user_books = BookInfo.objects.filter(breader=target_user_id).distinct() .order_by('bname')
        # 基于目标用户读过的书籍获取相似用户
        user_sim_dict = {}
        print(target_user_books)
        for target_user_book in target_user_books:
            users = ReaderInfo.objects.filter(bookinfo__bname=target_user_book.bname)
        for user in users:
            user_sim_dict[user.id] = 0
        if target_user.id in user_sim_dict.keys():
            del user_sim_dict[target_user_id]
        print(str(user_sim_dict))
        # 计算用户相似度：
        # 获取目标用户读过的书的数量
        target_user_books_num = target_user_books.count()
        # 假设相似用户和目标用户读过的相同书量为0
        book_same_num = 0
        # 假设用户相似度为0
        user_similarity = 0
        for user_sim_id in user_sim_dict:
            # 获取相似用户读过的书的数量
            user_sim_book_num = BookInfo.objects.filter(breader=user_sim_id).count()
            for target_user_book in target_user_books:
                book_same_num1 = BookInfo.objects.filter(bname=target_user_book, breader=user_sim_id)
                book_same_num += book_same_num1.count()
                # 获取和目标用户读过的书相同的相似用户数目
                user_book_same_num = ReaderInfo.objects.filter(bookinfo__bname=target_user_book)\
                    .exclude(id=target_user_id).count()
                if user_book_same_num:
                    user_similarity1 = book_same_num*1 / (math.log(1) + user_book_same_num)
                else:
                    user_similarity1 = 0
                user_similarity += user_similarity1
            user_similarity = user_similarity/math.sqrt(target_user_books_num * user_sim_book_num)
            # print(user_similarity)
            user_sim_dict[user_sim_id] = user_similarity
            # print(user_sim_book_num)
            # print(str(user_sim_dict))
        return user_sim_dict
    def target_user_book_interest(self):
        """用UserCF算法计算目标用户对物品的感兴趣程度"""

UserCf.user_sim(20151435113)
