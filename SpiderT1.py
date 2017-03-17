import requests
import re

def MySpider(page, rep):
	payload = {'cn': '', 'ci': 0, 'pcn': '娱乐明星', 'pci': 0, 'ct': 1, 'st': 'new', 'pn': page} 
	r = requests.get('http://tieba.baidu.com/f/index/forumpark', params = payload)

	balist = re.findall(rep, r.text)
	return balist

if __name__ == '__main__':
	rep = re.compile(r'<div class="ba_content">.*?<div class="ba_post')

	for i in range(31)[1:]:
		balist = MySpider(i, rep)
		#print(len(balist))

		re_name  = re.compile(r'<p class="ba_name">(.*?)</p>')
		re_m_num = re.compile(r'<span class="ba_m_num">(.*?)</span>')
		re_p_num = re.compile(r'<span class="ba_p_num">(.*?)</span>')
		re_desc  = re.compile(r'<p class="ba_desc">(.*?)</p>')

		for bacontent in balist:
			ba_name  = "Ba_name:     " + re.search(re_name,  bacontent).group(1) + "\n"
			ba_m_num = "Ba_m_number: " + re.search(re_m_num, bacontent).group(1) + "\n"
			ba_p_num = "Ba_p_number: " + re.search(re_p_num, bacontent).group(1) + "\n"
			ba_desc  = "Ba_desc:     " + re.search(re_desc,  bacontent).group(1) + "\n"
			ba_hr    = "================WARNING==DENGER===================\n"

			with open("E:\Programs\Python\exercises\Spider\Results\Rel3.txt", "a", encoding = "UTF-8") as f:
				f.write(ba_name + ba_m_num + ba_p_num + ba_desc + ba_hr)
