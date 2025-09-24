import { Component, inject } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';

interface AnalysisResult {
  verdict: string;
  score: string;
  reasoning: string;
  evidence: string;
  warnings: string;
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'fact-chex';
  searchQuery: string = '';
  showModal: boolean = false;
  analysisResult: AnalysisResult | null = null;
  isLoading: boolean = false;

  private http = inject(HttpClient);

  search(): void {
    if (!this.searchQuery.trim()) {
      return;
    }

    this.isLoading = true;
    this.showModal = true;

    this.http.post<AnalysisResult>('http://127.0.0.1:8000/fact-check', { claim: this.searchQuery })
      .subscribe({
        next: (data) => {
          console.log('API response:', data);
          this.analysisResult = data;
          this.isLoading = false;
        },
        error: (error) => {
          console.error('API call failed:', error);
          this.analysisResult = {
            verdict: 'ERROR',
            score: 'N/A',
            reasoning: 'Failed to get a response from the fact-checking service.',
            evidence: '',
            warnings: 'Please check if the backend server is running and accessible.'
          };
          this.isLoading = false;
        }
      });
  }

  closeModal(): void {
    this.showModal = false;
    this.analysisResult = null;
  }
}
