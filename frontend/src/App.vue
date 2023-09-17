<template>
	<NavigationBar :user="user" />
	<main class="px-8 py-6 bg-gray-100">
		<RouterView />
		<Toast />
	</main>
</template>

<script>
	import NavigationBar from '@/components/NavigationBar.vue';
	import Toast from '@/components/common/Toast.vue';
	import axios from 'axios';
	import { useUserStore } from '@/stores/user';
	import { onBeforeMount } from 'vue';

	export default {
		components: {
			NavigationBar,
			Toast,
		},

		setup() {
			const userStore = useUserStore();

			// Equivalent to beforeCreate lifecycle hook in Options API
			onBeforeMount(() => {
				userStore.initStore();

				const token = userStore.user.access;

				if (token) {
					axios.defaults.headers.common['Authorization'] = 'Bearer ' + token;
				} else {
					axios.defaults.headers.common['Authorization'] = '';
				}
			});

			return {
				userStore,
				user: userStore.user,
			};
		},
		watch: {
			user: {
				handler() {
					console.log('user changed');
					const userStore = useUserStore();
					this.user = userStore.user;
					console.log(this.user);
					return this.user;
				},
				deep: true,
			},
		},
	};
</script>
