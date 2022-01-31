# 페이지가 로딩되면, 두 가지 기능을 수행해야 합니다.

# 1) 주문하기(POST): 주문 정보 입력 후 '주문하기' 클릭 시 주문 목록에 추가되어야 합니다.
# 2) 주문내역보기(GET): 하단 주문 목록이 자동으로 보여야 합니다.



from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('shop_index.html')

@app.route('/orders', methods=['POST'])
def write_order():
# 1. 클라이언트가 준 정보 가져오기.from make_review()
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']
	# 2. DB에 정보 삽입하기
    doc = {
        'name': name_receive,
        'quantity': quantity_receive,
        'address': address_receive,
        'phone': phone_receive
    }
    db.orders.insert_one(doc)

	# 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '주문 성공!.'})

@app.route('/orders', methods=['GET'])
def load_orders():
    orders = list(db.orders.find({},{'_id': False}))
    return jsonify({'result':'success', 'orders': orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=4444, debug=True)
