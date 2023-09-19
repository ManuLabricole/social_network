<template>
	<div
		v-if="isProfileFetched"
		class="p-4 bg-white border border-gray-200 text-center rounded-lg">
		<img
			src="https://i.pravatar.cc/300?img=70"
			class="mb-6 rounded-full" />

		<p>
			<strong>{{ profile.user.name }}</strong>
		</p>
		<div class="mt-6 flex space-x-8 justify-around">
			<p class="text-xs text-gray-500">{{ profile.friends.length }} friends</p>
			<p class="text-xs text-gray-500">120 posts</p>
		</div>
	</div>
	<div v-else>Error while getting your profile info</div>
</template>

<script>
	import axios from 'axios';
	export default {
		name: 'MyProfile',
		setup() {
			return {};
		},
		data() {
			return {
				profile: {},
				isProfileFetched: false,
			};
		},

		mounted() {
			this.fetchProfileInfo();
		},

		methods: {
			fetchProfileInfo() {
				axios
					.get('/api/v1/users/me/')
					.then((response) => {
						this.profile = response.data;
						this.isProfileFetched = true;
					})
					.catch((error) => {
						console.error(error);
						console.warn('Error getting profile');
						this.isProfileFetched = false;
					});
			},
		},
	};
</script>

<style lang="scss" scoped></style>
