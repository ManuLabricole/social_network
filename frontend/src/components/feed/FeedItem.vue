<template>
	<div
		class="p-4 bg-white border border-gray-200 rounded-lg"
		:key="post.id">
		<div class="mb-6 flex items-center justify-between">
			<div class="flex items-center space-x-6">
				<router-link
					:to="{ name: 'profile', params: { id: post.author.user.id } }">
					<img
						src="https://i.pravatar.cc/300?img=70"
						class="w-[40px] rounded-full" />
				</router-link>

				<p>
					<strong>{{ post.author.user.name }}</strong>
				</p>
			</div>
			<p class="text-gray-600 text-center">
				{{ post.created_at_formatted }} ago
			</p>
		</div>
		<p class="text-2xl font-semibold mb-4 text-center">{{ post.title }}</p>
		<img
			src="https://images.unsplash.com/photo-1661956602868-6ae368943878?ixlib=rb-4.0.3&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2670&q=80"
			class="w-full rounded-lg" />
		<p>{{ post.body }}</p>
		<div class="my-6 flex justify-between">
			<div class="flex space-x-6">
				<div class="flex items-center space-x-2">
					<button @click="likePost(post.id)">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							fill="none"
							viewBox="0 0 24 24"
							stroke-width="1.5"
							stroke="currentColor"
							:class="[
								post.isLike ? 'liked' : 'unliked',
								animateLike
									? post.isLike
										? 'like-animation'
										: 'unlike-animation'
									: '',
							]"
							class="w-6 h-6">
							<path
								class=""
								stroke-linecap="round"
								stroke-linejoin="round"
								d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z" />
						</svg>
					</button>

					<span class="text-gray-500 text-xs"
						>{{ post.likes.length }}
						{{ post.likes.length <= 1 ? 'like' : 'likes' }}</span
					>
				</div>

				<div class="flex items-center space-x-2">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.5"
						stroke="currentColor"
						class="w-6 h-6">
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z" />
					</svg>
					<span class="text-gray-500 text-xs"
						>{{ post.comments.length }}
						{{ post.comments.length <= 1 ? 'comment' : 'comments' }}</span
					>
				</div>
			</div>

			<div>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke-width="1.5"
					stroke="currentColor"
					class="w-6 h-6">
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z" />
				</svg>
			</div>
		</div>
		<p class="text-gray-500 text-xs italic mb-2 text-center">
			Here the comment section
		</p>
	</div>
</template>

<script>
	import axios from 'axios';
	export default {
		name: 'FeedItem',
		props: {
			post: {
				type: Object,
				required: true,
			},
		},
		data() {
			return {
				animateLike: false,
			};
		},

		methods: {
			likePost(postId) {
				this.animateLike = true;
				axios
					.post(`/api/v1/posts/${postId}/like`)
					.then((response) => {
						this.$emit('post-updated', response.data.post);
					})
					.catch((error) => {
						console.log(error);
					});
			},
		},
	};
</script>
<style scoped>
	@keyframes pop {
		0% {
			fill: transparent;
			transform: scale(1);
		}
		50% {
			transform: scale(1.2);
		}
		100% {
			transform: scale(1);
			fill: red;
		}
	}

	@keyframes shake {
		0% {
			transform: rotate(0deg);
			fill: red;
		}
		25% {
			transform: rotate(-5deg);
		}
		50% {
			transform: rotate(5deg);
		}
		75% {
			transform: rotate(-5deg);
		}
		100% {
			transform: rotate(0deg);
			fill: transparent;
		}
	}

	.liked {
		fill: red;
		stroke: red;
	}

	.unliked {
		fill: transparent;
		stroke: gray;
	}

	.like-animation {
		animation: pop 0.5s;
	}

	.unlike-animation {
		animation: shake 0.5s;
	}
</style>
