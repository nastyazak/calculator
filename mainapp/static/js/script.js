var vm = new Vue({
	el: '#app',
	data: {
		categories: [],
		works: [],
		selected_works: [],
		order_works: []
	},
	created: function () {
		axios.get('api/categories').then(function (response){
			vm.categories = response.data
		});
		axios.get('api/works').then(function (response){
			vm.works = response.data
		});
	},
	computed: {		//начинает срабатывать когда что-то изменилось (напр. выбрал работу)
		sum: function () {
			let arr=[]
			// получить список выбранных работ
			for(i = 0; i < this.selected_works.length; i++) {
				elem = this.selected_works[i]
				if(Array.isArray(elem)) {	//проверка яляется ли объект массивом
					for(j = 0; j < elem.length; j++)
						arr.push(elem[j])
				}
				else {
					arr.push(elem)
				}
			}
			this.order_works = arr  //одномерный массив работ
			// суммирвание
			return arr.reduce(function(summa, current_elem) {		//текущая сумма (при старте = 0), текущий элемент
			 	return summa + current_elem.cost;
			 	}, 0);
		}
	},
	watch: {
		categories: function () {		//срабатывает, когда categories меняется (забрались с сервера)
			for(var i= 0; i < this.categories.length; i++) {
				this.selected_works[i] = [];
			}
		}
	},
	methods: {
		submit: function (){		//срабатывает при нажатии на кнопку
			if (this.sum === 0){
				alert('Сделайте выбор')
				return;
			}
			const order = {
				order: {
					id_user : id_user
				},
				order_works: this.order_works.map(obj => ({ id_work: obj.id }))
			}

			axios.defaults.headers.post['X-CSRFToken'] = document.querySelector('[name=csrfmiddlewaretoken]').value;	//передаем значени токена на сервер
			axios.post('/api/order/', order)
			 	.then(response => {
					window.location.href = "/thanks/";
				})
			 	.catch(error => {
					 alert(error);
				});

		}
	}
})
