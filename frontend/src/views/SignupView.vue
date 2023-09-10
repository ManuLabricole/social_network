<template>
	<div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
		<div class="main-left">
			<div class="p-12 bg-white border border-gray-200 rounded-lg">
				<h1 class="mb-6 text-2xl">Sign up</h1>

				<p class="mb-6 text-gray-500">
					Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum
					dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit
					mate. Lorem ipsum dolor sit mate.
				</p>

				<p class="font-bold">
					Already have an account?
					<RouterLink
						:to="{ name: 'login' }"
						class="underline"
						>Click here</RouterLink
					>
					to log in!
				</p>
			</div>
		</div>

		<div class="main-right">
			<div class="p-12 bg-white border border-gray-200 rounded-lg">
				<form
					class="space-y-6"
					v-on:submit.prevent="submitForm">
					<div>
						<label>Name</label><br />
						<input
							type="text"
							v-model="form.name"
							placeholder="Your full name"
							class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-xl" />
					</div>

					<div>
						<label>E-mail</label><br />
						<input
							type="email"
							v-model="form.email"
							placeholder="Your e-mail address"
							class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-xl" />
					</div>

					<div>
						<label>Password</label><br />
						<input
							type="password"
							v-model="form.password1"
							placeholder="Your password"
							class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-xl" />
					</div>

					<div>
						<label>Repeat password</label><br />
						<input
							type="password"
							v-model="form.password2"
							placeholder="Repeat your password"
							class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-xl" />
					</div>

					<template v-if="errors.length > 0">
						<div class="mt-4">
							<ul class="list-disc list-inside text-sm text-red-500">
								<li v-for="error in errors">{{ error }}</li>
							</ul>
						</div>
					</template>

					<div>
						<button class="py-4 px-6 bg-purple-600 text-white rounded-lg">
							Sign up
						</button>
					</div>
				</form>
			</div>
		</div>
	</div>
</template>

<script>
	import axios from 'axios';

	import { useToastStore } from '@/stores/toast';

	export default {
		setup() {
			const toastStore = useToastStore();
			return { toastStore };
		},

		data() {
			return {
				form: {
					email: '',
					name: '',
					password1: '',
					password2: '',
				},
				errors: [],
			};
		},

		methods: {
			submitForm() {
				this.errors = [];

				if (this.form.email === '') {
					this.errors.push('Your e-mail is missing');
				}

				if (this.form.name === '') {
					this.errors.push('Your name is missing');
				}

				if (this.form.password1 === '') {
					this.errors.push('Your password is missing');
				}

				if (this.form.password1 !== this.form.password2) {
					this.errors.push('The password does not match');
				}

				if (this.errors.length === 0) {
					axios
						.post('/api/v1/signup/', this.form)
						.then((response) => {
							console.log('response', response);
							if (response.data.message === 'success') {
								this.toastStore.showToast(
									5000,
									'The user is registered. Please log in',
									'bg-emerald-500'
								);

								this.form.email = '';
								this.form.name = '';
								this.form.password1 = '';
								this.form.password2 = '';
							} else {
								this.toastStore.showToast(
									5000,
									'Something went wrong. Please try again',
									'bg-red-300'
								);
								this.errors.push(response.data.errors)
							}
						})
						.catch((error) => {
							console.log('error', error);
						});
					console.log('POST REQUEST');
				}
			},
		},
	};
</script>
```
