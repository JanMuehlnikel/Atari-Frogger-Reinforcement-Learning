import os
import json

class EpisodeLogger:
    def __init__(self, log_file_path="logs/episode_logs.json"):
        self.log_file_path = log_file_path
        os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
        self.logs = []

    def log_episode(self, episode, total_reward, moving_average, episode_max_travelled_distance, epsilon, step_count, episode_step_distances, average_distance_travelled_per_episode):
        episode_log = {
            "episode": episode,
            "total_reward": total_reward,
            "moving_average": moving_average,
            "max_travelled_distance": episode_max_travelled_distance,
            "epsilon": epsilon,
            "steps": step_count,
            "step_distances": episode_step_distances,
            "avg_distance_travelled_per_episode": average_distance_travelled_per_episode
        }
        self.logs.append(episode_log)
        self._save_all_logs()

    def _save_all_logs(self):
        with open(self.log_file_path, 'w') as f:
            json.dump(self.logs, f, indent=4)