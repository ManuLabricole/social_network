<template>
	<NavigationBar />
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

	export default {
		setup() {
			const userStore = useUserStore();

			return {
				userStore,
			};
		},

		components: {
			NavigationBar,
			Toast,
		},

		beforeCreate() {
			this.userStore.initStore();

			const token = this.userStore.user.access;

			if (token) {
				axios.defaults.headers.common['Authorization'] = 'Bearer ' + token;
			} else {
				axios.defaults.headers.common['Authorization'] = '';
			}
		},
	};
</script>
