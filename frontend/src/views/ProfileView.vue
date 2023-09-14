<template>
	<div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
		<div class="main-left col-span-1">
			<div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
				<img
					src="https://i.pravatar.cc/300?img=70"
					class="mb-6 rounded-full" />

				<p>
					<strong>{{ profile.name }}</strong>
				</p>
				<div class="mt-6 flex space-x-8 justify-around">
					<p class="text-xs text-gray-500">182 friends</p>
					<p class="text-xs text-gray-500">120 posts</p>
				</div>
			</div>
		</div>
		<div class="main-center col-span-2 space-y-4">
			<FeedItem
				v-for="post in posts"
				v-bind:key="post.id"
				v-bind:post="post" />
		</div>
		<div class="main-right col-span-1 space-y-4">
			<PeopleYouMainKnow />
			<Trends />
		</div>
	</div>
</template>

<script>
	import PeopleYouMainKnow from '../components/PeopleYouMainKnow.vue';
	import Trends from '../components/Trends.vue';
	import FeedItem from '../components/FeedItem.vue';
	import axios from 'axios';
	export default {
		name: 'ProfileView',
		components: {
			PeopleYouMainKnow,
			Trends,
			FeedItem,
		},
		props: {
			id: {
				type: String,
				required: true,
			},
		},
		setup(props) {
			return {
				profileId: props.id,
			};
		},

		data() {
			return {
				posts: [],
				postBody: '',
				profile: {},
			};
		},
		watch: {
			id() {
				this.profileId = this.id;
				this.fetchProfile();
				this.getPostsByUserId();
				console.log('watching');
			},
		},
		mounted() {
			this.fetchProfile();
			this.getPostsByUserId();
		},
		methods: {
			getPostsByUserId() {
				axios
					.get(`/api/v1/posts/user/${this.profileId}/`)
					.then((response) => {
						console.log(response);
						this.posts = response.data;
					})
					.catch((error) => {
						console.error(error);
						console.warn('Error getting feed');
					});
			},
			fetchProfile() {
				axios
					.get(`/api/v1/user/${this.profileId}/`)
					.then((response) => {
						console.log(response);
						this.profile = response.data;
						console.log(this.profile.name);
					})
					.catch((error) => {
						console.error(error);
						console.warn('Error getting profile');
					});
			},
		},
	};
</script>

<style lang="postcss" scoped></style>
