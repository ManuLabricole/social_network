<template>
	<div
		class="flex align-center"
		v-if="user.isAuthenticated">
		<router-link :to="{ name: 'profile', params: { id: user.id } }">
			<img
				src="https://i.pravatar.cc/40?img=70"
				class="rounded-full" />
		</router-link>
		<button
			class="ml-4 py-4 px-6 bg-purple-600 text-white rounded-lg"
			@click="logout">
			Logout
		</button>
	</div>
</template>

<script>
	import axios from 'axios';
	import { useUserStore } from '@/stores/user';

	export default {
		setup() {
			console.log('User setup');
			const userStore = useUserStore();
			console.log('isAuthenticated', userStore.user.isAuthenticated);
			return { userStore };
		},
		computed: {
			user() {
				return this.userStore.user;
			},
		},

		methods: {
			login() {
				console.log('Fetching profile info');
				axios
					.get('/api/v1/me/')
					.then((response) => {
						console.log('API/ME response', response);
						this.userStore.setUserInfo(response.data);
					})
					.catch((error) => {
						console.log('API/ME error', error);
						this.errors.push(error);
					});
				console.log(this.userStore.user);
			},
			logout() {
				const userStore = useUserStore();
				userStore.removeToken();
				this.$router.push({ name: 'login' });
			},
		},
	};
</script>

<style lang="scss" scoped></style>
