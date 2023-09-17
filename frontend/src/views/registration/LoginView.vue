<template>
	<div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
		<div class="main-left">
			<div class="p-12 bg-white border border-gray-200 rounded-lg">
				<h1 class="mb-6 text-2xl">Log in</h1>

				<p class="mb-6 text-gray-500">
					Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum
					dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit
					mate. Lorem ipsum dolor sit mate.
				</p>

				<p class="font-bold">
					Don't have an account?
					<RouterLink
						:to="{ name: 'signup' }"
						class="underline"
						>Click here</RouterLink
					>
					to create one!
				</p>
			</div>
		</div>

		<div class="main-right">
			<div class="p-12 bg-white border border-gray-200 rounded-lg">
				<form
					class="space-y-6"
					v-on:submit.prevent="submitForm">
					<div>
						<label>E-mail</label><br />
						<input
							type="email"
							v-model="form.email"
							placeholder="Your e-mail address"
							class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg" />
					</div>

					<div>
						<label>Password</label><br />
						<input
							type="password"
							v-model="form.password"
							placeholder="Your password"
							class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg" />
					</div>

					<div>
						<button class="py-4 px-6 bg-purple-600 text-white rounded-lg">
							Log in
						</button>
					</div>
				</form>
			</div>
		</div>
	</div>
</template>

<script>
	import axios from 'axios';
	import { useUserStore } from '@/stores/user';
	export default {
		setup() {
			const userStore = useUserStore();
			return { userStore };
		},

		data() {
			return {
				form: {
					email: '',
					password: '',
				},
				errors: [],
			};
		},
		methods: {
			async submitForm() {
				this.errors = [];

				if (this.form.email === '') {
					this.errors.push('Your e-mail is missing');
				}

				if (this.form.password === '') {
					this.errors.push('Your password is missing');
				}

				if (this.errors.length === 0) {
					await axios
						.post('/api/v1/login/', this.form)
						.then((response) => {
							this.userStore.setToken(response.data);

							// console.log(response.data.access);

							axios.defaults.headers.common['Authorization'] =
								'Bearer ' + response.data.access;
						})
						.catch((error) => {
							console.log('error', error);
						});

					await axios
						.get('/api/v1/me/')
						.then((response) => {
							// console.log('API/ME response', response);
							this.userStore.setUserInfo(response.data);

							this.$router.push('/feed');
						})
						.catch((error) => {
							console.log('API/ME error', error);
						});
				}
			},
		},
	};
</script>
