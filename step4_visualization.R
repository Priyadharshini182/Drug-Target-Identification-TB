library(ggplot2)
library(dplyr)

cat("Loading data...\n")
aa_data    <- read.csv("data/aa_composition.csv")
blast_data <- read.csv("data/blast_results.csv")

# CHART 1: Amino Acid Composition
aa_data$AminoAcid <- factor(aa_data$AminoAcid,
  levels = aa_data$AminoAcid[order(-aa_data$Percentage)])

chart1 <- ggplot(aa_data, aes(x=AminoAcid,
                               y=Percentage,
                               fill=Percentage)) +
  geom_bar(stat="identity") +
  geom_text(aes(label=paste0(round(Percentage,1),"%")),
            vjust=-0.5, size=2.8) +
  scale_fill_gradient(low="#3498db", high="#e74c3c") +
  labs(title="Amino Acid Composition of InhA Protein",
       subtitle="Drug Target: M. tuberculosis | TB",
       x="Amino Acid", y="Composition (%)") +
  theme_minimal() +
  theme(legend.position="none")

ggsave("output/chart1_aa_composition.png",
       plot=chart1, width=10, height=6, dpi=300)
cat("✅ Chart 1 saved!\n")

# CHART 2: BLAST Identity
chart2 <- ggplot(blast_data,
                  aes(x=reorder(paste0("Hit",Rank), Identity_pct),
                      y=Identity_pct, fill=Identity_pct)) +
  geom_bar(stat="identity") +
  geom_text(aes(label=paste0(Identity_pct,"%")),
            hjust=-0.2, size=3.5) +
  scale_fill_gradient(low="#f39c12", high="#27ae60") +
  coord_flip() +
  labs(title="BLAST Results - Sequence Identity",
       x="BLAST Hit", y="Identity (%)") +
  theme_minimal() +
  theme(legend.position="none") +
  ylim(0, 115)

ggsave("output/chart2_blast_identity.png",
       plot=chart2, width=10, height=6, dpi=300)
cat("✅ Chart 2 saved!\n")

# CHART 3: E-value Plot
chart3 <- ggplot(blast_data,
                  aes(x=Rank, y=-log10(E_value + 1e-200),
                      color=Identity_pct)) +
  geom_point(size=5) +
  geom_line(color="gray70") +
  scale_color_gradient(low="#e74c3c", high="#2ecc71",
                       name="Identity %") +
  labs(title="BLAST Hits - E-value Significance",
       x="BLAST Hit Rank", y="-log10(E-value)") +
  theme_minimal()

ggsave("output/chart3_evalue.png",
       plot=chart3, width=9, height=5, dpi=300)
cat("✅ Chart 3 saved!\n")
cat("🎉 ALL CHARTS DONE! Check output/ folder.\n")